import logging
from django.apps import apps
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_polymorphic.serializers import PolymorphicSerializer
from print_nanny_webapp.devices.api.serializers import JanusStreamSerializer
from print_nanny_webapp.events.models import Event, WebRTCEvent, TestEvent
from print_nanny_webapp.events.enum import (
    EventSource,
    EventModel,
    TestEventModel,
    WebRTCEventModel,
)

logger = logging.getLogger(__name__)

Device = apps.get_model("devices", "Device")
User = get_user_model()


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        exclude = ("deleted",)
        read_only_fields = ("user", "created_dt")


class TestEventSerializer(serializers.ModelSerializer):
    model = serializers.ChoiceField(choices=TestEventModel.choices)

    class Meta:
        model = TestEvent
        exclude = ("deleted",)
        read_only_fields = ("user", "created_dt")


class WebRTCEventSerializer(serializers.ModelSerializer):
    model = serializers.ChoiceField(choices=WebRTCEventModel.choices)
    stream = JanusStreamSerializer(read_only=True)

    class Meta:
        model = WebRTCEvent
        exclude = ("deleted",)
        read_only_fields = ("user", "created_dt", "stream")


class PolymorphicEventSerializer(PolymorphicSerializer):
    """
    Generic polymorphic serializer for all Events

    The model field is used to distinguish Polymorphic serializers/models from each other
    Each model has a 1-1 relationship with models derived from Event in print_nanny_webapp.events.models
    The model field is equivalent to a Type

    The event_name field equivalent to a "sub type"
    """

    resource_type_field_name = "model"
    # Model -> Serializer mapping
    model_serializer_mapping = {
        WebRTCEvent: WebRTCEventSerializer,
        TestEvent: TestEventSerializer,
    }
