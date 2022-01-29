import logging
from collections.abc import Mapping
from rest_framework import serializers
from rest_polymorphic.serializers import PolymorphicSerializer
from print_nanny_webapp.events.models import TestEvent, Event
from print_nanny_webapp.events.enum import (
    EventSource,
    TestEventType,
    EventStatus,
    EventModel,
)

logger = logging.getLogger(__name__)


class EventSerializer(serializers.ModelSerializer):
    model = serializers.ChoiceField(choices=EventModel.choices)

    class Meta:
        model = Event
        read_only_fields = ("user", "device", "created_dt")


class TestEventSerializer(EventSerializer):
    model = serializers.ChoiceField(choices=[EventModel.TestEvent])

    class Meta:
        model = TestEvent
        fields = "__all__"
        read_only_fields = ("user", "device", "created_dt")
        fields = (
            "command",
            "created_dt",
            "device",
            "event_type",
            "id",
            "model",
            "source",
            "status",
            "user",
        )


class PolymorphicEventSerializer(PolymorphicSerializer):
    resource_type_field_name = "model"
    model_serializer_mapping = {
        TestEvent: TestEventSerializer,
    }

    resourcetype_map = {v: TestEvent._meta.object_name for v in TestEventType.values}

    def _get_resource_type_from_mapping(self, mapping):
        logger.debug(
            f"Got PolymorphicEventSerializer mapping={mapping} resourcetype_map={self.resourcetype_map}"
        )
        try:
            return mapping[self.resource_type_field_name]
        except KeyError:
            raise serializers.ValidationError(
                {
                    self.resource_type_field_name: "This field is required",
                }
            )

    def to_representation(self, instance):
        if isinstance(instance, Mapping):
            resource_type = self._get_resource_type_from_mapping(instance)
            serializer = self._get_serializer_from_resource_type(resource_type)
        else:
            resource_type = self.to_resource_type(instance)
            serializer = self._get_serializer_from_model_or_instance(instance)

        ret = serializer.to_representation(instance)
        return ret
