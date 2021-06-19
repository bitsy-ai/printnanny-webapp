from typing import Any, Dict
import os
import logging
import asyncio

from django.contrib.auth import get_user_model
from django.db import models
from django.apps import apps
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone, dateformat
from django.template import Context, Template


from print_nanny_webapp.utils.fields import ChoiceArrayField


User = get_user_model()
logger = logging.getLogger(__name__)


def _upload_to(instance, filename):
    datesegment = dateformat.format(timezone.now(), "Y/M/d/")
    path = os.path.join(f"uploads/{instance.__class__.__name__}", datesegment, filename)
    return path


##
# Base Polymorphic models
##


class AlertSettings(models.Model):
    class AlertSettingsEventType(models.TextChoices):
        PRINT_HEALTH = "PrintHealth", "Print health alerts"
        PRINT_STATUS = (
            "PrintStatus",
            "Print status updates (percent progress, paused, resumed, failed)",
        )

    class AlertMethod(models.TextChoices):
        """
        The channels to which an alert is sent
        """

        UI = "UI", "Print Nanny UI"
        EMAIL = "EMAIL", "Email notifications"
        DISCORD = "DISCORD", "Discord channel (webhook)"
        PARTNER_3DGEEKS = (
            "PARTNER_3DGEEKS",
            "3D Geeks mobile app",
        )

    created_dt = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_dt = models.DateTimeField(auto_now=True, db_index=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    alert_methods = ChoiceArrayField(
        models.CharField(choices=AlertMethod.choices, max_length=255),
        blank=True,
        default=(AlertMethod.EMAIL,),
    )
    event_types = ChoiceArrayField(
        models.CharField(choices=AlertSettingsEventType.choices, max_length=255),
        blank=True,
        default=(
            AlertSettingsEventType.PRINT_HEALTH,
            AlertSettingsEventType.PRINT_STATUS,
        ),
    )
    discord_webhook = models.CharField(
        null=True,
        max_length=255,
        blank=True,
        help_text="Send notifications to a Discord channel. Please check out this guide to <a href='https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks'>generate a webhook</a> url and paste it here.",
    )
    print_progress_percent = models.IntegerField(
        default=25,
        validators=[MinValueValidator(1), MaxValueValidator(100)],
        help_text="Progress notification interval. Example: 25 will notify you at 25%, 50%, 75%, and 100% progress",
    )


class AlertMessage(models.Model):
    """
    Base class for alert events
    """

    class AlertMessageType(models.TextChoices):
        TEST = "Test", "Hello {{ FIRST_NAME }} 👋"
        VIDEO_DONE = "VideoDone", "{{ GCODE_FILE }} - timelapse done 🎥"
        PRINT_HEALTH = "PrintHealth", "{{ GCODE_FILE }} - job is unhealthy 😵"
        PRINT_PROGRESS = (
            "PrintProgress",
            "{{ GCODE_FILE }} - {{ PRINT_PROGRESS }}% complete ⏳",
        )
        PRINT_DONE = "PrintDone", "{{ GCODE_FILE }} - job finished ✅"
        PRINT_FAILED = "PrintFailed", "{{ GCODE_FILE }} - job failed ❌"
        PRINT_PAUSED = "PrintPaused", "{{ GCODE_FILE }} - job paused ⏸️"
        PRINT_RESUMED = "PrintResumed", "{{ GCODE_FILE }} - job resumed ⏯️"
        PRINT_STARTED = "PrintStarted", "{{ GCODE_FILE }} - job started 🏁"
        PRINT_CANCELLED = "PrintCancelled", "{{ GCODE_FILE }} - job cancelled ❌"
        SHUTDOWN = "Shutdown", "{{ DEVICE_NAME }} - OctoPrint server shutdown 😴"
        STARTUP = "Startup", "{{ DEVICE_NAME }} - OctoPrint server startup ✨"
        CONNECTED = "Connected", "{{ DEVICE_NAME }} - OctoPrint connected to printer 🔗"
        DISCONNECTED = (
            "Disconnected",
            "{{ DEVICE_NAME }} - OctoPrint disconnected from printer 💥",
        )

    @property
    def message(self) -> str:
        template = Template(self.get_event_type_display())
        merge_data: Dict[str, Any] = {
            "FIRST_NAME": self.user.first_name,  # type: ignore
            "EMAIL": self.user.email,
        }
        if self.octoprint_device:
            merge_data.update({"DEVICE_NAME": self.octoprint_device.name})

        if self.print_session:
            merge_data.update(
                {
                    "PRINT_SESSION": self.print_session.session,
                    "GCODE_FILE": self.print_session.gcode_file,
                }
            )
        ctx = Context(merge_data)
        return template.render(ctx)

    alert_method = models.CharField(
        choices=AlertSettings.AlertMethod.choices,
        max_length=255,
    )
    event_type = models.CharField(
        choices=AlertMessageType.choices, max_length=255, null=True
    )
    event = models.ForeignKey(
        "telemetry.TelemetryEvent", on_delete=models.CASCADE, null=True
    )
    print_session = models.ForeignKey(
        "remote_control.PrintSession", on_delete=models.CASCADE, null=True
    )
    annotated_video = models.FileField(upload_to=_upload_to, null=True)

    created_dt = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_dt = models.DateTimeField(auto_now=True, db_index=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True)
    seen = models.BooleanField(default=False)
    sent = models.BooleanField(default=False)
    octoprint_device = models.ForeignKey(
        "remote_control.OctoPrintDevice", null=True, on_delete=models.CASCADE
    )
    needs_review = models.BooleanField(default=False)


##
# @ todo re-enable ManualVideoUpload feature
##

# class ManualVideoUploadAlert(Alert):
#     """
#     Base class for a prediction alert .gif or timelapse mp4 / mjpeg
#     """

#     def __init__(self, *args, **kwargs):
#         super().__init__(
#             *args, alert_type=Alert.AlertTypeChoices.MANUAL_VIDEO_UPLOAD, **kwargs
#         )

#     class JobStatusChoices(models.TextChoices):
#         PROCESSING = "Processing", "Processing"
#         SUCCESS = "SUCCESS", "Success"
#         FAILURE = "FAILURE", "Failure"
#         CANCELLED = "CANCELLED", "Cancelled"

#     class Backend(models.TextChoices):
#         EMAIL = "EMAIL", "Email"

#     job_status = models.CharField(
#         max_length=32,
#         choices=JobStatusChoices.choices,
#         default=JobStatusChoices.PROCESSING,
#     )

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, alert_type=Alert.AlertTypeChoices.COMMAND, **kwargs)

#     dataframe = models.FileField(upload_to=_upload_to, null=True)
#     original_video = models.FileField(upload_to=_upload_to, null=True)
#     annotated_video = models.FileField(upload_to=_upload_to, null=True)

#     feedback = models.BooleanField(null=True)
#     length = models.FloatField(null=True)
#     fps = models.FloatField(null=True)

#     notify_seconds = models.IntegerField(null=True)
#     notify_timecode = models.CharField(max_length=32, null=True)

#     @property
#     def original_filename(self):
#         return os.path.basename(self.original_video.name)


# class AlertPlot(models.Model):
#     image = models.ImageField(upload_to=_upload_to)
#     html = models.FileField(upload_to=_upload_to)
#     title = models.CharField(max_length=65)
#     description = models.CharField(max_length=255)
#     function = models.CharField(max_length=65)
#     alert = models.ForeignKey(ManualVideoUploadAlert, on_delete=models.CASCADE)
