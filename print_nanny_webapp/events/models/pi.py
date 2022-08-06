from django.db import models

from print_nanny_webapp.events.models.base import AbstractPiEvent
from print_nanny_webapp.events.models.enum import (
    PiBootEventType,
    PiGstreamerEventType,
    PiSoftwareUpdateEventType,
    PiEventModel,
)


class BasePiEvent(AbstractPiEvent):
    pass


class PiBootEvent(BasePiEvent):
    """
    Events emitted by Raspberry Pi during boot process
    """

    model = PiEventModel.PiBootEvent

    class Meta:
        index_together = ()

    event_type = models.CharField(
        max_length=32, choices=PiBootEventType.choices, db_index=True
    )

    # @property
    # def subject(self):
    #     return f"pi.{self.pi.id}.boot"


class PiSoftwareUpdateEvent(BasePiEvent):
    """
    Events related to Raspberry Pi upgrade process
    """

    model = PiEventModel.PiSoftwareUpdateEvent

    class Meta:
        index_together = [["version", "event_type"]]

    version = models.CharField(max_length=32)
    event_type = models.CharField(
        max_length=32,
        choices=PiSoftwareUpdateEventType.choices,
    )

    # @property
    # def subject(self):
    #     return f"pi.{self.pi.id}.swupdate"


class PiGstreamerEvent(BasePiEvent):
    model = PiEventModel.PiGstreamerEvent

    class Meta:

        index_together = ()

    event_type = models.CharField(
        max_length=32, choices=PiGstreamerEventType.choices, db_index=True
    )

    # @property
    # def subject(self):
    #     return f"pi.{self.pi.id}.gst.command"
