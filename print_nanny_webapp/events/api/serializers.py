import logging
from django.apps import apps
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_polymorphic.serializers import PolymorphicSerializer
from print_nanny_webapp.events.models.pi import (
    PiBootCommand,
    PiBootStatus,
    PiSoftwareUpdateCommand,
    PiSoftwareUpdateStatus,
    PiCamCommand,
    PiCamStatus,
    PiSoftwareUpdateStatus,
)
from print_nanny_webapp.events.models.alerts import EmailAlertSettings

from print_nanny_webapp.events.models.enum import PiEventModel

logger = logging.getLogger(__name__)

Pi = apps.get_model("devices", "Pi")
User = get_user_model()


class EmailAlertSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailAlertSettings
        fields = "__all__"
        read_only_fields = (
            "created_dt",
            "updated_dt",
            "user",
        )


class PiBootCommandSerializer(serializers.ModelSerializer):
    model = serializers.ChoiceField(choices=[PiEventModel.PiBootCommand])

    class Meta:
        model = PiBootCommand
        exclude = ("deleted",)
        read_only_fields = ("created_dt",)


class PiBootStatusSerializer(serializers.ModelSerializer):
    model = serializers.ChoiceField(choices=[PiEventModel.PiBootStatus])

    class Meta:
        model = PiBootStatus
        exclude = ("deleted",)
        read_only_fields = ("created_dt",)


class PiSoftwareUpdateCommandSerializer(serializers.ModelSerializer):
    model = serializers.ChoiceField(choices=[PiEventModel.PiSoftwareUpdateCommand])

    class Meta:
        model = PiSoftwareUpdateCommand
        exclude = ("deleted",)
        read_only_fields = ("created_dt",)


class PiSoftwareUpdateStatusSerializer(serializers.ModelSerializer):
    model = serializers.ChoiceField(choices=[PiEventModel.PiSoftwareUpdateStatus])

    class Meta:
        model = PiSoftwareUpdateStatus
        exclude = ("deleted",)
        read_only_fields = ("created_dt",)


class PiCamCommandSerializer(serializers.ModelSerializer):
    model = serializers.ChoiceField(choices=[PiEventModel.PiCamCommand])

    class Meta:
        model = PiCamCommand
        exclude = ("deleted",)
        read_only_fields = ("created_dt",)


class PiCamStatusSerializer(serializers.ModelSerializer):
    model = serializers.ChoiceField(choices=[PiEventModel.PiCamStatus])

    class Meta:
        model = PiCamStatus
        exclude = ("deleted",)
        read_only_fields = ("created_dt",)


class PolymorphicPiStatusSerializer(PolymorphicSerializer):
    resource_type_field_name = "model"

    model_serializer_mapping = {
        PiCamStatus: PiCamStatusSerializer,
        PiSoftwareUpdateStatus: PiSoftwareUpdateStatusSerializer,
        PiBootStatus: PiBootStatusSerializer,
    }


class PolymorphicPiCommandSerializer(PolymorphicSerializer):
    resource_type_field_name = "model"

    model_serializer_mapping = {
        PiCamCommand: PiCamCommandSerializer,
        PiSoftwareUpdateCommand: PiSoftwareUpdateCommandSerializer,
        PiBootCommand: PiBootCommandSerializer,
    }


class PolymorphicPiEventSerializer(PolymorphicSerializer):
    model_serializer_mapping = {
        PiCamStatus: PiCamStatusSerializer,
        PiSoftwareUpdateStatus: PiSoftwareUpdateStatusSerializer,
        PiBootStatus: PiBootStatusSerializer,
        PiCamCommand: PiCamCommandSerializer,
        PiSoftwareUpdateCommand: PiSoftwareUpdateCommandSerializer,
        PiBootCommand: PiBootCommandSerializer,
    }
