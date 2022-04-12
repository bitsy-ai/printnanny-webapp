from rest_framework import serializers
from print_nanny_webapp.octoprint.models import (
    OctoPrintBackup,
    OctoPrintSettings,
    GcodeFile,
    OctoPrinterProfile,
    OctoPrintInstall,
)


class OctoPrintInstallSerializer(serializers.ModelSerializer):
    class Meta:
        model = OctoPrintInstall
        exclude = ("deleted",)
        read_only_fields = ("user",)

    def update_or_create(self, validated_data, device_id):
        return OctoPrintInstall.objects.filter(device=device_id).update_or_create(
            device=device_id, defaults=validated_data
        )


class OctoPrinterProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = OctoPrinterProfile
        exclude = ("deleted",)
        read_only_fields = ("user",)

    def update_or_create(self, validated_data, user):
        return OctoPrintSettings.objects.filter(user=user).update_or_create(
            defaults=validated_data
        )


class GcodeFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = GcodeFile
        exclude = ("deleted",)
        read_only_fields = ("user",)


class OctoPrintSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OctoPrintSettings
        exclude = ("deleted",)
        read_only_fields = ("user",)

    def update_or_create(self, validated_data, user):
        return OctoPrintSettings.objects.filter(user=user).update_or_create(
            defaults=validated_data
        )


class OctoPrintBackupSerializer(serializers.ModelSerializer):
    class Meta:
        model = OctoPrintBackup
        fields = "__all__"
        read_only_fields = ("user",)
