import logging
from collections.abc import Mapping
from rest_framework import serializers
from rest_polymorphic.serializers import PolymorphicSerializer
from print_nanny_webapp.events.models import TestEvent, Event
from print_nanny_webapp.events.enum import (
    EventSource,
    TestEventType,
    EventStatus,
)

logger = logging.getLogger(__name__)


class EventSerializer(serializers.ModelSerializer):
    # resourcetype = serializers.ChoiceField(choices=[
    #     "TestEvent"
    # ])

    class Meta:
        model = Event
        read_only_fields = ("user", "device", "created_dt")


class TestEventSerializer(EventSerializer):
    resourcetype = serializers.CharField(default="TestEvent")

    class Meta:
        model = TestEvent
        read_only_fields = ("user", "device", "created_dt")
        fields = ("id", "type", "status", "source", "resourcetype")


class PolymorphicEventSerializer(PolymorphicSerializer):
    model_serializer_mapping = {
        TestEvent: TestEventSerializer,
    }

    def to_representation(self, instance):
        logger.info("Got instance", instance)
        if isinstance(instance, Mapping):
            resource_type = self._get_resource_type_from_mapping(instance)
            serializer = self._get_serializer_from_resource_type(resource_type)
        else:
            resource_type = self.to_resource_type(instance)
            serializer = self._get_serializer_from_model_or_instance(instance)

        ret = serializer.to_representation(instance)
        return ret
