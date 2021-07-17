import hashlib
import pytest
import tempfile
from django.conf import settings
import google.api_core.exceptions

from print_nanny_webapp.devices.services import (
    update_or_create_cloudiot_device,
    generate_keypair,
)


def test_generate_keypair():
    keypair = generate_keypair()

    public_key_checksum = hashlib.sha256(
        keypair["public_key_content"].encode("utf8")
    ).hexdigest()
    assert public_key_checksum == keypair["public_key_checksum"]

    private_key_checksum = hashlib.sha256(
        keypair["private_key_content"].encode("utf8")
    ).hexdigest()
    assert private_key_checksum == keypair["private_key_checksum"]

    primary_ca_checksum = hashlib.sha256(
        keypair["ca_certs"]["primary"].encode("utf8")
    ).hexdigest()
    assert primary_ca_checksum == keypair["ca_certs"]["primary_checksum"]

    backup_ca_checksum = hashlib.sha256(
        keypair["ca_certs"]["backup"].encode("utf8")
    ).hexdigest()
    assert backup_ca_checksum == keypair["ca_certs"]["backup_checksum"]


def test_update_cloudiot_device(mocker):

    serial = "1234"
    expected_name = f"serial-{serial}"
    user_id = 1
    metadata = {"meta": "data"}
    fingerprint = "fingerprint"
    public_key_content = "publickeyb64"

    mock_cloudiot = mocker.patch(
        "print_nanny_webapp.devices.services.cloudiot_v1.DeviceManagerClient"
    )
    _ = mocker.patch(
        "print_nanny_webapp.devices.services.cloudiot_v1.types.UpdateDeviceRequest"
    )
    mocker.patch("print_nanny_webapp.devices.services.MessageToDict")
    cloudiot_device, device_path = update_or_create_cloudiot_device(
        name=expected_name,
        serial=serial,
        user_id=user_id,
        metadata=metadata,
        fingerprint=fingerprint,
        public_key_content=public_key_content,
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
    public_key_content = "publickeyb64"

    mock_cloudiot = mocker.patch(
        "print_nanny_webapp.devices.services.cloudiot_v1.DeviceManagerClient"
    )
    mocker.patch("print_nanny_webapp.devices.services.MessageToDict")

    mock_cloudiot.return_value.get_device.side_effect = (
        google.api_core.exceptions.NotFound("foo")
    )
    cloudiot_device, device_path = update_or_create_cloudiot_device(
        name=expected_name,
        serial=serial,
        user_id=user_id,
        metadata=metadata,
        fingerprint=fingerprint,
        public_key_content=public_key_content,
    )

    assert mock_cloudiot.return_value.get_device.call_count == 1
    assert mock_cloudiot.return_value.update_device.call_count == 0
    assert mock_cloudiot.return_value.create_device.call_count == 1
