import logging
from django.apps import apps
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_polymorphic.serializers import PolymorphicSerializer
from print_nanny_webapp.events.models import Event, WebRTCEvent, TestEvent
from print_nanny_webapp.events.enum import EventSource, EventType

logger = logging.getLogger(__name__)

Device = apps.get_model("devices", "Device")
User = get_user_model()


class EventSerializer(serializers.ModelSerializer):
    source = serializers.ChoiceField(choices=EventSource.choices)

    class Meta:
        model = Event
        exclude = ("deleted",)
        read_only_fields = ("user", "created_dt")


class TestEventSerializer(serializers.ModelSerializer):
    event_type = serializers.ChoiceField(choices=[EventType.TestEvent])

    class Meta:
        model = TestEvent
        exclude = ("deleted",)
        read_only_fields = ("user", "created_dt")


class WebRTCEventSerializer(serializers.ModelSerializer):
    event_type = serializers.ChoiceField(choices=[EventType.WebRTCEvent])

    class Meta:
        model = WebRTCEvent
        exclude = ("deleted",)
        read_only_fields = ("user", "created_dt", "stream")


class PolymorphicEventSerializer(PolymorphicSerializer):
    """
    Generic polymorphic serializer for all Events

    A few private methods from PolymorphicSerializer are overridden to allow a persistent "event_type" field
    The default PolymorphicSerializer behavior discards the resourcetype field (event_type in this case) and does not save with the model
    """

    resource_type_field_name = "event_type"
    # Model -> Serializer mapping
    model_serializer_mapping = {
        WebRTCEvent: WebRTCEventSerializer,
        TestEvent: TestEventSerializer,
    }
