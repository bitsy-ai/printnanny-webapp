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


class AlertEventSettings(models.Model):
    class EventType(models.TextChoices):
        PRINT_PROGRESS = "PrintProgress", "Print progress notifications"
        PRINT_HEALTH = "PrintHealth", "Print health alerts"
        PRINT_STATUS = (
            "PrintStatus",
            "Print status updates (started, paused, resumed, cancelling, cancelled, failed)",
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
            EventType.PRINT_PROGRESS,
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


class Alert(PolymorphicModel):
    """
    Base class for alert events
    """

    alert_method = models.CharField(
        choices=AlertEventSettings.AlertMethod.choices,
        max_length=255,
    )
    event_type = models.CharField(
        choices=AlertEventSettings.EventType.choices, max_length=255, null=True
    )

    created_dt = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_dt = models.DateTimeField(auto_now=True, db_index=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True)
    seen = models.BooleanField(default=False)
    sent = models.BooleanField(default=False)
    octoprint_device = models.ForeignKey(
        "remote_control.OctoPrintDevice", null=True, on_delete=models.CASCADE
    )


class PrintSessionAlert(Alert):
    class AlertSubTypeChoices(models.TextChoices):
        SUCCESS = "SUCCESS", "Print session finished successfully"
        FAILURE = "FAILURE", "Failure detected in print session"

    # TODO additional statuses here (such as unread) are possible via UniqueConstrains definitions
    # https://docs.djangoproject.com/en/3.1/ref/models/constraints/#django.db.models.UniqueConstraint
    class Meta:
        constraints = (
            models.UniqueConstraint(
                fields=["print_session", "alert_subtype"],
                name="unique_alert_type_per_print_session",
            ),
        )

    def __init__(self, *args, **kwargs):
        super().__init__(
            *args, alert_type=Alert.AlertTypeChoices.PRINT_SESSION, **kwargs
        )

    needs_review = models.BooleanField(default=False)

    alert_subtype = models.CharField(
        max_length=36,
        choices=AlertSubTypeChoices.choices,
        default=AlertSubTypeChoices.SUCCESS,
    )

    print_session = models.ForeignKey(
        "remote_control.PrintSession", on_delete=models.CASCADE
    )
    annotated_video = models.FileField(upload_to=_upload_to)

    @property
    def dashboard_url(self):
        return reverse("dashboard:videos:list")


class ManualVideoUploadAlert(Alert):
    """
    Base class for a prediction alert .gif or timelapse mp4 / mjpeg
    """

    def __init__(self, *args, **kwargs):
        super().__init__(
            *args, alert_type=Alert.AlertTypeChoices.MANUAL_VIDEO_UPLOAD, **kwargs
        )

    class JobStatusChoices(models.TextChoices):
        PROCESSING = "Processing", "Processing"
        SUCCESS = "SUCCESS", "Success"
        FAILURE = "FAILURE", "Failure"
        CANCELLED = "CANCELLED", "Cancelled"

    class Backend(models.TextChoices):
        EMAIL = "EMAIL", "Email"

    job_status = models.CharField(
        max_length=32,
        choices=JobStatusChoices.choices,
        default=JobStatusChoices.PROCESSING,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, alert_type=Alert.AlertTypeChoices.COMMAND, **kwargs)

    dataframe = models.FileField(upload_to=_upload_to, null=True)
    original_video = models.FileField(upload_to=_upload_to, null=True)
    annotated_video = models.FileField(upload_to=_upload_to, null=True)

    feedback = models.BooleanField(null=True)
    length = models.FloatField(null=True)
    fps = models.FloatField(null=True)

    notify_seconds = models.IntegerField(null=True)
    notify_timecode = models.CharField(max_length=32, null=True)

    @property
    def original_filename(self):
        return os.path.basename(self.original_video.name)


class AlertPlot(models.Model):
    image = models.ImageField(upload_to=_upload_to)
    html = models.FileField(upload_to=_upload_to)
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=255)
    function = models.CharField(max_length=65)
    alert = models.ForeignKey(ManualVideoUploadAlert, on_delete=models.CASCADE)
