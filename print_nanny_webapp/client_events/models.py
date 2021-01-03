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

from django.apps import apps
from django.conf import settings
from django.core.files.base import ContentFile
from django.contrib.postgres.fields import ArrayField, JSONField
from django.contrib.sites.shortcuts import get_current_site

User = get_user_model()
logger = logging.getLogger(__name__)


class OctoPrintEventTypeChoices(models.TextChoices):
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


class ObjectDetectEventImage(models.Model):
    created_dt = models.DateTimeField()
    uuid = models.CharField(max_length=255, db_index=True)
    user = models.ForeignKey(User, db_index=True, on_delete=models.CASCADE)
    original_image = models.ImageField(
        upload_to="uploads/predict_event_original_image/%Y/%m/%d/"
    )
    annotated_image = models.ImageField(
        upload_to="uploads/predict_annotated_image/%Y/%m/%d/"
    )


class OctoPrintEvent(models.Model):

    created_dt = models.DateTimeField(db_index=True)
    event_type = models.CharField(
        max_length=255, db_index=True, choices=OctoPrintEventTypeChoices.choices
    )
    event_data = models.JSONField()
    device = models.ForeignKey(
        "remote_control.OctoPrintDevice", db_index=True, on_delete=models.CASCADE
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True)
    plugin_version = models.CharField(max_length=60)
    octoprint_version = models.CharField(max_length=60)


class PrintJobEventTypeChoices(models.TextChoices):
    # print job
    ERROR = "Error", "Error"
    PRINT_CANCELLED = "PrintCancelled", "PrintCancelled"
    PRINT_CANCELLING = "PrintCancelling", "PrintCancelling"
    PRINT_DONE = "PrintDone", "PrintDone"
    PRINT_FAILED = "PrintFailed", "PrintFailed"
    PRINT_PAUSED = "PrintPaused", "PrintPaused"
    PRINT_RESUMED = "PrintResumed", "PrintResumed"
    PRINT_STARTED = "PrintStarted", "PrintStarted"


OctoPrintEventCodes = [x.value for x in OctoPrintEventTypeChoices.__members__.values()]
PrintJobEventCodes = [x.value for x in PrintJobEventTypeChoices.__members__.values()]
TelemetryEventCodes = OctoPrintEventCodes + PrintJobEventCodes


class PrintJobEvent(models.Model):

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
    created_dt = models.DateTimeField(db_index=True)
    event_type = models.CharField(
        max_length=255, db_index=True, choices=PrintJobEventTypeChoices.choices
    )
    state = models.CharField(max_length=255)
    current_z = models.FloatField()
    progress = models.FloatField()
    job_data_file = models.CharField(max_length=255)

    event_data = models.JSONField()
    device = models.ForeignKey(
        "remote_control.OctoPrintDevice", db_index=True, on_delete=models.CASCADE
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True)
    print_job = models.ForeignKey(
        "remote_control.PrintJob", null=True, on_delete=models.CASCADE, db_index=True
    )

    plugin_version = models.CharField(max_length=60)
    octoprint_version = models.CharField(max_length=60)
