import logging
from django.apps import apps
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_polymorphic.serializers import PolymorphicSerializer
from print_nanny_webapp.events.models.pi import (
    PiBootEvent,
    PiGstreamerEvent,
    PiSoftwareUpdateEvent,
)
from print_nanny_webapp.events.models.alerts import EmailAlertSettings

from print_nanny_webapp.events.models import PiBootEvent
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


# class PiBootEventSerializer(serializers.Serializer):
#     resourcetype = serializers.ChoiceField(choices=["PiGstreamerEvent", "PiSoftwareUpdateEvent"])
#     class Meta:
#         abstract = True


class PiBootEventSerializer(serializers.ModelSerializer):
    model = serializers.ChoiceField(choices=[PiEventModel.PiBootEvent])

    class Meta:
        model = PiBootEvent
        exclude = ("deleted",)
        read_only_fields = ("created_dt",)


class PiSoftwareUpdateEventSerializer(serializers.ModelSerializer):
    model = serializers.ChoiceField(choices=[PiEventModel.PiSoftwareUpdateEvent])

    class Meta:
        model = PiSoftwareUpdateEvent
        exclude = ("deleted",)
        read_only_fields = ("created_dt",)


class PiGstreamerEventSerializer(serializers.ModelSerializer):
    model = serializers.ChoiceField(choices=[PiEventModel.PiGstreamerEvent])

    class Meta:
        model = PiGstreamerEvent
        exclude = ("deleted",)
        read_only_fields = ("created_dt",)


class PolymorphicPiEventSerializer(PolymorphicSerializer):
    resource_type_field_name = "model"

    model_serializer_mapping = {
        PiGstreamerEvent: PiGstreamerEventSerializer,
        PiSoftwareUpdateEvent: PiSoftwareUpdateEventSerializer,
        PiBootEvent: PiBootEventSerializer,
    }
