from collections.abc import Mapping
from rest_framework import serializers
from rest_polymorphic.serializers import PolymorphicSerializer
from drf_spectacular.utils import extend_schema_field
from drf_spectacular.types import OpenApiTypes

from print_nanny_webapp.devices.models import (
    Appliance,
    CameraController,
    CloudIoTDevice,
    Device,
    AppliancePKI,
    AnsibleFacts,
    # PrinterController,
    # PrinterProfile,
    # OctoprintPrinterProfile,
)
from print_nanny_webapp.devices.services import CACerts


##
# v1 Appliance Identity Provisioning (distributed via rpi-imager)
##
class CloudIoTDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CloudIoTDevice
        fields = "__all__"


class AppliancePKISerializer(serializers.ModelSerializer):
    class Meta:
        model = AppliancePKI
        fields = "__all__"


class AnsibleFactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppliancePKI
        fields = "__all__"


class ApplianceSerializer(serializers.ModelSerializer):
    pki = AppliancePKISerializer()
    ansible_facts = AnsibleFactsSerializer()

    class Meta:
        model = Appliance
        fields = "__all__"


class CreateAppliancePKISerializer(serializers.ModelSerializer):
    class Meta:
        model = AppliancePKI
        fields = (
            "public_key",
            "public_key_checksum",
            "private_key_checksum",
            "fingerprint",
        )


class CreateAnsibleFactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnsibleFacts
        fields = (
            "os_version",
            "os",
            "kernel_version",
            "hardware",
            "revision",
            "model",
            "serial",
            "cores",
            "ram",
            "cpu_flags",
            "release_channel",
            "json",
        )


class CreateApplianceSerializer(serializers.ModelSerializer):
    pki = CreateAppliancePKISerializer()
    ansible_facts = CreateAnsibleFactsSerializer()

    class Meta:
        model = Appliance
        fields = (
            "ansible_facts",
            "hostname",
            "pki",
        )


##
# v0 Device Identity Provisioning (distributed as OctoPrint plugin)
##
class DeviceIdentitySerializer(serializers.ModelSerializer):

    ca_certs = serializers.SerializerMethodField()

    def get_ca_certs(self, obj) -> CACerts:
        return getattr(obj, "ca_certs")

    # cloudiot_device_num_id = serializers.SerializerMethodField()

    # @extend_schema_field(OpenApiTypes.INT64)
    # def get_cloudiot_device_num_id(self, obj) -> int:
    #     return obj.cloudiot_device_num_id

    private_key = serializers.SerializerMethodField()

    def get_private_key(self, obj) -> str:
        return getattr(obj, "private_key")

    private_key_checksum = serializers.SerializerMethodField()

    def get_private_key_checksum(self, obj) -> str:
        return getattr(obj, "private_key_checksum")

    public_key = serializers.SerializerMethodField()

    def get_public_key(self, obj) -> str:
        return getattr(obj, "public_key")

    public_key_checksum = serializers.SerializerMethodField()

    def get_public_key_checksum(self, obj) -> str:
        return getattr(obj, "public_key_checksum")

    # TODO add manage_url when implementing dashboard views
    # manage_url = serializers.HyperlinkedIdentityField(
    #     view_name="devices:detail", lookup_field="pk"
    # )

    class Meta:
        model = Device
        fields = [
            "ca_certs",
            "cloudiot_device_name",
            "cloudiot_device_num_id",
            "cloudiot_device_path",
            "cores",
            "cpu_flags",
            "created_dt",
            "fingerprint",
            "hardware",
            "id",
            "kernel_version",
            "model",
            "name",
            "os_version",
            "os",
            "private_key_checksum",
            "private_key",
            "public_key_checksum",
            "public_key",
            "ram",
            "revision",
            "serial",
            "updated_dt",
            "url",
            "user",
            # "manage_url",
        ]

        extra_kwargs = {
            "url": {"view_name": "api:device-detail", "lookup_field": "id"},
        }

        # TODO
        # int64 fields in read_only_fields are munged to int32 in JSON schema
        # Reproduce and report to drf-spectacular
        # read_only_fields = (
        #     "ca_certs",
        #     "user",
        #     "public_key",
        #     "public_key_checksum",
        #     "private_key",
        #     "private_key_checksum",
        #     "fingerprint",
        #     "cloudiot_device_num_id",
        #     "cloudiot_device_name",
        #     "cloudiot_device_path",
        # )


class DeviceSerializer(serializers.ModelSerializer):

    # TODO enable
    # manage_url = serializers.HyperlinkedIdentityField(
    #     view_name="devices:detail", lookup_field="pk"
    # )

    @extend_schema_field(OpenApiTypes.INT64)
    def get_cloudiot_device_num_id(self, obj) -> int:
        return obj.cloudiot_device_num_id

    class Meta:
        model = Device
        fields = [field.name for field in Device._meta.fields] + [
            "url",
        ]

        extra_kwargs = {
            "url": {"view_name": "api:device-detail", "lookup_field": "id"},
        }
        read_only_fields = (
            "user",
            "public_key",
            "fingerprint",
            "cloudiot_device_num_id",
            "cloudiot_device_name",
            "cloudiot_device_path",
        )

    def update_or_create(self, user, name, validated_data):
        return Device.objects.update_or_create(
            user=user, name=name, defaults=validated_data
        )
