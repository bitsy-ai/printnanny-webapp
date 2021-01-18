from django.contrib.auth import get_user_model
from rest_framework import serializers

from print_nanny_webapp.remote_control.models import (
    GcodeFile,
    PrintJob,
    PrinterProfile,
    OctoPrintDevice,
    RemoteControlCommand,
)


class RemoteControlCommandSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = RemoteControlCommand
        fields = [field.name for field in RemoteControlCommand._meta.fields] + ["url"]
        extra_kwargs = {
            "url": {"view_name": "api:command-detail", "lookup_field": "id"},
        }


class OctoPrintDeviceKeySerializer(serializers.ModelSerializer):

    class Meta:
        model = OctoPrintDevice
        fields = [field.name for field in OctoPrintDevice._meta.fields] + ["url"]
        extra_kwargs = {
            "url": {"view_name": "api:octoprint-device-detail", "lookup_field": "id"},
        }

        read_only_fields = (
            "user",
            "public_key",
            "private_key",
            "fingerprint",
            "cloudiot_device_num_id",
            "cloudiot_device",
            "cloudiot_device_name",
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


class OctoPrintDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = OctoPrintDevice
        exclude = ("private_key",)
        extra_kwargs = {
            "url": {"view_name": "api:octoprint-device-detail", "lookup_field": "id"},
            "private_key": {"write_only": True},
        }

        read_only_fields = (
            "user",
            "public_key",
            "fingerprint",
            "cloudiot_device_num_id",
            "cloudiot_device",
            "cloudiot_device_name",
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
