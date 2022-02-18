import logging
from django.apps import apps
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_polymorphic.serializers import PolymorphicSerializer
from print_nanny_webapp.events.models import Event, WebRTCEvent
from print_nanny_webapp.events.enum import EventSource, WebRTCEventType

logger = logging.getLogger(__name__)

Device = apps.get_model("devices", "Device")
User = get_user_model()


class EventSerializer(serializers.ModelSerializer):
    source = serializers.ChoiceField(choices=EventSource.choices)

    class Meta:
        model = Event
        read_only_fields = ("user", "created_dt")
        fields = "__all__"


class WebRTCEventSerializer(serializers.ModelSerializer):
    event_type = serializers.ChoiceField(choices=WebRTCEventType.choices)

    class Meta:
        model = WebRTCEvent
        fields = "__all__"
        read_only_fields = ("user", "created_dt")

    def validate(self, attrs):
        """
        Check user owns device
        """
        user = User.objects.get(id=attrs["user"])
        device = Device.objects.get(id=attrs["device"])
        if user.id != device.id:
            raise serializers.ValidationError("finish must occur after start")
        return attrs


class PolymorphicEventSerializer(PolymorphicSerializer):
    """
    Generic polymorphic serializer for all Events
    """

    resource_type_field_name = "event_type"
    # Model -> Serializer mapping
    model_serializer_mapping = {WebRTCEvent: WebRTCEventSerializer}

    resourcetype_map = {
        # event_type value -> Model mapping
        e: WebRTCEvent.__name__
        for e in WebRTCEventType.values
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
