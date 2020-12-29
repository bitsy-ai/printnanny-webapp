import base64
import hashlib
import logging
import subprocess
import tempfile

from django.contrib.auth import get_user_model
from django.db import models
from django.apps import apps
from django.utils import timezone

from urllib.parse import urljoin
from google.cloud import iot_v1 as cloudiot_v1
from google.protobuf.json_format import MessageToDict

from django.conf import settings
from django.core.files.base import ContentFile
from django.contrib.postgres.fields import ArrayField, JSONField
from django.contrib.sites.shortcuts import get_current_site
from print_nanny_webapp.remote_control.models import PrintJob

User = get_user_model()
logger = logging.getLogger(__name__)


class OctoPrintDeviceManager(models.Manager):
    def create(self, **kwargs):

        with tempfile.TemporaryDirectory() as tmp:
            tmp_private_key_filename = f"{tmp}/rsa_private.pem"
            tmp_public_key_filename = f"{tmp}/rsa_public.pem"
            p = subprocess.run(
                [
                    "openssl",
                    "genpkey",
                    "-algorithm",
                    "RSA",
                    "-out",
                    tmp_private_key_filename,
                    "-pkeyopt",
                    "rsa_keygen_bits:2048",
                ]
            )
            logger.debug(p.stdout)
            if p.stderr:
                logger.error(p.stderr)

            p = subprocess.run(
                [
                    "openssl",
                    "rsa",
                    "-in",
                    tmp_private_key_filename,
                    "-pubout",
                    "-out",
                    tmp_public_key_filename,
                ]
            )
            logger.debug(p.stdout)
            if p.stderr:
                logger.error(p.stderr)

            p = subprocess.run(
                [
                    "openssl",
                    "sha3-512",
                    "-c",
                    tmp_public_key_filename,
                ],
                capture_output=True,
            )
            logger.debug(p.stdout)
            if p.stderr:
                logger.error(p.stderr)

            fingerprint = p.stdout
            fingerprint = fingerprint.decode().split('=')[-1]
            fingerprint = fingerprint.strip()

            client = cloudiot_v1.DeviceManagerClient()

            with open(tmp_public_key_filename) as pub_f:
                public_key_content = pub_f.read()
                public_key_file = ContentFile(public_key_content.encode())

            with open(tmp_public_key_filename) as priv_f:
                private_key_content = priv_f.read()
                private_key_file = ContentFile(private_key_content.encode())

            parent = client.registry_path(
                settings.GCP_PROJECT_ID,
                settings.GCP_CLOUD_IOT_DEVICE_REGISTRY_REGION,
                settings.GCP_CLOUD_IOT_DEVICE_REGISTRY,
            )
            serial = kwargs.get("serial")
            device_template = {
                "id": f"serial-{serial}",
                "credentials": [
                    {
                        "public_key": {
                            "format": cloudiot_v1.PublicKeyFormat.RSA_PEM,
                            "key": public_key_content,
                        }
                    }
                ],
            }

            cloudiot_device = client.create_device(
                parent=parent, device=device_template
            )

            cloudiot_device_dict = MessageToDict(cloudiot_device._pb)
            logger.info(f"iot create_device() succeeded {cloudiot_device_dict}")

            # @todo why aren't these fields uploading automagically?
            device = super().create(
                private_key=private_key_file,
                public_key=public_key_file,
                fingerprint=fingerprint,
                cloudiot_device=cloudiot_device_dict,
                cloudiot_device_num_id=cloudiot_device_dict.get("numId"),
                **kwargs,
            )
            device.private_key.save(f"{serial}_private.pem", private_key_file)
            device.public_key.save(f"{serial}_public.pem", public_key_file)
            device.save()
            return device


class OctoPrintDevice(models.Model):
    objects = OctoPrintDeviceManager()

    class Meta:
        unique_together = ("user", "serial")

    created_dt = models.DateTimeField(db_index=True, auto_now_add=True)
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True)

    private_key = models.FileField(upload_to="uploads/private_key/")
    public_key = models.FileField(upload_to="uploads/public_key/")
    fingerprint = models.CharField(max_length=255)
    cloudiot_device = JSONField()
    cloudiot_device_num_id = models.BigIntegerField()

    model = models.CharField(max_length=255)
    platform = models.CharField(max_length=255)
    cpu_flags = ArrayField(models.CharField(max_length=255))

    hardware = models.CharField(max_length=255)  # /cat/cpuinfo HARDWARE
    revision = models.CharField(max_length=255)  # /cat/cpuinfo REVISION
    serial = models.CharField(max_length=255)  # /cat/cpuinfo Serial
    cores = models.IntegerField()
    ram = models.IntegerField()

    python_version = models.CharField(max_length=255)
    pip_version = models.CharField(max_length=255)
    virtualenv = models.CharField(max_length=255)

    octoprint_version = models.CharField(max_length=255)
    plugin_version = models.CharField(max_length=255)
    print_nanny_client_version = models.CharField(max_length=255)


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
