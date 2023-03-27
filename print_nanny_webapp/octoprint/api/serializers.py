import logging
from typing import Dict, Any, Tuple
from rest_framework import serializers

from rest_polymorphic.serializers import PolymorphicSerializer

from print_nanny_webapp.octoprint.models import (
    OctoPrintBackup,
    OctoPrintPrintJobStatus,
    OctoPrintPrinterStatus,
    OctoPrintSettings,
    GcodeFile,
    OctoPrinterProfile,
    OctoPrintServer,
    OctoPrintServerStatus,
    OctoPrintGcodeEvent,
)
from print_nanny_webapp.octoprint.enum import OctoprintEventSubjectPattern


logger = logging.getLogger(__name__)


class OctoPrinterProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = OctoPrinterProfile
        exclude = ("deleted", "deleted_by_cascade")
        read_only_fields = ("user",)

    def update_or_create(self, validated_data, user):
        return OctoPrintSettings.objects.filter(user=user).update_or_create(
            defaults=validated_data
        )


class GcodeFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = GcodeFile
        exclude = ("deleted", "deleted_by_cascade")
        read_only_fields = ("user",)


class OctoPrintSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OctoPrintSettings
        exclude = ("deleted", "deleted_by_cascade")
        read_only_fields = ("user",)

    def update_or_create(self, validated_data, user):
        return OctoPrintSettings.objects.filter(user=user).update_or_create(
            defaults=validated_data
        )


class OctoPrintServerSerializer(serializers.ModelSerializer):
    settings = OctoPrintSettingsSerializer(read_only=True)
    base_url = serializers.CharField()
    base_path = serializers.CharField()
    venv_path = serializers.CharField()
    pip_path = serializers.CharField()
    python_path = serializers.CharField()

    class Meta:
        model = OctoPrintServer
        exclude = ("deleted", "deleted_by_cascade")
        read_only_fields = ("user", "base_path", "base_url")

    def update_or_create(
        self, validated_data: Dict[Any, Any], device_id: int, user_id: int
    ) -> Tuple[OctoPrintServer, bool]:

        instance, created = OctoPrintServer.objects.filter(
            device=device_id, user=user_id
        ).update_or_create(device=device_id, user=user_id, defaults=validated_data)
        logger.info("Saved %s created=%s", instance, created)

        if created:
            settings = OctoPrintSettings.objects.create(octoprint_server=instance)
            logger.info("Created default %s for %s", settings, instance)
            instance.refresh_from_db()
        return instance, created


class OctoPrintBackupSerializer(serializers.ModelSerializer):
    class Meta:
        model = OctoPrintBackup
        read_only_fields = ("user",)
        exclude = ("deleted", "deleted_by_cascade")


class OctoPrintPrinterStatusSerializer(serializers.ModelSerializer):
    subject_pattern = serializers.ChoiceField(
        choices=[OctoprintEventSubjectPattern.OctoPrintPrinterStatus]
    )

    class Meta:
        model = OctoPrintPrinterStatus
        exclude = ("deleted", "deleted_by_cascade", "polymorphic_ctype")


class OctoPrintPrintJobPayloadSerializer(serializers.Serializer):
    """
    Serialize OctoPrint print job status events:
    https://docs.octoprint.org/en/master/events/index.html?highlight=events#printing
    """

    name = serializers.CharField()
    path = serializers.CharField()
    origin = serializers.CharField()
    size = serializers.IntegerField(required=False)
    time = serializers.FloatField(required=False)
    position = serializers.DictField()


class OctoPrintPrintJobStatusSerializer(serializers.ModelSerializer):
    subject_pattern = serializers.ChoiceField(
        choices=[OctoprintEventSubjectPattern.OctoPrintPrintJobStatus]
    )

    payload = OctoPrintPrintJobPayloadSerializer()

    class Meta:
        model = OctoPrintPrintJobStatus
        exclude = ("deleted", "deleted_by_cascade", "polymorphic_ctype")


class OctoPrintServerStatusSerializer(serializers.ModelSerializer):
    subject_pattern = serializers.ChoiceField(
        choices=[OctoprintEventSubjectPattern.OctoPrintServerStatus]
    )

    class Meta:
        model = OctoPrintServerStatus
        exclude = ("deleted", "deleted_by_cascade", "polymorphic_ctype")


class OctoPrintGcodeEventSerializer(serializers.ModelSerializer):
    subject_pattern = serializers.ChoiceField(
        choices=[OctoprintEventSubjectPattern.OctoPrintGcodeEvent]
    )

    class Meta:
        model = OctoPrintGcodeEvent
        exclude = ("deleted", "deleted_by_cascade", "polymorphic_ctype")


class PolymorphicOctoPrintEventSerializer(PolymorphicSerializer):
    resource_type_field_name = "subject_pattern"
    model_serializer_mapping = {
        OctoPrintPrintJobStatus: OctoPrintPrintJobStatusSerializer,
        OctoPrintPrinterStatus: OctoPrintPrinterStatusSerializer,
        OctoPrintServerStatus: OctoPrintServerStatusSerializer,
        OctoPrintGcodeEvent: OctoPrintGcodeEventSerializer,
    }

    def to_resource_type(self, model_or_instance):
        return model_or_instance.subject_pattern
