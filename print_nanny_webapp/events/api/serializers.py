import logging
from rest_framework import serializers
from rest_polymorphic.serializers import PolymorphicSerializer
from print_nanny_webapp.events.models import Event, WebRTCEvent
from print_nanny_webapp.events.enum import EventSource, WebRTCEventType

logger = logging.getLogger(__name__)


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        read_only_fields = ("user", "created_dt")
        fields = "__all__"


class WebRTCEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebRTCEvent
        read_only_fields = "device"


class PolymorphicEventSerializer(PolymorphicSerializer):
    resource_type_field_name = "event_type"
    model_serializer_mapping = {WebRTCEvent: WebRTCEventSerializer}

    resourcetype_map = {
        WebRTCEventType.CLOUD_MONITOR_START.value: WebRTCEvent.__name__,
        WebRTCEventType.CLOUD_MONITOR_STOP.value: WebRTCEvent.__name__,
    }

    def create(self, validated_data):
        """
        Override PolymorphicSerializer.create to skip validated_data.pop(self.resource_type_field_name)
        """
        resource_type = validated_data[self.resource_type_field_name]
        serializer = self._get_serializer_from_resource_type(resource_type)
        return serializer.create(validated_data)

    def update(self, instance, validated_data):
        resource_type = validated_data[self.resource_type_field_name]
        serializer = self._get_serializer_from_resource_type(resource_type)
        return serializer.update(instance, validated_data)

    def _get_resource_type_from_mapping(self, mapping):
        logger.info(
            "PolymorphicEventSerializer mapping=%s resourcetype_map=%s",
            mapping,
            self.resourcetype_map,
        )
        try:
            task_type = mapping[self.resource_type_field_name]
            logger.info("PolymorphicEventSerializer task_type=%s", task_type)
            return self.resourcetype_map[task_type]
        except KeyError:
            raise serializers.ValidationError(
                {
                    self.resource_type_field_name: "Failed to extract resource from field",
                }
            )
