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
        private_key_filename = f"{tmp}/{serial}_rsa_private.pem"
        public_key_filename = f"{tmp}/{serial}_rsa_public.pem"

        p = subprocess.run(
            [
                "openssl",
                "genpkey",
                "-algorithm",
                "RSA",
                "-out",
                private_key_filename,
                "-pkeyopt",
                "rsa_keygen_bits:2048",
            ],
            capture_output=True,
        )
        p = subprocess.run(
            [
                "openssl",
                "rsa",
                "-in",
                private_key_filename,
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
        
        with open(public_key_filename) as f:
            public_key_content = f.read()
            f.seek(0)
            public_key_checksum = hashlib.sha256(f.read()).hexdigest()

        with open(private_key_filename) as f:
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


def delete_and_recreate_cloudiot_device(
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
                    "format": cloudiot_v1.PublicKeyFormat.RSA_PEM,
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

    device_path = client.device_path(
        settings.GCP_PROJECT_ID,
        settings.GCP_CLOUD_IOT_DEVICE_REGISTRY_REGION,
        settings.GCP_CLOUD_IOT_DEVICE_REGISTRY,
        name,
    )

    try:
        cloudiot_device = client.delete_device(name=device_path)
        logger.info(f"Deleted existing device {device_path}")
    except google.api_core.exceptions.NotFound as e:
        logger.warning(
            {
                "error": e,
                "msg": f"No existing device found with name {name}",
            }
        )

    cloudiot_device = client.create_device(parent=parent, device=device_template)

    logger.info(f"Created new device in registry {device_path}")

    cloudiot_device_dict = MessageToDict(cloudiot_device._pb)
    return cloudiot_device_dict, device_path
