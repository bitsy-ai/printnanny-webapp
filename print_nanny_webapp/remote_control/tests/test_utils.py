import hashlib
import pytest
import tempfile
from django.conf import settings
import google.api_core.exceptions

from print_nanny_webapp.remote_control.utils import (
    update_or_create_cloudiot_device,
    generate_keypair,
)


def test_generate_keypair():
    rsa_keypair = generate_keypair()

    public_key_checksum = hashlib.sha256(rsa_keypair["public_key_content"]).hexdigest()
    assert public_key_checksum == rsa_keypair["public_key_checksum"]
    private_key_checksum = hashlib.sha256(
        rsa_keypair["private_key_content"]
    ).hexdigest()
    assert private_key_checksum == rsa_keypair["private_key_checksum"]


def test_update_cloudiot_device(mocker):

    serial = "1234"
    expected_name = f"serial-{serial}"
    user_id = 1
    metadata = {"meta": "data"}
    fingerprint = "fingerprint"
    public_key_b64 = "publickeyb64"

    mock_cloudiot = mocker.patch(
        "print_nanny_webapp.remote_control.utils.cloudiot_v1.DeviceManagerClient"
    )
    mocker.patch("print_nanny_webapp.remote_control.utils.MessageToDict")
    cloudiot_device, device_path = update_or_create_cloudiot_device(
        name=expected_name,
        serial=serial,
        user_id=user_id,
        metadata=metadata,
        fingerprint=fingerprint,
        public_key_b64=public_key_b64,
    )

    assert mock_cloudiot.return_value.get_device.call_count == 1
    assert mock_cloudiot.return_value.create_device.call_count == 0
    assert mock_cloudiot.return_value.update_device.call_count == 1


def test_create_cloudiot_device(mocker):

    serial = "1234"
    expected_name = f"serial-{serial}"
    user_id = 1
    metadata = {"meta": "data"}
    fingerprint = "fingerprint"
    public_key_b64 = "publickeyb64"

    mock_cloudiot = mocker.patch(
        "print_nanny_webapp.remote_control.utils.cloudiot_v1.DeviceManagerClient"
    )
    mocker.patch("print_nanny_webapp.remote_control.utils.MessageToDict")

    mock_cloudiot.return_value.get_device.side_effect = (
        google.api_core.exceptions.NotFound("foo")
    )
    cloudiot_device, device_path = update_or_create_cloudiot_device(
        name=expected_name,
        serial=serial,
        user_id=user_id,
        metadata=metadata,
        fingerprint=fingerprint,
        public_key_b64=public_key_b64,
    )

    assert mock_cloudiot.return_value.get_device.call_count == 1
    assert mock_cloudiot.return_value.update_device.call_count == 0
    assert mock_cloudiot.return_value.create_device.call_count == 1
