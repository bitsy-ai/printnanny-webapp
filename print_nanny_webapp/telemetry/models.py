import logging

from django.contrib.auth import get_user_model
from django.db import models
from django.apps import apps

from polymorphic.models import PolymorphicModel

from django.apps import apps
from print_nanny_webapp.telemetry.enum import (
    PrintNannyPluginEventType,
    OctoprintEventType,
    RemoteCommandEventType,
    PrintJobEventType,
    EventSource,
    TelemetryEventType,
    PrinterEventType,
)
from polymorphic.managers import PolymorphicManager

User = get_user_model()
logger = logging.getLogger(__name__)


class TelemetryEvent(PolymorphicModel):
    """
    Base class for client-side events
    """

    event_type = models.CharField(
        max_length=255,
        db_index=True,
        choices=TelemetryEventType.choices,
        default=TelemetryEventType.CONNECT_TEST_NOOP,
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
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True)
    print_nanny_plugin_version = models.CharField(max_length=60)
    print_nanny_client_version = models.CharField(max_length=60)
    print_nanny_beta_client_version = models.CharField(max_length=60, null=True)
    octoprint_version = models.CharField(max_length=36)


class RemoteCommandEvent(TelemetryEvent):
    """
    Commands sent to the OctoPrint device
    """

    def __init__(self, *args, **kwargs):
        if "event_source" in kwargs.keys():
            kwargs.pop("event_source")
        event_source = EventSource.REMOTE_COMMAND
        return super().__init__(*args, event_source=event_source, **kwargs)

    event_codes = [x.value for x in RemoteCommandEventType.__members__.values()]


class PrintNannyPluginEvent(TelemetryEvent):
    """
    Events emitted by OctoPrint Nanny plugin

    OctoPrint sends these as snake-cased strings

    For use with: https://docs.octoprint.org/en/master/plugins/hooks.html?highlight=custom_events#octoprint-events-register-custom-events
    """

    def __init__(self, *args, **kwargs):
        if "event_source" in kwargs.keys():
            kwargs.pop("event_source")
        event_source = event_source = EventSource.PRINT_NANNY_PLUGIN
        return super().__init__(*args, event_source=event_source, **kwargs)

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
        if "event_source" in kwargs.keys():
            kwargs.pop("event_source")
        event_source = EventSource.OCTOPRINT
        return super().__init__(*args, event_source=event_source, **kwargs)

    event_codes = [x.value for x in OctoprintEventType.__members__.values()]


class PrinterEvent(TelemetryEvent):
    def __init__(self, *args, **kwargs):
        if "event_source" in kwargs.keys():
            kwargs.pop("event_source")
        event_source = EventSource.OCTOPRINT
        return super().__init__(*args, event_source=event_source, **kwargs)

    CSS_CLASS_MAP = {
        "closedOrError": "text-danger",
        "Error": "text-danger",
        "Ready": "text-success",
        "sdReady": "text-success",
        "Pausing": "text-warning",
        "Cancelling": "text-warning",
        "Paused": "text-warning",
        "Operational": "text-success",
        "Printing": "text-success",
        "Offline": "text-warning",
        "offline": "text-warning",
        "Connecting": "text-warning",
        "Opening serial connection": "text-warning",
        "Resuming": "text-warning",
        "Finishing": "text-warning",
    }
    event_codes = [x.value for x in PrinterEventType.__members__.values()]
    printer_state = models.CharField(
        max_length=36,
        choices=PrinterEventType.choices,
        default=PrinterEventType.DISCONNECTED,
    )

    @property
    def css_class(self):
        return self.CSS_CLASS_MAP[self.event_type]


class PrintJobEvent(TelemetryEvent):
    def __init__(self, *args, **kwargs):
        if "event_source" in kwargs.keys():
            kwargs.pop("event_source")
        event_source = EventSource.OCTOPRINT
        return super().__init__(*args, event_source=event_source, **kwargs)

    event_codes = [x.value for x in PrintJobEventType.__members__.values()]
    CSS_CLASS_MAP = {
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

    @property
    def css_class(self):
        return self.CSS_CLASS_MAP[self.event_type]
