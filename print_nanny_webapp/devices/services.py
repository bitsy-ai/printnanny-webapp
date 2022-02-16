from __future__ import annotations
import logging
from typing import Tuple
from google.cloud import iot_v1 as cloudiot_v1
import google.api_core.exceptions
from django.conf import settings
from django.template.loader import render_to_string

from .models import (
    Device,
    CloudiotDevice,
    PublicKey,
)

logger = logging.getLogger(__name__)


def render_janus_env(device: Device) -> str:
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
        settings.GCP_CLOUD_IOT_DEVICE_REGISTRY_REGION,
        settings.GCP_CLOUD_IOT_STANDALONE_DEVICE_REGISTRY,
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
        settings.GCP_CLOUD_IOT_DEVICE_REGISTRY_REGION,
        settings.GCP_CLOUD_IOT_STANDALONE_DEVICE_REGISTRY,
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
) -> Tuple[cloudiot_v1.Device, bool]:
    client = cloudiot_v1.DeviceManagerClient()

    device_path = client.device_path(
        settings.GCP_PROJECT_ID,
        settings.GCP_CLOUD_IOT_DEVICE_REGISTRY_REGION,
        settings.GCP_CLOUD_IOT_STANDALONE_DEVICE_REGISTRY,
        public_key.device.cloudiot_name,
    )

    try:
        existing_cloudiot_device: cloudiot_v1.types.Device = client.get_device(
            name=device_path
        )
        gcp_response = update_cloudiot_device(existing_cloudiot_device, public_key)
    except google.api_core.exceptions.NotFound:
        logger.warning(f"Device not found {device_path} - creating")
        gcp_response = create_cloudiot_device(public_key)
    return CloudiotDevice.objects.update_or_create(
        public_key=public_key,
        device=public_key.device,
        num_id=gcp_response.num_id,
        name=gcp_response.name,
    )
