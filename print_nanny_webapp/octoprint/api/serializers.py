import logging
from typing import Dict, Any, Tuple
from rest_framework import serializers
from print_nanny_webapp.octoprint.models import (
    OctoPrintBackup,
    OctoPrintClientStatus,
    OctoPrintPrintJobStatus,
    OctoPrintPrinterStatus,
    OctoPrintSettings,
    GcodeFile,
    OctoPrinterProfile,
    OctoPrintServer,
    OctoPrintServerStatus,
)
from rest_polymorphic.serializers import PolymorphicSerializer


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


class OctoPrintServerSerializer(serializers.ModelSerializer):
    settings = OctoPrintSettingsSerializer(read_only=True)

    class Meta:
        model = OctoPrintServer
        exclude = ("deleted",)
        read_only_fields = ("user",)

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
        fields = "__all__"
        read_only_fields = ("user",)


class OctoPrintPrinterStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = OctoPrintPrinterStatus
        exclude = ("deleted", "polymorphic_ctype")


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
    payload = OctoPrintPrintJobPayloadSerializer()

    class Meta:
        model = OctoPrintPrintJobStatus
        exclude = ("deleted", "polymorphic_ctype")


class OctoPrintClientStatusPayloadSerializer(serializers.Serializer):
    remote_address = serializers.CharField()
    username = serializers.CharField(required=-False)


class OctoPrintClientStatusSerializer(serializers.ModelSerializer):
    payload = OctoPrintClientStatusPayloadSerializer()

    class Meta:
        model = OctoPrintClientStatus
        exclude = ("deleted", "polymorphic_ctype")


class OctoPrintServerStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = OctoPrintServerStatus
        exclude = ("deleted", "polymorphic_ctype")


class PolymorphicOctoPrintEventSerializer(PolymorphicSerializer):
    resource_type_field_name = "subject_pattern"
    model_serializer_mapping = {
        OctoPrintPrintJobStatus: OctoPrintPrintJobStatusSerializer,
        OctoPrintPrinterStatus: OctoPrintPrinterStatusSerializer,
        OctoPrintClientStatus: OctoPrintClientStatusSerializer,
        OctoPrintServerStatus: OctoPrintServerStatusSerializer,
    }

    def to_resource_type(self, model_or_instance):
        return model_or_instance.subject_pattern
