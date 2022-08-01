from django.db import models

from .base import AbstractPiEvent
from .enum import (
    PiBootEventType,
    PiBootCommandType,
    PiGstreamerCommandType,
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


class PiBootCommand(BasePiEvent):
    """
    Events emitted by PrintNanny Cloud or other user-facing services
    Raspberry Pi subscribes to command subjects
    """

    class Meta:
        index_together = ()

    event_type = models.CharField(
        max_length=32, choices=PiBootCommandType.choices, db_index=True
    )


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


class PiGstreamerCommand(BasePiEvent):
    class Meta:
        index_together = ()

    event_type = models.CharField(
        max_length=32, choices=PiGstreamerCommandType.choices, db_index=True
    )
