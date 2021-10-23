import hashlib
import pytest
import tempfile
from django.conf import settings
from django.test import TestCase
import google.api_core.exceptions

from google.cloud import iot_v1 as cloudiot_v1
from print_nanny_webapp.devices.models import Appliance

from print_nanny_webapp.devices.services import (
    update_or_create_cloudiot_device,
    generate_keypair,
)

from django.contrib.auth import get_user_model

User = get_user_model()

TEST_EMAIL = "testing@print-nanny.com"
TEST_HOSTNAME = "testing.local"


# @pytest.mark.django_db
# @pytest.mark.fixture
# def user():
#     return User.objects.create(email=TEST_EMAIL)


# @pytest.mark.django_db
# @pytest.mark.fixture
# def appliance(user):
#     return Appliance.objects.create(user=user, hostname=TEST_HOSTNAME)


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

    keypair = generate_keypair()
    cloudiot_device = update_or_create_cloudiot_device(
        appliance=appliance, keypair=keypair
    )

    assert mock_cloudiot_client.return_value.get_device.call_count == 1
    assert mock_cloudiot_client.return_value.update_device.call_count == 0
    assert mock_cloudiot_client.return_value.create_device.call_count == 1


# def DeviceServices(TestCase):
#     def setUp(self):
#         self.hostname = "testing.local"
#         self.user = User.objects.create(
#             email=self.email
#         )
#         self.appliance = Appliance.objects.create(
#             user=self.user,
#             hostname=self.hostname
#         )
#         return super().setUp()


# def test_generate_keypair():
#     keypair = generate_keypair()

#     public_key_checksum = hashlib.sha256(
#         keypair["public_key_content"].encode("utf8")
#     ).hexdigest()
#     assert public_key_checksum == keypair["public_key_checksum"]

#     private_key_checksum = hashlib.sha256(
#         keypair["private_key_content"].encode("utf8")
#     ).hexdigest()
#     assert private_key_checksum == keypair["private_key_checksum"]

#     primary_ca_checksum = hashlib.sha256(
#         keypair["ca_certs"]["primary"].encode("utf8")
#     ).hexdigest()
#     assert primary_ca_checksum == keypair["ca_certs"]["primary_checksum"]

#     backup_ca_checksum = hashlib.sha256(
#         keypair["ca_certs"]["backup"].encode("utf8")
#     ).hexdigest()
#     assert backup_ca_checksum == keypair["ca_certs"]["backup_checksum"]


# @pytest.mark.django_db
# def test_update_cloudiot_device(mocker):

#     appliance = Appliance.objects.create(

#     )
#     serial = "1234"
#     expected_name = f"serial-{serial}"
#     user_id = 1
#     metadata = {"meta": "data"}
#     fingerprint = "fingerprint"
#     public_key_content = "publickeyb64"

#     mock_cloudiot = mocker.patch(
#         "print_nanny_webapp.devices.services.cloudiot_v1.DeviceManagerClient"
#     )
#     _ = mocker.patch(
#         "print_nanny_webapp.devices.services.cloudiot_v1.types.UpdateDeviceRequest"
#     )
#     mocker.patch("print_nanny_webapp.devices.services.MessageToDict")
#     cloudiot_device, device_path = update_or_create_cloudiot_device(
#         name=expected_name,
#         serial=serial,
#         user_id=user_id,
#         metadata=metadata,
#         fingerprint=fingerprint,
#         public_key_content=public_key_content,
#     )

#     assert mock_cloudiot.return_value.get_device.call_count == 1
#     assert mock_cloudiot.return_value.create_device.call_count == 0
#     assert mock_cloudiot.return_value.update_device.call_count == 1


# def test_create_cloudiot_device(mocker):

#     serial = "1234"
#     expected_name = f"serial-{serial}"
#     user_id = 1
#     metadata = {"meta": "data"}
#     fingerprint = "fingerprint"
#     public_key_content = "publickeyb64"

#     mock_cloudiot = mocker.patch(
#         "print_nanny_webapp.devices.services.cloudiot_v1.DeviceManagerClient"
#     )
#     mocker.patch("print_nanny_webapp.devices.services.MessageToDict")

#     mock_cloudiot.return_value.get_device.side_effect = (
#         google.api_core.exceptions.NotFound("foo")
#     )
#     cloudiot_device, device_path = update_or_create_cloudiot_device(
#         name=expected_name,
#         serial=serial,
#         user_id=user_id,
#         metadata=metadata,
#         fingerprint=fingerprint,
#         public_key_content=public_key_content,
#     )

#     assert mock_cloudiot.return_value.get_device.call_count == 1
#     assert mock_cloudiot.return_value.update_device.call_count == 0
#     assert mock_cloudiot.return_value.create_device.call_count == 1
