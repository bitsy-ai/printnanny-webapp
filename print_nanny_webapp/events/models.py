import logging

from django.contrib.auth import get_user_model
from django.db import models
from polymorphic.managers import PolymorphicManager
from polymorphic.models import PolymorphicModel
from safedelete.managers import SafeDeleteManager
from safedelete.models import SafeDeleteModel, SOFT_DELETE
from .enum import EventSource, TestEventName, WebRTCEventName, EventType

User = get_user_model()
logger = logging.getLogger(__name__)


class Event(PolymorphicModel, SafeDeleteModel):
    """
    Polymorphic Base Event
    """

    class Meta:
        ordering = ["-created_dt"]
        index_together = [["user", "source", "created_dt"]]

    _safedelete_policy = SOFT_DELETE
    created_dt = models.DateTimeField(auto_now_add=True)
    source = models.CharField(max_length=32, choices=EventSource.choices)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    send_ws = models.BooleanField(
        default=True, help_text="Broadcast to events websocket: /ws/events"
    )


class TestEvent(Event):
    event_type = EventType.TestEvent

    class Meta:
        index_together = [["device", "event_name"]]

    event_name = models.CharField(max_length=32, choices=TestEventName.choices)
    device = models.ForeignKey(
        "devices.Device", on_delete=models.CASCADE, related_name="test_events"
    )
    send_mqtt = models.BooleanField(
        default=True,
        help_text="Broadcast to mqtt topic: /devices/{device-id}/commands/",
    )


class WebRTCEventManager(PolymorphicManager, SafeDeleteManager):
    def create(self, **kwargs):

        event_name = kwargs.get("event_name")
        if event_name == WebRTCEventName.STREAM_START:
            from print_nanny_webapp.devices.services import janus_cloud_setup
            from print_nanny_webapp.devices.models import Device

            device_id = kwargs.get("device_id")
            device = Device.objects.get(id=device_id)
            stream = janus_cloud_setup(device)
            return super().create(stream=stream, **kwargs)

        return super().create(**kwargs)


class WebRTCEvent(Event):
    """
    Events related to WebRTC and PrintNanny video monitoring system
    """

    event_type = EventType.WebRTCEvent
    objects = WebRTCEventManager()

    class Meta:
        index_together = [["device", "stream", "event_name"]]

    event_name = models.CharField(max_length=32, choices=WebRTCEventName.choices)
    device = models.ForeignKey(
        "devices.Device", on_delete=models.CASCADE, related_name="webrtc_events"
    )
    stream = models.ForeignKey(
        "devices.JanusStream", on_delete=models.CASCADE, null=True
    )
    data = models.JSONField(default=dict)
    send_mqtt = models.BooleanField(
        default=True,
        help_text="Broadcast to mqtt topic: /devices/{device-id}/commands/",
    )
