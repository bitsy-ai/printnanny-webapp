import os
import logging
import asyncio

from django.contrib.auth import get_user_model
from django.db import models
from django.apps import apps
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings
from django.contrib.postgres.fields import ArrayField
from django.template.loader import render_to_string
from django.utils import timezone, dateformat
from django.utils.text import capfirst
from polymorphic.models import PolymorphicModel
from polymorphic.managers import PolymorphicManager
from channels.layers import get_channel_layer
from rest_framework.renderers import JSONRenderer
from anymail.message import AnymailMessage
from asgiref.sync import async_to_sync
from django.urls import reverse
import stringcase

from django.contrib.postgres.fields import JSONField

from print_nanny_webapp.utils.fields import ChoiceArrayField
from print_nanny_webapp.alerts.tasks.common import trigger_alerts_task


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
    class EventType(models.TextChoices):
        PRINT_HEALTH = "PrintHealth", "Print health alerts"
        PRINT_STATUS = (
            "PrintStatus",
            "Print status updates (started, percent progress, paused, resumed, cancelling, cancelled, failed, done)",
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
        models.CharField(choices=EventType.choices, max_length=255),
        blank=True,
        default=(
            EventType.PRINT_HEALTH,
            EventType.PRINT_STATUS,
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

    def on_print_progress(self, octoprint_event):
        from print_nanny_webapp.alerts.api.serializers import AlertSerializer

        progress = octoprint_event.event_data.get("event_data").get("progress")
        if progress % self.on_progress_percent == 0:
            serialized_obj = ProgressAlertSerializer(self)
            return self.trigger_alerts_task(serialized_obj)


class AlertEventTypes(models.TextChoices):
    VIDEO_DONE = "VideoDone", "VideoDone"
    PRINT_HEALTH = "PrintHealth", "PrintHealth"
    PRINT_PROGRESS = "PrintProgress", "PrintProgress"
    PRINT_DONE = "PrintDone", "PrintDone"
    PRINT_FAILED = "PrintFailed", "PrintFailed"
    PRINT_PAUSED = "PrintPaused", "PrintPaused"
    PRINT_RESUMED = "PrintResumed", "PrintResumed"
    PRINT_STARTED = "PrintStarted", "PrintStarted"

    @classmethod
    def from_flatbuffer_event_type(cls, event_type):
        """
            flatbuffer generated enum

        class AlertEventTypeEnum(object):
            print_health = 0
            print_progress = 1
            print_done = 2
            print_failed = 3
            print_paused = 4
            print_resumed = 5
            print_started = 6
            video_done = 7


        """
        from print_nanny_client.alerts import AlertEventTypeEnum
        name = stringcase.AlertEventTypeEnum(event_type).name
        return cls(stringcase.uppercase(name))

class AlertMessage(models.Model):
    """
    Base class for alert events
    """

    alert_method = models.CharField(
        choices=AlertSettings.AlertMethod.choices,
        max_length=255,
    )
    event_type = models.CharField(
        choices=AlertEventTypes.choices, max_length=255, null=True
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
