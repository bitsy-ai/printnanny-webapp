import logging

from django.contrib.auth import get_user_model
from django.db import models
from django.apps import apps

from polymorphic.models import PolymorphicModel

from django.apps import apps
from django.contrib.postgres.fields import JSONField
from print_nanny_webapp.telemetry.types import (
    PrintNannyPluginEventType,
    OctoprintEventType,
    RemoteCommandEventType,
    PrintStatusEventType,
    EventSource,
    TelemetryEventType,
    PrinterState
)
from polymorphic.managers import PolymorphicManager

User = get_user_model()
logger = logging.getLogger(__name__)


class TelemetryEventManager(PolymorphicManager):
    def create(self, user=None, **kwargs):
        from print_nanny_webapp.remote_control.models import OctoPrintDevice

        if user is None:
            octoprint_device = kwargs.get("octoprint_device")
            if octoprint_device is None:
                octoprint_device_id = kwargs.get("octoprint_device_id")
                if octoprint_device_id is None:
                    raise ValueError("octoprint_device is required")
                octoprint_device = OctoPrintDevice.objects.get(id=octoprint_device_id)
            user = octoprint_device.user
        return super().create(user=user, **kwargs)


class TelemetryEvent(PolymorphicModel):
    """
    Base class for client-side events
    """

    objects = TelemetryEventManager()

    event_type = models.CharField(
        max_length=255, db_index=True, choices=TelemetryEventType.choices
    )
    ts = models.DateTimeField(auto_now_add=True, db_index=True)
    event_source = models.CharField(
        max_length=36,
        choices=EventSource.choices,
        default=EventSource.PRINT_NANNY_PLUGIN,
    )
    event_data = models.JSONField(default=dict, null=True)
    octoprint_environment = models.JSONField(default=dict)
    octoprint_printer_data = models.JSONField(default=dict)
    temperature = models.JSONField(default=dict)
    octoprint_device = models.ForeignKey(
        "remote_control.OctoPrintDevice",
        db_index=True,
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True)
    print_nanny_plugin_version = models.CharField(max_length=60)
    print_nanny_client_version = models.CharField(max_length=60)
    octoprint_version = models.CharField(max_length=36)
    print_session = models.ForeignKey(
        "remote_control.PrintSession",
        null=True,
        on_delete=models.CASCADE,
        db_index=True,
    )


class RemoteCommandEvent(TelemetryEvent):
    """
    Commands sent to the OctoPrint device
    """

    def __init__(self, *args, **kwargs):
        return super().__init__(
            *args, event_source=EventSource.REMOTE_COMMAND, **kwargs
        )

    event_codes = [x.value for x in RemoteCommandEventType.__members__.values()]


class PrintNannyPluginEvent(TelemetryEvent):
    """
    Events emitted by OctoPrint Nanny plugin

    OctoPrint sends these as snake-cased strings

    For use with: https://docs.octoprint.org/en/master/plugins/hooks.html?highlight=custom_events#octoprint-events-register-custom-events
    """

    def __init__(self, *args, **kwargs):
        return super().__init__(
            *args, event_source=EventSource.PRINT_NANNY_PLUGIN, **kwargs
        )

    plugin_identifier = "octoprint_nanny"
    octoprint_event_prefix = "plugin_octoprint_nanny_"

    event_codes = [x.value for x in PrintNannyPluginEventType.__members__.values()]

    @classmethod
    def strip_octoprint_prefix(self, event_type):

        return event_type.replace(self.octoprint_event_prefix, "")


class OctoPrintEvent(TelemetryEvent):
    """
    Events emitted by OctoPrint Core and plugins bundled with core
    PascalCased strings
    """

    def __init__(self, *args, **kwargs):
        return super().__init__(*args, event_source=EventSource.OCTOPRINT, **kwargs)

    event_codes = [x.value for x in OctoprintEventType.__members__.values()]


class PrintStatusEvent(TelemetryEvent):
    def __init__(self, *args, **kwargs):
        return super().__init__(*args, event_source=EventSource.OCTOPRINT, **kwargs)

    event_codes = [x.value for x in PrintStatusEventType.__members__.values()]
    JOB_EVENT_TYPE_CSS_CLASS = {
        "Error": "text-danger",
        "PrintCancelled": "text-danger",
        "PrintCancelling": "text-danger",
        "PrintDone": "text-success",
        "PrintFailed": "text-danger",
        "PrintPaused": "text-warning",
        "PrintResumed": "text-success",
        "PrintStarted": "text-success",
        "Idle": "text-warning",
    }
    # https://docs.octoprint.org/en/master/api/datamodel.html?highlight=flags#printer-state (text)
    printer_state = models.CharField(max_length=255, choices=PrinterState.choices, null=True)


    # state = JSONField(default=dict)
    # current_z = models.FloatField(null=True)
    # # {'completion': 0.0008570890761342134, 'filepos': 552, 'printTime': 0, 'printTimeLeft': 29826, 'printTimeLeftOrigin': 'analysis'}.
    # progress = JSONField(default=dict)
    # job_data_file = models.CharField(max_length=255)
