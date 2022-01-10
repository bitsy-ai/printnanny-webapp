from __future__ import annotations
import subprocess
import hashlib
import logging
import tempfile
import requests
import os
from typing import Tuple, TypedDict
from zipfile import ZipFile

from django.apps import apps
from django.http import FileResponse
from django.http.request import HttpRequest
from django.conf import settings
from rest_framework.renderers import JSONRenderer
from google.cloud import iot_v1 as cloudiot_v1
import google.api_core.exceptions
from django.template.loader import render_to_string

from print_nanny_webapp.devices.api.serializers import LicenseSerializer
from print_nanny_webapp.utils.api.service import get_api_config
from print_nanny_webapp.utils.api.serializers import PrintNannyApiConfigSerializer
from print_nanny_webapp.users.api.serializers import UserSerializer

from .models import Device, CloudiotDevice, License
from .constants import FileLocator

logger = logging.getLogger(__name__)


class CACerts(TypedDict):
    ca_certs: str
    checksum: str


class KeyPair(TypedDict):
    private_key: str
    private_key_filename: str
    public_key: str
    public_key_filename: str
    fingerprint: str
    # ca_certs: CACerts


def render_janus_env(device: Device) -> str:
    context = dict(
        janus_admin_secret=device.janus_admin_secret, janus_token=device.janus_token
    )
    return render_to_string("janus.env.j2", context)


def render_honeycomb_env() -> str:
    context = dict(
        honeycomb_dataset=settings.HONEYCOMB_DATASET,
        honeycomb_api_key=settings.HONEYCOMB_API_KEY,
    )
    return render_to_string("honeycomb.env.j2", context)


def check_ca_certs():

    if not os.path.exists(FileLocator.CA_CERTS_FILENAME):

        with open("primary_ca.crt", "wb+") as f:
            res = requests.get(settings.GCP_LTS_CA_PRIMARY)
            f.write(res.content)

        subprocess.run(
            [
                "openssl",
                "x509",
                "-inform",
                "DER",
                "-in",
                "primary_ca.crt",
                "-out",
                "primary_ca.pem",
            ],
            capture_output=True,
        )
        with open("backup_ca.crt", "wb+") as f:
            res = requests.get(settings.GCP_LTS_CA_BACKUP)
            f.write(res.content)
        subprocess.run(
            [
                "openssl",
                "x509",
                "-inform",
                "DER",
                "-in",
                "backup_ca.crt",
                "-out",
                "backup_ca.pem",
            ],
            capture_output=True,
        )

    with open(FileLocator.CA_CERTS_FILENAME, "rb") as f:
        ca_certs_content = f.read()
        ca_certs_checksum = hashlib.sha256(ca_certs_content).hexdigest()

    return CACerts(
        ca_certs=ca_certs_content.decode("utf8"),
        checksum=ca_certs_checksum,
    )


def generate_keypair(tmp: str):

    # ca_certs = check_ca_certs()

    sec1_filename = f"{tmp}/{FileLocator.KEY_PRIVATE_SEC1_FILENAME}"
    pkcs8_filename = f"{tmp}/{FileLocator.KEY_PRIVATE_PKCS8_FILENAME}"
    public_key_filename = f"{tmp}/{FileLocator.KEY_PUBLIC_FILENAME}"

    p = subprocess.check_output(
        [
            "openssl",
            "ecparam",
            "-genkey",
            "-name",
            "prime256v1",
            "-noout",
            "-out",
            sec1_filename,
        ],
    )
    # Keats/jsonwebtoken crate only supports PKCS8 format for private EC keys
    # https://github.com/Keats/jsonwebtoken#convert-sec1-private-key-to-pkcs8
    p = subprocess.check_output(
        [
            "openssl",
            "pkcs8",
            "-topk8",
            "-nocrypt",
            "-in",
            sec1_filename,
            "-out",
            pkcs8_filename,
        ],
    )

    p = subprocess.check_output(
        [
            "openssl",
            "ec",
            "-in",
            sec1_filename,
            "-pubout",
            "-out",
            public_key_filename,
        ],
    )

    p = subprocess.check_output(
        [
            "openssl",
            "sha3-256",
            "-c",
            public_key_filename,
        ],
    )
    fingerprint = p.decode().split("=")[-1]
    fingerprint = fingerprint.strip()
    logger.info(fingerprint)

    with open(public_key_filename, "rb") as f:
        public_key_content = f.read()

    with open(pkcs8_filename, "rb") as f:
        private_key_content = f.read()

    return KeyPair(
        private_key_filename=pkcs8_filename,
        public_key_filename=public_key_filename,
        private_key=private_key_content.decode("utf8"),
        public_key=public_key_content.decode("utf8"),
        fingerprint=fingerprint,
        # ca_certs=ca_certs,
    )


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


def create_cloudiot_device(device: Device, keypair: KeyPair):
    client = cloudiot_v1.DeviceManagerClient()
    parent = client.registry_path(
        settings.GCP_PROJECT_ID,
        settings.GCP_CLOUD_IOT_DEVICE_REGISTRY_REGION,
        settings.GCP_CLOUD_IOT_STANDALONE_DEVICE_REGISTRY,
    )

    cloudiot_device = cloudiot_v1.types.Device()
    cloudiot_device.id = device.to_cloudiot_id
    cloudiot_device.credentials = [
        {
            "public_key": {
                "format": cloudiot_v1.PublicKeyFormat.ES256_PEM,
                "key": keypair["public_key"],
            }
        }
    ]
    cloudiot_device.metadata = dict(
        fingerprint=keypair["fingerprint"],
        device_id=str(device.id),
        device_hostname=device.hostname,
        user_id=str(device.user.id),
        email=device.user.email,
    )

    return client.create_device(parent=parent, device=cloudiot_device)


def update_cloudiot_device(
    cloudiot_device: cloudiot_v1.types.Device, device: Device, keypair: KeyPair
):
    client = cloudiot_v1.DeviceManagerClient()
    cloudiot_device.credentials = [
        {
            "public_key": {
                "format": cloudiot_v1.PublicKeyFormat.ES256_PEM,
                "key": keypair["public_key"],
            }
        }
    ]
    cloudiot_device.metadata = dict(
        fingerprint=keypair["fingerprint"],
        device_id=str(device.id),
        device_hostname=device.hostname,
        user_id=str(device.user.id),
        email=device.user.email,
    )
    # google.api_core.exceptions.InvalidArgument: 400 The fields 'device.id' and 'device.num_id' must be empty.
    del cloudiot_device.num_id
    del cloudiot_device.id

    request = cloudiot_v1.types.UpdateDeviceRequest(
        device=cloudiot_device, update_mask={"paths": ["credentials", "metadata"]}
    )
    return client.update_device(request=request)


def update_or_create_cloudiot_device(
    device: Device, keypair: KeyPair
) -> cloudiot_v1.Device:
    # request to Cloud IoT API
    client = cloudiot_v1.DeviceManagerClient()

    device_path = client.device_path(
        settings.GCP_PROJECT_ID,
        settings.GCP_CLOUD_IOT_DEVICE_REGISTRY_REGION,
        settings.GCP_CLOUD_IOT_STANDALONE_DEVICE_REGISTRY,
        device.to_cloudiot_id,
    )

    try:
        existing_cloudiot_device: cloudiot_v1.types.Device = client.get_device(
            name=device_path
        )
        return update_cloudiot_device(existing_cloudiot_device, device, keypair)
    except google.api_core.exceptions.NotFound:
        return create_cloudiot_device(device, keypair)


def generate_keypair_and_update_or_create_cloudiot_device(
    device: Device, tmp: str
) -> Tuple[KeyPair, License, CloudiotDevice]:
    keypair = generate_keypair(tmp)
    # revoke all existing licenses (soft-delete)
    device.licenses.all().delete()

    cloudiot_device = update_or_create_cloudiot_device(device=device, keypair=keypair)
    CloudiotDevice = apps.get_model("devices", "CloudiotDevice")

    # update apppliance relationships
    if device.cloudiot_devices.first():
        device.cloudiot_devices.update(
            num_id=cloudiot_device.num_id,
            name=cloudiot_device.name,
        )
    else:
        # create new print_nanny_webapp.devices.models.CloudiotDevices object
        CloudiotDevice.objects.create(
            num_id=cloudiot_device.num_id,
            name=cloudiot_device.name,
            device=device,
        )

    license = License.objects.create(
        public_key=keypair["public_key"],
        fingerprint=keypair["fingerprint"],
        device=device,
    )
    return keypair, license, device.cloudiot_devices.first()


def generate_zipped_license_file(
    device: Device,
    request: HttpRequest,
    tmp: str,
) -> str:
    from .api.serializers import DeviceSerializer

    keypair, license, _ = generate_keypair_and_update_or_create_cloudiot_device(
        device, tmp
    )
    zip_filename = f"{tmp}/{FileLocator.LICENSE_ZIP_FILENAME}"

    user_serializer = UserSerializer(device.user, context=dict(request=request))
    user_json = JSONRenderer().render(user_serializer.data)

    device_serializer = DeviceSerializer(device, context=dict(request=request))
    device_json = JSONRenderer().render(device_serializer.data)

    license_serializer = LicenseSerializer(license, context=dict(request=request))
    license_json = JSONRenderer().render(license_serializer.data)

    api_config = get_api_config(request)
    api_config_serializer = PrintNannyApiConfigSerializer(instance=api_config)
    api_config_json = JSONRenderer().render(api_config_serializer.data)

    with ZipFile(zip_filename, "x") as zf:
        # write keypair to zipfile
        zf.write(
            keypair["public_key_filename"],
            arcname=os.path.basename(keypair["public_key_filename"]),
        )
        zf.write(
            keypair["private_key_filename"],
            arcname=os.path.basename(keypair["private_key_filename"]),
        )
        zf.writestr("honeycomb.env", render_honeycomb_env())
        zf.writestr("janus.env", render_janus_env())
        zf.writestr("device.json", device_json)
        zf.writestr("license.json", license_json)
        zf.writestr("api_config.json", api_config_json)
        zf.writestr("user.json", user_json)

    return zip_filename


def generate_zipped_license_response(
    device: Device, request: HttpRequest
) -> FileResponse:

    with tempfile.TemporaryDirectory() as tmp:
        filename = generate_zipped_license_file(device, request, tmp)
        # some_file = self.model.objects.get(imported_file=filename)
        response = FileResponse(open(filename, "rb"), content_type="application/zip")
        # https://docs.djangoproject.com/en/1.11/howto/outputting-csv/#streaming-large-csv-files
        response[
            "Content-Disposition"
        ] = f'attachment; filename="{FileLocator.LICENSE_ZIP_FILENAME}"'
        return response
