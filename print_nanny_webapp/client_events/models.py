from django.contrib.auth import get_user_model
from django.db import models
from django.apps import apps
from django.utils import timezone

from urllib.parse import urljoin
from django.contrib.postgres.fields import ArrayField
from django.contrib.sites.shortcuts import get_current_site
from print_nanny_webapp.remote_control.models import PrintJob

User = get_user_model()


class PredictSession(models.Model):
    created_dt = models.DateTimeField(db_index=True, auto_now_add=True)
    closed_dt = models.DateTimeField(db_index=True, auto_now=True)
    closed = models.BooleanField(default=False)
    channel_name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True)


class ObjectDetectEvent(models.Model):
    '''
        prev: ObjectDetectEvent

    '''

    created_dt = models.DateTimeField(db_index=True, auto_now=True)
    gcs_path = models.CharField(max_length=255, null=True, db_index=True)
    predict_session = models.ForeignKey(
        PredictSession, on_delete=models.CASCADE, db_index=True
    )
    print_job = models.ForeignKey(PrintJob, on_delete=models.CASCADE, null=True, db_index=True)



class OctoPrintEvent(models.Model):
    class EventTypeChoices(models.TextChoices):
        # OctoPrint javascript client / browser -> OctoPrint server (not Print Nanny webapp)
        CLIENT_AUTHED = "ClientAuthed", "ClientAuthed"
        CLIENT_CLOSED = "ClientClosed", "ClientClosed"
        CLIENT_DEAUTHED = "ClientDeauthed", "ClientDeauthed"
        CLIENT_OPENED = "ClientOpened", "ClientOpened"
        SETTINGS_UPDATED = "SettingsUpdated", "SettingsUpdated"
        # USER_LOGGED_IN = "UserLoggedIn"
        # USER_LOGGED_OUT = "UserLoggedOut"

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

        # octoprint server <-> printer
        CONNECTED = "Connected", "Connected"
        DISCONNECTED = "Disconnected", "Disconnected"
        PRINTER_RESET = "PrinterReset", "PrinterReset"

        # printer profile
        PRINTER_PROFILE_ADDED = "PrinterProfileAdded", "PrinterProfileAdded"
        PRINTER_PROFILE_DELETED = "PrinterProfileDeleted", "PrinterProfileDeleted"
        PRINTER_PROFILE_MODIFIED = "PrinterProfileModified", "PrinterProfileModified"

        # print job
        ERROR = "Error", "Error"
        PRINT_CANCELLED = "PrintCancelled", "PrintCancelled"
        PRINT_CANCELLING = "PrintCancelling", "PrintCancelling"
        PRINT_DONE = "PrintDone", "PrintDone"
        PRINT_FAILED = "PrintFailed", "PrintFailed"
        PRINT_PAUSED = "PrintPaused", "PrintPaused"
        PRINT_RESUMED = "PrintResumed", "PrintResumed"
        PRINT_STARTED = "PrintStarted", "PrintStarted"

        # octoprint server
        # CONNECTIVITY_CHANGED = "ConnectivityChanged"
        SHUTDOWN = "Shutdown", "Shutdown"
        STARTUP = "Startup", "Startup"

    dt = models.DateTimeField(db_index=True)
    event_type = models.CharField(
        max_length=30, db_index=True, choices=EventTypeChoices.choices
    )
    event_data = models.JSONField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True, null=True)
    plugin_version = models.CharField(max_length=30)
    octoprint_version = models.CharField(max_length=30)
    print_job = models.ForeignKey(
        PrintJob, null=True, on_delete=models.CASCADE, db_index=True
    )
