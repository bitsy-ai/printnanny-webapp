import logging

from django.contrib.auth import get_user_model
from django.db import models
from django.apps import apps

from polymorphic.models import PolymorphicModel

from django.apps import apps
from print_nanny_webapp.telemetry.types import (
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


class PrinterEvent(TelemetryEvent):
    def __init__(self, *args, **kwargs):
        return super().__init__(*args, event_source=EventSource.OCTOPRINT, **kwargs)

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
        return super().__init__(*args, event_source=EventSource.OCTOPRINT, **kwargs)

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
