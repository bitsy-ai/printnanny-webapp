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
