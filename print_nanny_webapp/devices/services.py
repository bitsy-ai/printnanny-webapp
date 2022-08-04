from __future__ import annotations
import io
import logging
from uuid import uuid4
from typing import Tuple, Dict, Any
import requests
import zipfile
from google.cloud import iot_v1 as cloudiot_v1
import google.api_core.exceptions
from django.db import IntegrityError
from django.conf import settings
from django.template.loader import render_to_string
from django.http import HttpRequest
from rest_framework.renderers import JSONRenderer
from print_nanny_webapp.devices.api.serializers import (
    PrintNannyLicenseSerializer,
)
from print_nanny_webapp.devices.enum import JanusConfigType
from print_nanny_webapp.utils.api.serializers import PrintNannyApiConfigSerializer
from print_nanny_webapp.utils.api.service import get_api_config

from django_nats_nkeys.models import NatsOrganizationOwner
from django_nats_nkeys.services import (
    create_nats_account_org,
    nsc_generate_creds,
    create_nats_app,
)

from .models import CloudiotDevice, Pi, PiNatsApp, PublicKey, WebrtcStream

logger = logging.getLogger(__name__)


def janus_admin_add_token(stream: WebrtcStream) -> Dict[str, Any]:
    if stream.config_type == JanusConfigType.CLOUD:
        req = dict(
            janus="add_token",
            token=stream.api_token,
            admin_secret=settings.JANUS_CLOUD_ADMIN_SECRET,
            plugins=["janus.plugin.streaming"],
            transaction=uuid4().hex,
        )
        res = requests.post(stream.admin_url, json=req)
        logger.info("Got response to POST %s: %s", stream.admin_url, res)
        res.raise_for_status()
        return res.json()
    else:
        raise NotImplementedError(
            f"janus_admin_add_token not implemented in events.services for JanusConfigType={JanusConfigType.EDGE}"
        )


def render_janus_env(device: Pi) -> str:
    context = dict(
        janus_admin_secret=device.active_license.janus_admin_secret,
        janus_token=device.active_license.janus_token,
    )
    return render_to_string("janus.env.j2", context)


def render_honeycomb_env() -> str:
    context = dict(
        honeycomb_dataset=settings.HONEYCOMB_DATASET,
        honeycomb_api_key=settings.HONEYCOMB_API_KEY,
    )
    return render_to_string("honeycomb.env.j2", context)


def delete_cloudiot_device(device_id_int64: int):

    client = cloudiot_v1.DeviceManagerClient()
    device_path = client.device_path(
        settings.GCP_PROJECT_ID,
        settings.GCP_CLOUDIOT_DEVICE_REGISTRY_REGION,
        settings.GCP_CLOUDIOT_STANDALONE_DEVICE_REGISTRY,
        str(device_id_int64),
    )
    try:
        return client.delete_device(name=device_path)
    except google.api_core.exceptions.NotFound as e:
        logger.error(e)


def cloudiot_device_request(
    cloudiot_device: cloudiot_v1.types.Device, public_key: PublicKey
) -> cloudiot_v1.types.Device:
    cloudiot_device.credentials = [
        {
            "public_key": {
                "format": cloudiot_v1.PublicKeyFormat.ES256_PEM,
                "key": public_key.pem,
            }
        }
    ]
    cloudiot_device.metadata = dict(
        fingerprint=public_key.fingerprint,
        device_id=str(public_key.device.id),
        device_hostname=public_key.device.hostname,
        user_id=str(public_key.device.user.id),
        email=public_key.device.user.email,
    )
    return cloudiot_device


def create_cloudiot_device(public_key: PublicKey):

    client = cloudiot_v1.DeviceManagerClient()
    parent = client.registry_path(
        settings.GCP_PROJECT_ID,
        settings.GCP_CLOUDIOT_DEVICE_REGISTRY_REGION,
        settings.GCP_CLOUDIOT_STANDALONE_DEVICE_REGISTRY,
    )

    cloudiot_device = cloudiot_v1.types.Device()
    cloudiot_device.id = public_key.device.cloudiot_name
    cloudiot_device = cloudiot_device_request(cloudiot_device, public_key)

    return client.create_device(parent=parent, device=cloudiot_device)


def update_cloudiot_device(cloudiot_device: CloudiotDevice, public_key: PublicKey):
    client = cloudiot_v1.DeviceManagerClient()

    cloudiot_device = cloudiot_device_request(cloudiot_device, public_key)
    # google.api_core.exceptions.InvalidArgument: 400 The fields 'device.id' and 'device.num_id' must be empty.
    del cloudiot_device.num_id
    del cloudiot_device.id

    request = cloudiot_v1.types.UpdateDeviceRequest(
        device=cloudiot_device, update_mask={"paths": ["credentials", "metadata"]}
    )
    return client.update_device(request=request)


def update_or_create_cloudiot_device(
    public_key: PublicKey,
) -> Tuple[CloudiotDevice, bool]:
    client = cloudiot_v1.DeviceManagerClient()

    device_path = client.device_path(
        settings.GCP_PROJECT_ID,
        settings.GCP_CLOUDIOT_DEVICE_REGISTRY_REGION,
        settings.GCP_CLOUDIOT_STANDALONE_DEVICE_REGISTRY,
        public_key.device.cloudiot_name,
    )

    try:
        existing_cloudiot_device: cloudiot_v1.types.Device = client.get_device(
            name=device_path
        )
        gcp_response = update_cloudiot_device(existing_cloudiot_device, public_key)
        logger.info("Found cloudiot device, gcp_response=%s", gcp_response)
    except google.api_core.exceptions.NotFound:
        logger.info("Pi not found, attempting to create, gcp_response=%s", device_path)
        gcp_response = create_cloudiot_device(public_key)
        logger.info("Created cloudiot device, gcp_response=%s", gcp_response)
    try:
        obj, created = CloudiotDevice.objects.update_or_create(
            device=public_key.device,
            deleted=None,
            defaults=dict(
                public_key=public_key,
                num_id=gcp_response.num_id,
                name=gcp_response.name,
            ),
        )
    except IntegrityError as e:
        cloudiot_device = CloudiotDevice.objects.filter(
            device=public_key.device
        ).first()
        logger.warning(
            "CloudiotDevice.objects.update_or_create raised integrity error=%s. Updating cloudiot_deice %s",
            e,
            cloudiot_device,
        )
        cloudiot_device.public_key = public_key
        cloudiot_device.num_id = gcp_response.num_id
        cloudiot_device.name = gcp_response.name
        cloudiot_device.save()
        obj = cloudiot_device
        created = False
    logger.info("Saved CloudiotDevice model %s created=%s", obj, created)
    return obj, created


def janus_cloud_setup(device: Pi) -> Tuple[WebrtcStream, bool]:
    # 1) get or create WebrtcStream mountpoint
    stream, created = WebrtcStream.objects.get_or_create(
        device=device, config_type=JanusConfigType.CLOUD
    )
    logger.info(
        "Retrieved WebrtcStream id=%s user=%s created=%s",
        stream.id,
        device.user.id,
        created,
    )

    # 2) ensure token added to Janus Gateway
    # Janus stores tokens in memory, so added tokens are flushed on restart
    # janus_admin_add_token(janus_auth)
    logger.info("Retrieved WebrtcStream %s created=%s", stream, created)
    return stream, created


def create_pi_nats_app(pi: Pi) -> PiNatsApp:
    # is user already the owner of NatsOrganization?
    try:
        org_owner = NatsOrganizationOwner.objects.get(organization_user__user=pi.user)
        org = org_owner.organization
    except NatsOrganizationOwner.DoesNotExist:
        org = create_nats_account_org(pi.user)

    # create nats app associated with org user
    app = create_nats_app(pi.user, org, pi=pi)
    return app


def build_license_zip(pi: Pi, request: HttpRequest) -> bytes:
    api = get_api_config(request, user=pi.user)
    license_json = PritnNannyLicenseSerializer(api=api, pi=pi)

    # is there already a NatsApp associated with Pi?
    try:
        app = PiNatsApp.objects.get(pi=pi)
    # no app, step through NATS account + app creation process
    except PiNatsApp.DoesNotExist:
        app = create_pi_nats_app(pi)

    nats_creds = nsc_generate_creds(app.organization, app)

    creds_bundle = [
        ("license.json", JSONRenderer().render(license_json.data)),
        ("nats.creds", nats_creds),
    ]

    # do not write sensitive credentials to disk
    # instead, write to memory buffer
    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, "a") as zip_obj:
        for file_name, data in creds_bundle:
            zip_obj.writestr(file_name, data)
    return zip_buffer.getvalue()
