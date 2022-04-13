import logging
from rest_framework import serializers
from print_nanny_webapp.octoprint.models import (
    OctoPrintBackup,
    OctoPrintSettings,
    GcodeFile,
    OctoPrinterProfile,
    OctoPrintInstall,
)

logger = logging.getLogger(__name__)


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


class OctoPrintInstallSerializer(serializers.ModelSerializer):
    settings = OctoPrintSettingsSerializer(read_only=True)

    class Meta:
        model = OctoPrintInstall
        exclude = ("deleted",)
        read_only_fields = ("user",)

    def update_or_create(self, validated_data, device_id):

        instance = OctoPrintInstall.objects.filter(device=device_id).update_or_create(
            device=device_id, defaults=validated_data
        )
        # initialize OctoPrintSettings
        if instance.settings is None:
            settings, created = OctoPrintSettings.objects.get_or_create(
                octoprint_install=instance
            )
            if created:
                logger.info("Created default %s for %s", settings, instance)
                instance.refresh_from_db()
        return instance


class OctoPrintBackupSerializer(serializers.ModelSerializer):
    class Meta:
        model = OctoPrintBackup
        fields = "__all__"
        read_only_fields = ("user",)
