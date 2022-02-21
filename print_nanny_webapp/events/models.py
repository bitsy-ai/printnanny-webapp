import logging

from django.contrib.auth import get_user_model
from django.db import models
from polymorphic.models import PolymorphicModel
from safedelete.models import SafeDeleteModel, SOFT_DELETE
from .enum import EventSource, WebRTCEventName

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


class WebRTCEvent(Event):
    """
    Events related to WebRTC and PrintNanny video monitoring system
    """

    class Meta:
        index_together = [["device", "stream", "event_name"]]

    event_name = models.CharField(max_length=32, choices=WebRTCEventName.choices)
    device = models.ForeignKey(
        "devices.Device", on_delete=models.CASCADE, related_name="events"
    )
    stream = models.ForeignKey(
        "devices.JanusStream", on_delete=models.CASCADE, null=True
    )
    data = models.JSONField(default=dict)
