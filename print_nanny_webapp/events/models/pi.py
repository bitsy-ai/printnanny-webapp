from django.db import models

from print_nanny_webapp.events.models.base import AbstractPiEvent
from print_nanny_webapp.events.models.enum import (
    PiBootCommandType,
    PiBootStatusType,
    PiCamCommandType,
    PiCamStatusType,
    PiSoftwareUpdateCommandType,
    PiSoftwareUpdateStatusType,
    PiEventModel,
)


class BasePiEvent(AbstractPiEvent):
    pass


class PiBootCommand(BasePiEvent):
    """
    Commands related to Raspberry Pi boot process
    """

    model = PiEventModel.PiBootStatus

    class Meta:
        index_together = ()

    event_type = models.CharField(
        max_length=32, choices=PiBootCommandType.choices, db_index=True
    )


class PiBootStatus(BasePiEvent):
    """
    Status events emitted by Raspberry Pi during boot process
    """

    model = PiEventModel.PiBootStatus

    class Meta:
        index_together = ()

    event_type = models.CharField(
        max_length=32, choices=PiBootStatusType.choices, db_index=True
    )


class PiSoftwareUpdateCommand(BasePiEvent):
    """
    Commands related to Raspberry Pi upgrade process
    """

    model = PiEventModel.PiSoftwareUpdateCommand

    class Meta:
        index_together = [["version", "event_type"]]

    version = models.CharField(max_length=32)
    event_type = models.CharField(
        max_length=32,
        choices=PiSoftwareUpdateCommandType.choices,
    )


class PiSoftwareUpdateStatus(BasePiEvent):
    """
    Events related to Raspberry Pi upgrade process
    """

    model = PiEventModel.PiSoftwareUpdateStatus

    class Meta:
        index_together = [["version", "event_type"]]

    version = models.CharField(max_length=32)
    event_type = models.CharField(
        max_length=32,
        choices=PiSoftwareUpdateStatusType.choices,
    )


class PiCamCommand(BasePiEvent):
    """
    Commands related to Raspberry Pi camera/gstreamer app
    """

    model = PiEventModel.PiCamCommand

    class Meta:

        index_together = ()

    event_type = models.CharField(
        max_length=32, choices=PiCamCommandType.choices, db_index=True
    )


class PiCamStatus(BasePiEvent):
    """
    Status updates related to Raspberry Pi camera/gstreamer app
    """

    model = PiEventModel.PiCamStatus

    class Meta:

        index_together = ()

    event_type = models.CharField(
        max_length=32, choices=PiCamStatusType.choices, db_index=True
    )
