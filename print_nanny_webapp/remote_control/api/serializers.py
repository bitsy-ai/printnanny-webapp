from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import serializers

from print_nanny_webapp.remote_control.models import (
    GcodeFile,
    PrintSession,
    PrinterProfile,
    OctoPrintDevice,
    RemoteControlCommand,
)


class RemoteControlCommandSerializer(serializers.ModelSerializer):
    class Meta:
        model = RemoteControlCommand
        fields = [field.name for field in RemoteControlCommand._meta.fields] + [
            "url",
            "octoprint_event_type",
        ]
        extra_kwargs = {
            "url": {"view_name": "api:command-detail", "lookup_field": "id"},
        }


class PrintSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrintSession
        fields = [field.name for field in PrintSession._meta.fields] + [
            "url",
            "datesegment",
            "created_dt",
        ]
        read_only_fields = ("user",)
        extra_kwargs = {
            "url": {"view_name": "api:print-session-detail", "lookup_field": "session"}
        }
        lookup_field = ("session", "id")


class OctoPrintDeviceKeySerializer(serializers.ModelSerializer):

    active_session = PrintSessionSerializer(required=False)

    cloudiot_device_configs = serializers.SerializerMethodField()

    def get_cloudiot_device_configs(self, obj):
        return obj.cloudiot_device_configs

    private_key = serializers.SerializerMethodField()

    def get_private_key(self, obj):
        return getattr(obj, "private_key", None)

    private_key_checksum = serializers.SerializerMethodField()

    def get_private_key_checksum(self, obj):
        return getattr(obj, "private_key_checksum", None)

    public_key_checksum = serializers.CharField()

    # def get_public_key_checksum(self, obj):
    #     return getattr(obj, "public_key_checksum", None)

    ca_certs = serializers.DictField(child=serializers.CharField())

    # def get_ca_certs(self, obj):
    #     return getattr(obj, "ca_certs", None)

    manage_url = serializers.HyperlinkedIdentityField(
        view_name="dashboard:octoprint-devices:detail", lookup_field="pk"
    )

    class Meta:
        model = OctoPrintDevice
        fields = (
            "active_session" "ca_certs",
            "cloudiot_device_name",
            "cloudiot_device_num_id",
            "cloudiot_device_path",
            "cloudiot_device",
            "cores",
            "cpu_flags",
            "created_dt",
            "hardware",
            "manage_url",
            "model",
            "monitoring_active",
            "name",
            "octoprint_version",
            "pip_version",
            "platform",
            "plugin_version",
            "print_nanny_client_version",
            "private_key_checksum",
            "private_key",
            "public_key_checksum",
            "public_key",
            "python_version",
            "ram",
            "revision",
            "serial",
            "user",
        )

        extra_kwargs = {
            "url": {"view_name": "api:octoprint-device-detail", "lookup_field": "id"},
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
            "active_session",
            "monitoring_active",
        )

    def update_or_create(self, user, serial, validated_data):
        unique_together = ("user", "serial")
        defaults = {k: v for k, v in validated_data.items() if k not in unique_together}
        unique_together_fields = {
            k: v for k, v in validated_data.items() if k in unique_together
        }
        return OctoPrintDevice.objects.update_or_create(
            user=user, serial=serial, defaults=validated_data
        )


class OctoPrintDeviceSerializer(serializers.ModelSerializer):

    active_session = PrintSessionSerializer(required=False)

    cloudiot_device_configs = serializers.SerializerMethodField()

    def get_cloudiot_device_configs(self, obj):
        return obj.cloudiot_device_configs

    manage_url = serializers.HyperlinkedIdentityField(
        view_name="dashboard:octoprint-devices:detail", lookup_field="pk"
    )

    class Meta:
        model = OctoPrintDevice
        fields = [field.name for field in OctoPrintDevice._meta.fields] + [
            "cloudiot_device_configs",
            "manage_url",
            "monitoring_active",
            "active_session",
        ]

        extra_kwargs = {
            "url": {"view_name": "api:octoprint-devices-detail", "lookup_field": "id"},
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
            "monitoring_active",
            "active_session",
        )

    def update_or_create(self, user, serial, validated_data):
        unique_together = ("user", "serial")
        defaults = {k: v for k, v in validated_data.items() if k not in unique_together}
        unique_together_fields = {
            k: v for k, v in validated_data.items() if k in unique_together
        }
        # return OctoPrintDevice.objects.filter(
        #     **unique_together_fields, user=user
        # ).update_or_create(**unique_together_fields, user=user, defaults=defaults)
        return OctoPrintDevice.objects.update_or_create(
            user=user, serial=serial, defaults=validated_data
        )


class GcodeFileSerializer(serializers.ModelSerializer):

    # https://github.com/aio-libs/aiohttp/issues/3652
    # octoprint_device is accepted as a string and deserialized to an integer
    octoprint_device = serializers.CharField()

    class Meta:
        model = GcodeFile
        read_only_fields = ("user",)
        fields = [field.name for field in GcodeFile._meta.fields] + ["url"]
        extra_kwargs = {
            "url": {"view_name": "api:gcode-file-detail", "lookup_field": "id"}
        }

    def update_or_create(self, validated_data, user):
        unique_together = ("user", "file_hash")
        defaults = {k: v for k, v in validated_data.items() if k not in unique_together}
        unique_together_fields = {
            k: v for k, v in validated_data.items() if k in unique_together
        }
        return GcodeFile.objects.filter(
            **unique_together_fields, user=user
        ).update_or_create(**unique_together_fields, user=user, defaults=defaults)


class PrinterProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrinterProfile
        fields = [field.name for field in PrinterProfile._meta.fields] + ["url"]
        read_only_fields = ("user",)

        extra_kwargs = {
            "url": {"view_name": "api:printer-profile-detail", "lookup_field": "id"}
        }

    def update_or_create(self, validated_data, user):
        unique_together = (
            "user",
            "name",
        )
        defaults = {k: v for k, v in validated_data.items() if k not in unique_together}
        unique_together_fields = {
            k: v for k, v in validated_data.items() if k in unique_together
        }
        return PrinterProfile.objects.filter(
            **unique_together_fields, user=user
        ).update_or_create(**unique_together_fields, user=user, defaults=defaults)
