import logging

from django.contrib.auth import get_user_model
from django.db import models
from django.apps import apps
from polymorphic.models import PolymorphicModel
from safedelete.models import SafeDeleteModel, SOFT_DELETE
from .enum import EventSource, PrintNannyEventType, PrintNannyEventStatus

User = get_user_model()
logger = logging.getLogger(__name__)


class Event(PolymorphicModel, SafeDeleteModel):
    """
    Polymorphic Base Event
    """

    _safedelete_policy = SOFT_DELETE
    created_dt = models.DateTimeField(auto_now_add=True, db_index=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True)


class PrintNannyEvent(Event):
    """
    Events emitted by Print Nanny OS
    """

    source = EventSource.PRINT_NANNY
    type = models.CharField(max_length=255, choices=PrintNannyEventType.choices)
    status = models.CharField(
        max_length=255,
        choices=PrintNannyEventStatus.choices,
        default=PrintNannyEventStatus.SENT,
    )
    device = models.ForeignKey("devices.Device", on_delete=models.CASCADE)
