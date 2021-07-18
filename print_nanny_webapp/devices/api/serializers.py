from collections.abc import Mapping
from rest_framework import serializers
from rest_polymorphic.serializers import PolymorphicSerializer
from drf_spectacular.utils import extend_schema_field
from drf_spectacular.types import OpenApiTypes

from print_nanny_webapp.devices.models import (
    Device,
    PrinterController,
    OctoprintController,
    PrinterProfile,
    OctoprintPrinterProfile,
)
from print_nanny_webapp.devices.services import CACerts


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


class PrinterControllerSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrinterController
        read_only_fields = ("user", "polymorphic_ctype")
        exclude = ("deleted",)


class OctoprintControllerSerializer(serializers.ModelSerializer):
    class Meta:
        model = OctoprintController
        read_only_fields = ("user", "polymorphic_ctype")
        exclude = ("deleted",)


class PrinterControllerPolymorphicSerializer(PolymorphicSerializer):
    model_serializer_mapping = {
        PrinterController: PrinterControllerSerializer,
        OctoprintController: OctoprintControllerSerializer,
    }

    def to_representation(self, instance):
        if isinstance(instance, Mapping):
            resource_type = self._get_resource_type_from_mapping(instance)
            serializer = self._get_serializer_from_resource_type(resource_type)
        else:
            resource_type = self.to_resource_type(instance)
            serializer = self._get_serializer_from_model_or_instance(instance)

        ret = serializer.to_representation(instance)
        return ret


class PrinterProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrinterProfile
        read_only_fields = ("user", "polymorphic_ctype")
        exclude = ("deleted",)


class OctoprintPrinterProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = OctoprintPrinterProfile
        read_only_fields = ("user", "polymorphic_ctype")
        exclude = ("deleted",)


class PrinterProfilePolymorphicSerializer(PolymorphicSerializer):
    model_serializer_mapping = {
        PrinterProfile: PrinterProfileSerializer,
        OctoprintPrinterProfile: OctoprintPrinterProfileSerializer,
    }

    def to_representation(self, instance):
        if isinstance(instance, Mapping):
            resource_type = self._get_resource_type_from_mapping(instance)
            serializer = self._get_serializer_from_resource_type(resource_type)
        else:
            resource_type = self.to_resource_type(instance)
            serializer = self._get_serializer_from_model_or_instance(instance)

        ret = serializer.to_representation(instance)
        return ret
