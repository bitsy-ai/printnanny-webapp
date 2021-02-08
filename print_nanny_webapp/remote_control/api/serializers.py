from django.contrib.auth import get_user_model
from rest_framework import serializers

from print_nanny_webapp.remote_control.models import (
    GcodeFile,
    PrintJob,
    PrinterProfile,
    OctoPrintDevice,
    RemoteControlCommand,
    RemoteControlSnapshot,
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


class OctoPrintDeviceKeySerializer(serializers.ModelSerializer):

    private_key = serializers.SerializerMethodField()
    configs = serializers.ListField(allow_empty=True)

    def get_private_key(self, obj):
        return getattr(obj, "private_key", None)

    class Meta:
        model = OctoPrintDevice
        fields = [field.name for field in OctoPrintDevice._meta.fields] + [
            "url",
            "private_key",
        ]
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
            "configs"
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

    configs = serializers.ListField(allow_empty=True)

    class Meta:
        model = OctoPrintDevice
        fields = [field.name for field in OctoPrintDevice._meta.fields]

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
            "configs"
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


class RemoteControlSnapshotSerializer(serializers.ModelSerializer):
    class Meta:
        model = RemoteControlSnapshot
        fields = [field.name for field in RemoteControlSnapshot._meta.fields] + ["url"]
        extra_kwargs = {
            "url": {"view_name": "api:snapshot-detail", "lookup_field": "id"}
        }


class RemoteControlSnapshotCreateResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = RemoteControlSnapshot
        fields = ["url", "id", "created_dt"]
        extra_kwargs = {
            "url": {"view_name": "api:snapshot-detail", "lookup_field": "id"}
        }


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


class PrintJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrintJob
        fields = [field.name for field in PrintJob._meta.fields] + ["url"]
        read_only_fields = ("user",)
        extra_kwargs = {
            "url": {"view_name": "api:print-job-detail", "lookup_field": "id"}
        }


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
