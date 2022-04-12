import logging

from django.contrib.auth import get_user_model
from django.db import models
from polymorphic.models import PolymorphicModel
from safedelete.models import SafeDeleteModel, SOFT_DELETE
from .enum import (
    EventSource,
    TestEventName,
    WebRTCEventName,
    EventModel,
    OctoPrintEventName,
)

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
    model = EventModel.TestEvent

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


class OctoPrintEvent(Event):
    class Meta:
        index_together = (("octoprint_install", "device", "event_name"),)

    octoprint_install = models.ForeignKey(
        "octoprint.OctoPrintInstall",
        on_delete=models.CASCADE,
        related_name="octoprint_events",
    )
    event_name = models.CharField(max_length=32, choices=OctoPrintEventName.choices)
    device = models.ForeignKey(
        "devices.Device", on_delete=models.CASCADE, related_name="octoprint_events"
    )
    payload = models.JSONField(default=dict)


class WebRTCEvent(Event):
    """
    Events related to WebRTC and PrintNanny video monitoring system
    """

    model = EventModel.WebRTCEvent

    class Meta:
        index_together = [["device", "stream", "event_name"]]

    event_name = models.CharField(max_length=32, choices=WebRTCEventName.choices)
    device = models.ForeignKey(
        "devices.Device", on_delete=models.CASCADE, related_name="webrtc_events"
    )
    stream = models.ForeignKey("devices.JanusStream", on_delete=models.CASCADE)
    data = models.JSONField(default=dict)
    send_mqtt = models.BooleanField(
        default=True,
        help_text="Broadcast to mqtt topic: /devices/{device-id}/commands/",
    )
