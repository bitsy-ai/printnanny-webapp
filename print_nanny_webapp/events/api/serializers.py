from collections.abc import Mapping
from rest_framework import serializers
from rest_polymorphic.serializers import PolymorphicSerializer
from print_nanny_webapp.events.models import TestEvent, Event
from print_nanny_webapp.events.enum import (
    EventSource,
    TestEventType,
    EventStatus,
)


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"
        read_only_fields = ("user", "polymorphic_ctype")


class TestEventSerializer(EventSerializer):
    class Meta:
        model = TestEvent
        fields = "__all__"


class PolymorphicEventSerializer(PolymorphicSerializer):
    model_serializer_mapping = {
        Event: EventSerializer,
        TestEvent: TestEventSerializer,
    }

    def to_representation(self, instance):
        if isinstance(instance, Mapping):
            resource_type = self._get_resource_type_from_mapping(instance)
            serializer = self._get_serializer_from_resource_type(resource_type)
        else:
            resource_type = self.to_resource_type(instance)
            serializer = self._get_serializer_from_model_or_instance(instance)

        ret = serializer.to_representation(instance)
        return ret
