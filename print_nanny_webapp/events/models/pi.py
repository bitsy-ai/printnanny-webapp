from django.db import models

from .base import AbstractPiEvent
from .enum import (
    PiBootEventType,
    PiGstreamerEventType,
    PiSoftwareUpdateEventType,
)


class BasePiEvent(AbstractPiEvent):
    pass


class PiBootEvent(BasePiEvent):
    """
    Events emitted by Raspberry Pi during boot process
    """

    class Meta:
        index_together = ()

    event_type = models.CharField(
        max_length=32, choices=PiBootEventType.choices, db_index=True
    )

    @property
    def subject(self):
        return f"pi.{self.pi.id}.boot"


class PiSoftwareUpdateEvent(BasePiEvent):
    """
    Events related to Raspberry Pi upgrade process
    """

    class Meta:
        index_together = [["version", "event_type"]]

    version = models.CharField(max_length=32)
    event_type = models.CharField(
        max_length=32,
        choices=PiSoftwareUpdateEventType.choices,
    )

    @property
    def subject(self):
        return f"pi.{self.pi.id}.swupdate"


class PiGstreamerEvent(BasePiEvent):
    class Meta:
        index_together = ()

    event_type = models.CharField(
        max_length=32, choices=PiGstreamerEventType.choices, db_index=True
    )

    @property
    def subject(self):
        return f"pi.{self.pi.id}.gst.command"
