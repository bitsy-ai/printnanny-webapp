import pytest
import tempfile
from django.conf import settings
from print_nanny_webapp.remote_control.utils import (
    delete_and_recreate_cloudiot_device,
    generate_keypair,
)


def test_generate_keypair():
    with tempfile.TemporaryDirectory() as tmp:
        tmp_private_key_filename = f"{tmp}/test_rsa_private.pem"
        tmp_public_key_filename = f"{tmp}/test_rsa_public.pem"
        _, _public_key_content, _private_key_content = generate_keypair(
            tmp_private_key_filename, tmp_public_key_filename
        )

        with open(tmp_public_key_filename) as f:
            public_key_content = f.read().strip()

        with open(tmp_private_key_filename) as f:
            private_key_content = f.read().strip()

        assert public_key_content == _public_key_content
        assert private_key_content == _private_key_content


def test_delete_and_recrease_cloudiot_device(mocker):

    serial = "1234"
    expected_name = f"serial-{serial}"
    user_id = 1
    metadata = {"meta": "data"}
    fingerprint = "fingerprint"
    public_key_content = "public key content"

    mock_cloudiot = mocker.patch("print_nanny_webapp.remote_control.utils.cloudiot_v1")

    cloudiot_device, device_path = delete_and_recreate_cloudiot_device(
        serial=serial,
        user_id=user_id,
        metadata=metadata,
        fingerprint=fingerprint,
        public_key_content=public_key_content,
    )


#
