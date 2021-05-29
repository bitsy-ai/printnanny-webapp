import logging

from django.contrib.auth import get_user_model
from django.db import models
from django.apps import apps

from django.apps import apps
from django.contrib.postgres.fields import JSONField
from print_nanny_webapp.telemetry.types import (
    PrintNannyPluginEventType,
    OctoprintEventType,
    RemoteCommandEventType,
    PrintStatusEventType,
)

User = get_user_model()
logger = logging.getLogger(__name__)


class TelemetryEvent(models.Model):
    """
    Base class for client-side events
    """

    class Meta:
        abstract = True

    created_dt = models.DateTimeField(auto_now_add=True, db_index=True)
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


class RemoteCommandEvent(TelemetryEvent):
    """
    Commands sent to the OctoPrint device
    """

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

    event_codes = [x.value for x in OctoprintEventType.__members__.values()]
    event_type = models.CharField(
        max_length=255, db_index=True, choices=OctoprintEventType.choices
    )
    print_session = models.ForeignKey(
        "remote_control.PrintSession",
        null=True,
        on_delete=models.CASCADE,
        db_index=True,
    )


class PrintStatusEvent(TelemetryEvent):
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
    print_session = models.ForeignKey(
        "remote_control.PrintSession",
        null=True,
        on_delete=models.CASCADE,
        db_index=True,
    )
