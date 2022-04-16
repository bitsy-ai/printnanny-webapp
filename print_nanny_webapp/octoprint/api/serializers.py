import logging
from typing import Dict, Any, Tuple
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

    def update_or_create(
        self, validated_data: Dict[Any, Any], device_id: int, user_id: int
    ) -> Tuple[OctoPrintInstall, bool]:

        instance, created = OctoPrintInstall.objects.filter(
            device=device_id, user=user_id
        ).update_or_create(device=device_id, user=user_id, defaults=validated_data)
        logger.info("Saved %s created=%s", instance, created)

        if created:
            settings = OctoPrintSettings.objects.create(octoprint_install=instance)
            logger.info("Created default %s for %s", settings, instance)
            instance.refresh_from_db()
        return instance, created


class OctoPrintBackupSerializer(serializers.ModelSerializer):
    class Meta:
        model = OctoPrintBackup
        fields = "__all__"
        read_only_fields = ("user",)
