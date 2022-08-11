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

from print_nanny_webapp.events.models.enum import PiEventSubjectPattern

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
    subject_pattern = serializers.ChoiceField(
        choices=[PiEventSubjectPattern.PiBootCommand]
    )

    class Meta:
        model = PiBootCommand
        exclude = ("deleted", "polymorphic_ctype")


class PiBootStatusSerializer(serializers.ModelSerializer):
    subject_pattern = serializers.ChoiceField(
        choices=[PiEventSubjectPattern.PiBootStatus]
    )

    class Meta:
        model = PiBootStatus
        exclude = ("deleted", "polymorphic_ctype")


class PiSoftwareUpdatePayloadSerializer(serializers.Serializer):
    wic_tarball_url = serializers.CharField()
    wic_bmap_url = serializers.CharField()
    manifest_url = serializers.CharField()
    swu_url = serializers.CharField()
    version_id = serializers.CharField()
    version = serializers.CharField()
    version_codename = serializers.CharField()


class PiSoftwareUpdateCommandSerializer(serializers.ModelSerializer):

    payload = PiSoftwareUpdatePayloadSerializer()
    subject_pattern = serializers.ChoiceField(
        choices=[PiEventSubjectPattern.PiSoftwareUpdateCommand]
    )

    class Meta:
        model = PiSoftwareUpdateCommand
        exclude = ("deleted", "polymorphic_ctype")


class PiSoftwareUpdateStatusSerializer(serializers.ModelSerializer):
    subject_pattern = serializers.ChoiceField(
        choices=[PiEventSubjectPattern.PiSoftwareUpdateStatus]
    )

    class Meta:
        model = PiSoftwareUpdateStatus
        exclude = ("deleted", "polymorphic_ctype")


class PiCamCommandSerializer(serializers.ModelSerializer):
    subject_pattern = serializers.ChoiceField(
        choices=[PiEventSubjectPattern.PiCamCommand]
    )

    class Meta:
        model = PiCamCommand
        exclude = ("deleted", "polymorphic_ctype")


class PiCamStatusSerializer(serializers.ModelSerializer):
    subject_pattern = serializers.ChoiceField(
        choices=[PiEventSubjectPattern.PiCamStatus]
    )

    class Meta:
        model = PiCamStatus
        exclude = ("deleted", "polymorphic_ctype")


class PolymorphicPiStatusSerializer(PolymorphicSerializer):
    resource_type_field_name = "subject_pattern"

    model_serializer_mapping = {
        PiCamStatus: PiCamStatusSerializer,
        PiSoftwareUpdateStatus: PiSoftwareUpdateStatusSerializer,
        PiBootStatus: PiBootStatusSerializer,
    }


class PolymorphicPiCommandSerializer(PolymorphicSerializer):
    resource_type_field_name = "subject_pattern"

    model_serializer_mapping = {
        PiCamCommand: PiCamCommandSerializer,
        PiSoftwareUpdateCommand: PiSoftwareUpdateCommandSerializer,
        PiBootCommand: PiBootCommandSerializer,
    }


class PolymorphicPiEventSerializer(PolymorphicSerializer):
    resource_type_field_name = "subject_pattern"
    model_serializer_mapping = {
        PiCamStatus: PiCamStatusSerializer,
        PiSoftwareUpdateStatus: PiSoftwareUpdateStatusSerializer,
        PiBootStatus: PiBootStatusSerializer,
        PiCamCommand: PiCamCommandSerializer,
        PiSoftwareUpdateCommand: PiSoftwareUpdateCommandSerializer,
        PiBootCommand: PiBootCommandSerializer,
    }

    def to_resource_type(self, model_or_instance):
        return model_or_instance.subject_pattern
