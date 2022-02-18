import logging

from django.contrib.auth import get_user_model
from django.db import models
from django.apps import apps
from polymorphic.models import PolymorphicModel
from safedelete.models import SafeDeleteModel, SOFT_DELETE
from .enum import EventSource, WebRTCType

User = get_user_model()
logger = logging.getLogger(__name__)


class Event(PolymorphicModel, SafeDeleteModel):
    """
    Polymorphic Base Event
    """

    _safedelete_policy = SOFT_DELETE
    created_dt = models.DateTimeField(auto_now_add=True, db_index=True)
    source = models.CharField(max_length=32, choices=EventSource.choices)
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True)


class WebRTCEvent(Event):
    """
    Events related to WebRTC and PrintNanny video monitoring system
    """

    event_type = models.CharField(max_length=32, choices=WebRTCType.choices)
    device = models.ForeignKey("devices.Device", on_delete=models.CASCADE)
