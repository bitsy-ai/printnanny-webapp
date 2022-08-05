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

from ..models import PiBootEvent

logger = logging.getLogger(__name__)

Pi = apps.get_model("devices", "Pi")
User = get_user_model()


class EmailAlertSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailAlertSettings
        fields = "__all__"
        read_only_fields = ("created_dt", "updated_dt", "user")


class PiBootEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = PiBootEvent
        exclude = ("deleted",)
        read_only_fields = ("created_dt",)


class PiSoftwareUpdateEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = PiSoftwareUpdateEvent
        exclude = ("deleted",)
        read_only_fields = ("created_dt",)


class PiGstreamerEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = PiGstreamerEvent
        exclude = ("deleted",)
        read_only_fields = ("created_dt",)


class PolymorphicPiEventSerializer(PolymorphicSerializer):
    """
    Generic polymorphic serializer for all Events

    The model field is used to distinguish Polymorphic serializers/models from each other
    Each model has a 1-1 relationship with models derived from Event in print_nanny_webapp.events.models
    The model field is equivalent to a Type

    The event_name field equivalent to a "sub type"
    """

    resource_type_field_name = "__class__"
    # Model -> Serializer mapping
    model_serializer_mapping = {
        PiGstreamerEvent: PiGstreamerEventSerializer,
        PiSoftwareUpdateEvent: PiSoftwareUpdateEventSerializer,
        PiBootEvent: PiBootEventSerializer,
    }
