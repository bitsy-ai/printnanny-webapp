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
)

User = get_user_model()
logger = logging.getLogger(__name__)


class TelemetryEvent(PolymorphicModel):
    """
    Base class for client-side events
    """
    event_type = RemoteCommandEventType.choices

    created_dt = models.DateTimeField(auto_now_add=True, db_index=True)
    event_source = models.CharField(max_length=36, choices=EventSource.choices, default=EventSource.PRINT_NANNY_PLUGIN)
    event_data = models.JSONField(null=True)
    octoprint_device = models.ForeignKey(
        "remote_control.OctoPrintDevice",
        db_index=True,
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True)
    plugin_version = models.CharField(max_length=60)
    client_version = models.CharField(max_length=60)
    octoprint_version = models.CharField(max_length=60)
    metadata = JSONField(null=True)
    octoprint_job = JSONField(null=True)
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
        return super().__init__(*args, event_source=EventSource.REMOTE_COMMAND, **kwargs)

    event_codes = [x.value for x in RemoteCommandEventType.__members__.values()]
    event_type = models.CharField(
        max_length=255, db_index=True, choices=RemoteCommandEventType.choices
    )


class PrintNannyPluginEvent(TelemetryEvent):
    """
    Events emitted by OctoPrint Nanny plugin

    OctoPrint sends these as snake-cased strings

    For use with: https://docs.octoprint.org/en/master/plugins/hooks.html?highlight=custom_events#octoprint-events-register-custom-events
    """
    def __init__(self, *args, **kwargs):
        return super().__init__(*args, event_source=EventSource.PRINT_NANNY_PLUGIN, **kwargs)

    plugin_identifier = "octoprint_nanny"
    octoprint_event_prefix = "plugin_octoprint_nanny_"

    event_codes = [x.value for x in PrintNannyPluginEventType.__members__.values()]

    event_type = models.CharField(
        max_length=255, db_index=True, choices=PrintNannyPluginEventType.choices
    )

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
    event_type = models.CharField(
        max_length=255, db_index=True, choices=OctoprintEventType.choices
    )



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
    event_type = models.CharField(
        max_length=255, db_index=True, choices=PrintStatusEventType.choices
    )
    state = JSONField(default=dict)
    current_z = models.FloatField(null=True)
    # {'completion': 0.0008570890761342134, 'filepos': 552, 'printTime': 0, 'printTimeLeft': 29826, 'printTimeLeftOrigin': 'analysis'}.
    progress = JSONField(default=dict)
    job_data_file = models.CharField(max_length=255)
