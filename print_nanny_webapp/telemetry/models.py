import base64
import hashlib
import logging
import subprocess
import tempfile
import enum

from django.contrib.auth import get_user_model
from django.db import models
from django.apps import apps
from django.utils import timezone

from urllib.parse import urljoin

from polymorphic.models import PolymorphicModel
from django.apps import apps
from django.conf import settings
from django.core.files.base import ContentFile
from django.contrib.postgres.fields import ArrayField, JSONField
from django.contrib.sites.shortcuts import get_current_site

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
    device = models.ForeignKey(
        "remote_control.OctoPrintDevice",
        db_index=True,
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True)
    plugin_version = models.CharField(max_length=60)
    client_version = models.CharField(max_length=60)
    octoprint_version = models.CharField(max_length=60)


def _upload_to(instance, filename):
    datesegment = dateformat.format(timezone.now(), "Y/M/d/")
    path = os.path.join(f"uploads/{instance.__class__.__name__}", datesegment, filename)
    logger.info("Uploading to path")
    return path


class RemoteCommandEvent(TelemetryEvent):
    """
    Commands sent to the OctoPrint device
    """

    class EventType(models.TextChoices):

        RECEIVED = (
            "received",
            "Command was received by device",
        )
        FAILED = (
            "failed",
            "Command failed. Please download your Octoprint logs and open a Github issue to get this fixed.",
        )
        SUCCESS = (
            "success",
            "Command succeeded",
        )

        # @todo
        # PRINT_START_RECEIVED
        # PRINT_START_FAILED
        # PRINT_START_SUCCESS

        # PRINT_STOP_RECEIVED
        # PRINT_STOP_FAILED
        # PRINT_STOP_SUCCESS

        # PRINT_PAUSE_RECEIVED
        # PRINT_PAUSE_FAILED
        # PRINT_PAUSE_SUCCESS

        # PRINT_RESUME_RECEIVED
        # PRINT_RESUME_FAILED
        # PRINT_RESUME_SUCCESS

        # MOVE_NOZZLE_RECEIVED
        # MOVE_NOZZLE_FAILED
        # MOVE_NOZZLE_SUCCESS

    event_codes = [x.value for x in EventType.__members__.values()]

    event_type = models.CharField(
        max_length=255, db_index=True, choices=EventType.choices
    )


class OctoPrintPluginEvent(TelemetryEvent):
    """
    Events emitted by OctoPrint Nanny plugin

    OctoPrint sends these as snake-cased strings
    """

    class EventType(models.TextChoices):

        DEVICE_REGISTER_START = "device_register_start", "Device registration started"
        DEVICE_REGISTER_DONE = "device_register_done", "Device registration succeeded"
        DEVICE_REGISTER_FAILED = "device_register_failed", "Device registration failed"

        PRINTER_PROFILE_SYNC_START = (
            "printer_profile_sync_start",
            "Printer profile sync started",
        )
        PRINTER_PROFILE_SYNC_DONE = (
            "printer_profile_sync_done",
            "Printer profile sync succeeded",
        )
        PRINTER_PROFILE_SYNC_FAILED = (
            "printer_profile_sync_failed",
            "Printer profile sync failed",
        )

    event_codes = [x.value for x in EventType.__members__.values()]

    event_type = models.CharField(
        max_length=255, db_index=True, choices=EventType.choices
    )


class OctoPrintEvent(TelemetryEvent):
    """
    Events emitted by OctoPrint Core and plugins bundled with core
    PascalCased strings
    """

    class EventType(models.TextChoices):
        # OctoPrint javascript client / browser -> OctoPrint server (not Print Nanny webapp)
        CLIENT_AUTHED = "ClientAuthed", "ClientAuthed"
        CLIENT_CLOSED = "ClientClosed", "ClientClosed"
        CLIENT_DEAUTHED = "ClientDeauthed", "ClientDeauthed"
        CLIENT_OPENED = "ClientOpened", "ClientOpened"
        SETTINGS_UPDATED = "SettingsUpdated", "SettingsUpdated"

        USER_LOGGED_IN = "UserLoggedIn"
        USER_LOGGED_OUT = "UserLoggedOut"

        # file events
        # FILE_DESELECTED = "FileDeselected"
        # FILE_SELECTED = "FileSelected"
        # METADATA_ANALYSIS_FINISHED = "MetadataAnalysisFinished"
        # METADATA_STATISTICS_UPDATED = "MetadataStatisticsUpdated"
        FILE_ADDED = "FileAdded", "FileAdded"
        FILE_REMOVED = "FileRemoved", "FileRemoved"
        FOLDER_ADDED = "FolderAdded", "FolderAdded"
        FOLDER_REMOVED = "FolderRemoved", "FolderRemoved"
        TRANSFER_DONE = "TransferDone", "TransferDone"
        TRANSFER_FAILED = "TransferFailed", "TransferFailed"
        TRANSFER_STARTED = "TransferStarted", "TransferStarted"
        UPDATED_FILES = "UpdatedFiles", "UpdatedFiles"
        UPLOAD = "Upload", "Upload"

        # timelapse
        CAPTURE_DONE = "CaptureDone", "CaptureDone"
        CAPTURE_FAILED = "CaptureFailed", "CaptureFailed"
        CAPTURE_START = "CaptureStart", "CaptureStart"
        MOVIE_DONE = "MovieDone", "MovieDone"
        MOVIE_FAILED = "MovieFailed", "MovieFailed"
        MOVIE_RENDERING = "MovieRendering", "MovieRendering"
        POSTROLL_END = "PostRollEnd", "PostRollEnd"
        POSTROLL_START = "PostRollStart", "PostRollStart"

        # slicer
        SLICING_CANCELLED = "SlicingCancelled", "SlicingCancelled"
        SLICING_DONE = "SlicingDone", "SlicingDone"
        SLICING_FAILED = "SlicingFailed", "SlicingFailed"
        SLICING_PROFILE_ADDED = "SlicingProfileAdded", "SlicingProfileAdded"
        SLICING_PROFILE_DELETED = "SlicingProfileDeleted", "SlicingProfileDeleted"
        SLICING_PROFILE_MODIFIED = "SlicingProfileModified", "SlicingProfileModified"
        SLICING_STARTED = "SlicingStarted", "SlicingStarted"

        # octoprint server <-> printer telemetry
        CONNECTED = "Connected", "Connected"
        DISCONNECTED = "Disconnected", "Disconnected"
        PRINTER_RESET = "PrinterReset", "PrinterReset"
        PRINTER_STATE_CHANGED = "PrinterStateChanged", "PrinterStateChanged"
        FIRMWARE_DATA = "FirmwareData", "FirmwareData"

        # printer profile
        PRINTER_PROFILE_ADDED = "PrinterProfileAdded", "PrinterProfileAdded"
        PRINTER_PROFILE_DELETED = "PrinterProfileDeleted", "PrinterProfileDeleted"
        PRINTER_PROFILE_MODIFIED = "PrinterProfileModified", "PrinterProfileModified"

        # print progress
        PRINT_PROGRESS = "PrintProgress", "PrintProgress"

        # pi throttle state
        # @todo (not sure why this event is formatted different by octoprint)
        PI_THROTTLE_STATE = (
            "plugin_pi_support_throttle_state",
            "plugin_pi_support_throttle_state",
        )

        # octoprint server
        # CONNECTIVITY_CHANGED = "ConnectivityChanged"
        SHUTDOWN = "Shutdown", "Shutdown"
        STARTUP = "Startup", "Startup"

    event_codes = [x.value for x in EventType.__members__.values()]
    event_type = models.CharField(
        max_length=255, db_index=True, choices=EventType.choices
    )
    print_session = models.ForeignKey(
        "remote_control.PrintSession",
        null=True,
        on_delete=models.CASCADE,
        db_index=True,
    )


class PrintStatusEvent(TelemetryEvent):
    class EventType(models.TextChoices):
        # print job
        ERROR = "Error", "Error"
        PRINT_CANCELLED = "PrintCancelled", "PrintCancelled"
        PRINT_CANCELLING = "PrintCancelling", "PrintCancelling"
        PRINT_DONE = "PrintDone", "PrintDone"
        PRINT_FAILED = "PrintFailed", "PrintFailed"
        PRINT_PAUSED = "PrintPaused", "PrintPaused"
        PRINT_RESUMED = "PrintResumed", "PrintResumed"
        PRINT_STARTED = "PrintStarted", "PrintStarted"

    event_codes = [x.value for x in EventType.__members__.values()]
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
        max_length=255, db_index=True, choices=EventType.choices
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
