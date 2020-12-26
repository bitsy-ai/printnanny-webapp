from django.contrib.auth import get_user_model
from rest_framework import serializers

from print_nanny_webapp.remote_control.models import (
    GcodeFile,
    PrintJob,
    PrinterProfile,
)


class GcodeFileSerializer(serializers.ModelSerializer):
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
