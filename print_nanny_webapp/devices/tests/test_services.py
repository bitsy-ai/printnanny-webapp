import hashlib
import pytest
import tempfile
from django.conf import settings
from django.test import TestCase
import google.api_core.exceptions

from google.cloud import iot_v1 as cloudiot_v1
from print_nanny_webapp.devices.models import Appliance

from print_nanny_webapp.devices.services import (
    generate_keypair_and_update_or_create_cloudiot_device,
    generate_keypair,
)

from django.contrib.auth import get_user_model

User = get_user_model()

TEST_EMAIL = "testing@print-nanny.com"
TEST_HOSTNAME = "testing.local"


class MockDevice(object):
    num_id = 1
    id = "1"
    name = "1"


@pytest.mark.django_db
def test_create_cloudiot_device(mocker, user):

    appliance = Appliance.objects.create(user=user, hostname=TEST_HOSTNAME)
    mock_cloudiot_client = mocker.patch(
        "print_nanny_webapp.devices.services.cloudiot_v1.DeviceManagerClient"
    )
    mock_cloudiot_client.return_value.create_device.return_value = MockDevice()

    mock_cloudiot_client.return_value.get_device.side_effect = (
        google.api_core.exceptions.NotFound("Fake Exception")
    )

    keypair, cloudiot_device = generate_keypair_and_update_or_create_cloudiot_device(
        appliance
    )

    assert mock_cloudiot_client.return_value.get_device.call_count == 1
    assert mock_cloudiot_client.return_value.update_device.call_count == 0
    assert mock_cloudiot_client.return_value.create_device.call_count == 1
    assert cloudiot_device.appliance == appliance


@pytest.mark.django_db
def test_update_cloudiot_device(mocker, user):

    appliance = Appliance.objects.create(user=user, hostname=TEST_HOSTNAME)
    mock_cloudiot_client = mocker.patch(
        "print_nanny_webapp.devices.services.cloudiot_v1.DeviceManagerClient"
    )
    mock_cloudiot_device_update_request = mocker.patch(
        "print_nanny_webapp.devices.services.cloudiot_v1.types.UpdateDeviceRequest"
    )
    mock_cloudiot_client.return_value.update_device.return_value = MockDevice()

    keypair, cloudiot_device = generate_keypair_and_update_or_create_cloudiot_device(
        appliance
    )

    assert mock_cloudiot_client.return_value.get_device.call_count == 1
    assert mock_cloudiot_client.return_value.update_device.call_count == 1
    assert mock_cloudiot_client.return_value.create_device.call_count == 0
    assert cloudiot_device.appliance == appliance


def test_generate_keypair():
    keypair = generate_keypair()

    public_key_checksum = hashlib.sha256(
        keypair["public_key"].encode("utf8")
    ).hexdigest()
    assert public_key_checksum == keypair["public_key_checksum"]

    private_key_checksum = hashlib.sha256(
        keypair["private_key"].encode("utf8")
    ).hexdigest()
    assert private_key_checksum == keypair["private_key_checksum"]
