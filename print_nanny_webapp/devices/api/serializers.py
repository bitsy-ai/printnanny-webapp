from collections.abc import Mapping
from rest_framework import serializers
from rest_polymorphic.serializers import PolymorphicSerializer
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

    cloudiot_device_configs = serializers.SerializerMethodField()

    def get_cloudiot_device_configs(self, obj) -> str:
        return obj.cloudiot_device_configs

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

    manage_url = serializers.HyperlinkedIdentityField(
        view_name="dashboard:devices:detail", lookup_field="pk"
    )

    class Meta:
        model = Device
        fields = [field.name for field in Device._meta.fields] + [
            "url",
            "private_key",
            "private_key_checksum",
            "public_key",
            "public_key_checksum",
            "cloudiot_device_configs",
            "ca_certs",
            "manage_url",
        ]
        extra_kwargs = {
            "url": {"view_name": "api:device-detail", "lookup_field": "id"},
        }

        read_only_fields = (
            "ca_certs",
            "user",
            "public_key",
            "public_key_checksum",
            "private_key",
            "private_key_checksum",
            "fingerprint",
            "cloudiot_device_num_id",
            "cloudiot_device",
            "cloudiot_device_name",
            "cloudiot_device_path",
            "cloudiot_device_configs",
        )


class DeviceSerializer(serializers.ModelSerializer):

    # TODO enable
    # manage_url = serializers.HyperlinkedIdentityField(
    #     view_name="devices:detail", lookup_field="pk"
    # )
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
            "cloudiot_device",
            "cloudiot_device_name",
            "cloudiot_device_path",
            "cloudiot_device_configs",
        )

    def update_or_create(self, user, serial, validated_data):
        return Device.objects.update_or_create(
            user=user, serial=serial, defaults=validated_data
        )


class PrinterControllerSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrinterController
        fields = "__all__"
        read_only_fields = ("user", "polymorphic_ctype")


class OctoprintControllerSerializer(serializers.ModelSerializer):
    class Meta:
        model = OctoprintController
        fields = "__all__"
        read_only_fields = ("user", "polymorphic_ctype")


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
        fields = "__all__"
        read_only_fields = ("user", "polymorphic_ctype")


class OctoprintPrinterProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = OctoprintPrinterProfile
        fields = "__all__"
        read_only_fields = ("user", "polymorphic_ctype")


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
