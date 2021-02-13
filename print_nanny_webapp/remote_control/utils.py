import hashlib
import logging
import tempfile

from typing import TypedDict
from django.conf import settings
from google.cloud import iot_v1 as cloudiot_v1
from google.protobuf.json_format import MessageToDict
import google.api_core.exceptions
import subprocess

logger = logging.getLogger(__name__)


class RSAKeyPair(TypedDict):
    private_key_content: str
    private_key_checksum: str
    public_key_content: str
    public_key_checksum: str
    fingerprint: str


def generate_keypair():
    with tempfile.TemporaryDirectory() as tmp:
        keypair_filename = f"{tmp}/ec256_keypair.pem"
        public_key_filename = f"{tmp}/ec_public.pem"

        p = subprocess.run(
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
            capture_output=True,
        )

        p = subprocess.run(
            [
                "openssl",
                "ec",
                "-in",
                keypair_filename,
                "-pubout",
                "-out",
                public_key_filename,
            ],
            capture_output=True,
        )
        p = subprocess.run(
            [
                "openssl",
                "sha3-256",
                "-c",
                public_key_filename,
            ],
            capture_output=True,
        )
        fingerprint = p.stdout
        fingerprint = fingerprint.decode().split("=")[-1]
        fingerprint = fingerprint.strip()

        with open(public_key_filename, "rb") as f:
            public_key_content = f.read()
            f.seek(0)
            public_key_checksum = hashlib.sha256(f.read()).hexdigest()

        with open(keypair_filename, "rb") as f:
            private_key_content = f.read()
            f.seek(0)
            private_key_checksum = hashlib.sha256(f.read()).hexdigest()

        return RSAKeyPair(
            private_key_content=private_key_content,
            private_key_checksum=private_key_checksum,
            public_key_content=public_key_content,
            public_key_checksum=public_key_checksum,
            fingerprint=fingerprint,
        )


def create_cloudiot_device(
    name: str,
    serial: str,
    user_id: int,
    metadata: dict,
    fingerprint: str,
    public_key_content: str,
):
    client = cloudiot_v1.DeviceManagerClient()
    parent = client.registry_path(
        settings.GCP_PROJECT_ID,
        settings.GCP_CLOUD_IOT_DEVICE_REGISTRY_REGION,
        settings.GCP_CLOUD_IOT_DEVICE_REGISTRY,
    )

    string_kwargs = {k: str(v) for k, v in metadata.items()}
    device_template = {
        "id": name,
        "credentials": [
            {
                "public_key": {
                    "format": cloudiot_v1.PublicKeyFormat.ES256_PEM,
                    "key": public_key_content,
                }
            }
        ],
        "metadata": {
            "user_id": str(user_id),
            "serial": serial,
            "fingerprint": fingerprint,
            **string_kwargs,
        },
    }
    return client.create_device(parent=parent, device=device_template)


def update_cloudiot_device(
    device: cloudiot_v1.types.Device,
    name: str,
    serial: str,
    user_id: int,
    metadata: dict,
    fingerprint: str,
    public_key_content: str,
):
    client = cloudiot_v1.DeviceManagerClient()
    string_kwargs = {k: str(v) for k, v in metadata.items()}
    device.credentials = [
        {
            "public_key": {
                "format": cloudiot_v1.PublicKeyFormat.ES256_PEM,
                "key": public_key_content,
            }
        }
    ]
    device.metadata = {
        "user_id": str(user_id),
        "serial": serial,
        "fingerprint": fingerprint,
        **string_kwargs,
    }
    del device.id
    del device.num_id
    return client.update_device(
        device=device, update_mask={"paths": ["credentials", "metadata"]}
    )


def update_or_create_cloudiot_device(
    name: str,
    serial: str,
    user_id: int,
    metadata: dict,
    fingerprint: str,
    public_key_content: str,
):
    client = cloudiot_v1.DeviceManagerClient()

    device_path = client.device_path(
        settings.GCP_PROJECT_ID,
        settings.GCP_CLOUD_IOT_DEVICE_REGISTRY_REGION,
        settings.GCP_CLOUD_IOT_DEVICE_REGISTRY,
        name,
    )

    try:
        cloudiot_device = client.get_device(name=device_path)
        cloudiot_device = update_cloudiot_device(
            cloudiot_device,
            name,
            serial,
            user_id,
            metadata,
            fingerprint,
            public_key_content,
        )
    except google.api_core.exceptions.NotFound as e:
        cloudiot_device = create_cloudiot_device(
            name, serial, user_id, metadata, fingerprint, public_key_content
        )

    cloudiot_device_dict = MessageToDict(cloudiot_device._pb)
    return cloudiot_device_dict, device_path
