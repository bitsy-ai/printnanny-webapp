import logging
from typing import Mapping
from django.apps import apps
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_polymorphic.serializers import PolymorphicSerializer
from print_nanny_webapp.events.models import Event, WebRTCEvent
from print_nanny_webapp.events.enum import EventSource, WebRTCEventType
from rest_framework.fields import empty

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
    # event_type = serializers.ChoiceField(choices=WebRTCEventType.choices)
    # device = serializers.PrimaryKeyRelatedField(queryset=Device.objects.all())

    class Meta:
        model = WebRTCEvent
        fields = "__all__"
        read_only_fields = ("user", "created_dt")


class PolymorphicEventSerializer(PolymorphicSerializer):
    """
    Generic polymorphic serializer for all Events

    A few private methods from PolymorphicSerializer are overridden to allow a persistent "event_type" field
    The default PolymorphicSerializer behavior discards the resourcetype field (event_type in this case) and does not save with the model
    """

    resource_type_field_name = "event_type"
    # Model -> Serializer mapping
    model_serializer_mapping = {WebRTCEvent: WebRTCEventSerializer}
    resource_type_model_mapping = {e.value: WebRTCEvent for e in WebRTCEventType}
    resourcetype_map = {
        # event_type value -> Model mapping
        e.value: WebRTCEvent.__name__
        for e in WebRTCEventType
    }

    def __init__(self, *args, **kwargs):
        super(serializers.Serializer, self).__init__(*args, **kwargs)

        model_serializer_mapping = self.model_serializer_mapping
        self.model_serializer_mapping = {}
        for model, serializer in model_serializer_mapping.items():
            if callable(serializer):
                serializer = serializer(*args, **kwargs)
                serializer.parent = self
            self.model_serializer_mapping[model] = serializer

    def create(self, validated_data):
        """
        Override PolymorphicSerializer.create to skip validated_data.pop(self.resource_type_field_name)
        """
        resource_type = validated_data[self.resource_type_field_name]
        # this is because PolymorphicSerializer expects to .pop() and discard the resourcetype field
        # instead of discarding resourcetype, we save as event_type
        # resource_type = validated_data.pop(self.resource_type_field_name)

        serializer = self._get_serializer_from_resource_type(resource_type)
        return serializer.create(validated_data)

    def update(self, instance, validated_data):
        resource_type = validated_data[self.resource_type_field_name]
        # this is because PolymorphicSerializer expects to .pop() and discard the resourcetype field
        # instead of discarding resourcetype, we save as event_type
        # resource_type = validated_data.pop(self.resource_type_field_name)

        serializer = self._get_serializer_from_resource_type(resource_type)
        return serializer.update(instance, validated_data)

    def to_representation(self, instance):
        if isinstance(instance, Mapping):
            resource_type = self._get_resource_type_from_mapping(instance)
            serializer = self._get_serializer_from_resource_type(resource_type)
        else:
            resource_type = self.to_resource_type(instance)
            serializer = self._get_serializer_from_model_or_instance(instance)

        ret = serializer.to_representation(instance)
        return ret
