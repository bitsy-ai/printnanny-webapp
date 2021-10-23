from __future__ import annotations

from typing import Tuple
import hashlib
import logging
import tempfile
import requests
import os
from django.apps import apps
from typing import TypedDict
from django.conf import settings
from google.cloud import iot_v1 as cloudiot_v1
import google.api_core.exceptions
import subprocess

from .models import Appliance, CloudIoTDevice

logger = logging.getLogger(__name__)


class CACerts(TypedDict):
    primary: str
    primary_checksum: str
    backup: str
    backup_checksum: str


class KeyPair(TypedDict):
    private_key: str
    private_key_checksum: str
    public_key: str
    public_key_checksum: str
    fingerprint: str
    # TODO x509
    # ca_certs: CACerts


def check_ca_certs():

    if not os.path.exists("primary_ca.pem"):
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
    with open("primary_ca.pem", "rb") as f:
        primary_ca_content = f.read()
        primary_ca_checksum = hashlib.sha256(primary_ca_content).hexdigest()

    if not os.path.exists("backup_ca.pem"):
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
    with open("backup_ca.pem", "rb") as f:
        backup_ca_content = f.read()
        backup_ca_checksum = hashlib.sha256(backup_ca_content).hexdigest()

    return CACerts(
        primary=primary_ca_content.decode("utf8"),
        backup=backup_ca_content.decode("utf8"),
        primary_checksum=primary_ca_checksum,
        backup_checksum=backup_ca_checksum,
    )


def generate_keypair():

    # TODO x509
    # ca_certs = check_ca_certs()

    with tempfile.TemporaryDirectory() as tmp:
        keypair_filename = f"{tmp}/ecdsa256_keypair.pem"
        public_key_filename = f"{tmp}/ecdsa_public.pem"

        p = subprocess.check_output(
            [
                "openssl",
                "ecparam",
                "-genkey",
                "-name",
                "prime256v1",
                "-noout",
                "-out",
                keypair_filename,
            ],
        )

        p = subprocess.check_output(
            [
                "openssl",
                "ec",
                "-in",
                keypair_filename,
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
            public_key_checksum = hashlib.sha256(public_key_content).hexdigest()

        with open(keypair_filename, "rb") as f:
            private_key_content = f.read()
            private_key_checksum = hashlib.sha256(private_key_content).hexdigest()

        return KeyPair(
            private_key=private_key_content.decode("utf8"),
            private_key_checksum=private_key_checksum,
            public_key=public_key_content.decode("utf8"),
            public_key_checksum=public_key_checksum,
            fingerprint=fingerprint,
        )


def delete_cloudiot_device(device_id_int64: int):

    client = cloudiot_v1.DeviceManagerClient()
    device_path = client.device_path(
        settings.GCP_PROJECT_ID,
        settings.GCP_CLOUD_IOT_DEVICE_REGISTRY_REGION,
        settings.GCP_CLOUD_IOT_DEVICE_REGISTRY,
        str(device_id_int64),
    )
    try:
        return client.delete_device(name=device_path)
    except google.api_core.exceptions.NotFound as e:
        logger.error(e)


def create_cloudiot_device(appliance: Appliance, keypair: KeyPair):
    client = cloudiot_v1.DeviceManagerClient()
    parent = client.registry_path(
        settings.GCP_PROJECT_ID,
        settings.GCP_CLOUD_IOT_DEVICE_REGISTRY_REGION,
        settings.GCP_CLOUD_IOT_DEVICE_REGISTRY,
    )

    device = cloudiot_v1.types.Device()
    device.id = appliance.to_cloudiot_id
    device.credentials = [
        {
            "public_key": {
                "format": cloudiot_v1.PublicKeyFormat.ES256_PEM,
                "key": keypair["public_key"],
            }
        }
    ]
    device.metadata = dict(
        fingerprint=keypair["fingerprint"],
        appliance_id=str(appliance.id),
        appliance_hostname=appliance.hostname,
        user_id=str(appliance.user.id),
        email=appliance.user.email,
    )

    return client.create_device(parent=parent, device=device)


def update_cloudiot_device(
    device: cloudiot_v1.types.Device, appliance: Appliance, keypair: KeyPair
):
    client = cloudiot_v1.DeviceManagerClient()
    device.credentials = [
        {
            "public_key": {
                "format": cloudiot_v1.PublicKeyFormat.ES256_PEM,
                "key": keypair["public_key"],
            }
        }
    ]
    device.metadata = dict(
        fingerprint=keypair["fingerprint"],
        appliance_id=str(appliance.id),
        appliance_hostname=appliance.hostname,
        user_id=str(appliance.user.id),
        email=appliance.user.email,
    )
    # google.api_core.exceptions.InvalidArgument: 400 The fields 'device.id' and 'device.num_id' must be empty.
    del device.num_id
    del device.id

    request = cloudiot_v1.types.UpdateDeviceRequest(
        device=device, update_mask={"paths": ["credentials", "metadata"]}
    )
    return client.update_device(request=request)


def update_or_create_cloudiot_device(
    appliance: Appliance, keypair: KeyPair
) -> cloudiot_v1.Device:
    # request to Cloud IoT API
    client = cloudiot_v1.DeviceManagerClient()

    device_path = client.device_path(
        settings.GCP_PROJECT_ID,
        settings.GCP_CLOUD_IOT_DEVICE_REGISTRY_REGION,
        settings.GCP_CLOUD_IOT_DEVICE_REGISTRY,
        appliance.to_cloudiot_id,
    )

    try:
        existing_cloudiot_device: cloudiot_v1.types.Device = client.get_device(
            name=device_path
        )
        return update_cloudiot_device(existing_cloudiot_device, appliance, keypair)
    except google.api_core.exceptions.NotFound:
        return create_cloudiot_device(appliance, keypair)


def generate_keypair_and_update_or_create_cloudiot_device(
    appliance: Appliance,
) -> Tuple[KeyPair, CloudIoTDevice]:
    keypair = generate_keypair()
    cloudiot_device = update_or_create_cloudiot_device(
        appliance=appliance, keypair=keypair
    )
    CloudIoTDevice = apps.get_model("devices", "CloudIoTDevice")
    AppliancePublicKey = apps.get_model("devices", "AppliancePublicKey")

    # update apppliance relationships
    if appliance.cloudiot_devices.first():
        appliance.cloudiot_devices.update(
            num_id=cloudiot_device.num_id,
            name=cloudiot_device.name,
        )
    else:
        # create new print_nanny_webapp.devices.models.CloudIoTDevices object
        CloudIoTDevice.objects.create(
            num_id=cloudiot_device.num_id,
            name=cloudiot_device.name,
            appliance=appliance,
        )
    if appliance.public_keys.first():
        appliance.public_keys.update(
            public_key=keypair["public_key"],
            public_key_checksum=keypair["public_key_checksum"],
            fingerprint=keypair["fingerprint"],
            appliance=appliance,
        )
    else:
        AppliancePublicKey.objects.create(
            public_key=keypair["public_key"],
            public_key_checksum=keypair["public_key_checksum"],
            fingerprint=keypair["fingerprint"],
            appliance=appliance,
        )
    return keypair, appliance.cloudiot_devices.first()
