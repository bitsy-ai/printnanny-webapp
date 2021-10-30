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

from .models import Device, CloudiotDevice

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
    ca_certs: CACerts


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

    ca_certs = check_ca_certs()

    with tempfile.TemporaryDirectory() as tmp:
        sec1_filename = f"{tmp}/ecdsa256_sec1.pem"
        pkcs8_filename = f"{tmp}/ecdsa256.pem"
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
            public_key_checksum = hashlib.sha256(public_key_content).hexdigest()

        with open(pkcs8_filename, "rb") as f:
            private_key_content = f.read()
            private_key_checksum = hashlib.sha256(private_key_content).hexdigest()

        return KeyPair(
            private_key=private_key_content.decode("utf8"),
            private_key_checksum=private_key_checksum,
            public_key=public_key_content.decode("utf8"),
            public_key_checksum=public_key_checksum,
            fingerprint=fingerprint,
            ca_certs=ca_certs,
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
    device: Device,
) -> Tuple[KeyPair, CloudiotDevice]:
    keypair = generate_keypair()
    cloudiot_device = update_or_create_cloudiot_device(device=device, keypair=keypair)
    CloudiotDevice = apps.get_model("devices", "CloudiotDevice")
    DevicePublicKey = apps.get_model("devices", "DevicePublicKey")

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
    if device.public_keys.first():
        device.public_keys.update(
            public_key=keypair["public_key"],
            public_key_checksum=keypair["public_key_checksum"],
            fingerprint=keypair["fingerprint"],
            device=device,
        )
    else:
        DevicePublicKey.objects.create(
            public_key=keypair["public_key"],
            public_key_checksum=keypair["public_key_checksum"],
            fingerprint=keypair["fingerprint"],
            device=device,
        )
    return keypair, device.cloudiot_devices.first()
