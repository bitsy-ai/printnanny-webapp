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

import stringcase

from print_nanny_webapp.utils.fields import ChoiceArrayField

User = get_user_model()
logger = logging.getLogger(__name__)


def _upload_to(instance, filename):
    datesegment = dateformat.format(timezone.now(), "Y/M/d/")
    path = os.path.join(f"uploads/{instance.__class__.__name__}", datesegment, filename)
    logger.info("Uploading to path")
    return path


##
# Base Polymorphic models
##


class Alert(PolymorphicModel):

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

    class AlertTypeChoices(models.TextChoices):
        COMMAND = "COMMAND", "Remote command status updates"
        PROGRESS = "PRINT_PROGRESS", "Percentage-based print progress"
        MANUAL_VIDEO_UPLOAD = (
            "MANUAL_VIDEO_UPLOAD",
            "Manually-uploaded video is ready for review",
        )
        DEFECT = "DEFECT", "Defect detected in print"

    class AlertMethodChoices(models.TextChoices):
        UI = "UI", "Receive Print Nanny UI notifications"
        EMAIL = "EMAIL", "Receive email notifications"
        DISCORD = "DISCORD", "Receive notifications through Discord"

    alert_method = models.CharField(choices=AlertMethodChoices.choices, max_length=255)
    alert_type = models.CharField(choices=AlertTypeChoices.choices, max_length=255)

    created_dt = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_dt = models.DateTimeField(auto_now=True, db_index=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True)
    seen = models.BooleanField(default=False)
    dismissed = models.BooleanField(default=False)


class AlertSettings(PolymorphicModel):

    created_dt = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_dt = models.DateTimeField(auto_now=True, db_index=True)

    alert_type = models.CharField(
        choices=Alert.AlertTypeChoices.choices, max_length=255
    )
    alert_methods = ChoiceArrayField(
        models.CharField(choices=Alert.AlertMethodChoices.choices, max_length=255),
        blank=True,
        default=(Alert.AlertMethodChoices.UI,),
    )
    enabled = models.BooleanField(
        default=True, help_text="Enable or disable this alert channel"
    )


##
# Method Settings models
##


class DiscordMethodSettings(models.Model):
    class TargetIDTypeChoices(models.TextChoices):
        USER = "USER", "User"
        CHANNEL = "CHANNEL", "Channel"

    created_dt = models.DateTimeField(auto_now_add=True)
    updated_dt = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True)

    # Channel ID is where to send a message if you're not going for event-driven
    # Channel IDs are of "snowflake" type
    # Snowflakes are 64 bit unsigned integers represented as decimal strings
    # so max 21 characters - 24 to be "safe"
    # https://discord.com/developers/docs/reference#snowflakes
    # TODO: Add a label with capital 'ID'. `label` kwarg is not recognized?
    target_id = models.CharField(
        help_text="ID to send notifications to\nTo get an item's ID, enable developer mode on under Discord Settings -> Appearance and right click to the target it (ex. a channel or a user) and \"Copy ID\"",
        max_length=24, db_index=True)
    target_id_type = models.CharField(max_length=255, choices=TargetIDTypeChoices.choices, db_index=True)


##
# Alert Settings models
##


class ProgressAlertSettings(AlertSettings):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, alert_type=Alert.AlertTypeChoices.PROGRESS, **kwargs)

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    on_progress_percent = models.IntegerField(
        default=25,
        validators=[MinValueValidator(1), MaxValueValidator(100)],
        help_text="Progress notification interval. Example: 25 will notify you at 25%, 50%, 75%, and 100% progress",
    )

    def on_print_progress(self, octoprint_event):
        RemoteControlCommand = apps.get_model("remote_control", "RemoteControlCommand")

        progress = octoprint_event.event_data.get("event_data").get("progress")
        if progress % self.on_progress_percent == 0:
            command = RemoteControlCommand.objects.create(
                command=RemoteControlCommand.CommandChoices.SNAPSHOT,
                device=octoprint_event.device,
                user=octoprint_event.user,
            )
            logger.info(
                f"ProgressAlertSettings.on_print_progress issued command id={command.id}"
            )


class DefectAlertSettings(AlertSettings):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, alert_type=Alert.AlertTypeChoices.DEFECT, **kwargs)


class RemoteControlCommandAlertSettings(AlertSettings):
    class AlertSubTypeChoices(models.TextChoices):
        RECEVIED = "RECEIVED", "Command was acknowledged by device"
        FAILED = "FAILED", "Command failed"
        SUCCESS = "SUCCESS", "Command succeeded"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, alert_type=Alert.AlertTypeChoices.COMMAND, **kwargs)

    def command_to_attr(self, command_str):
        # shamelessly ripped from https://www.geeksforgeeks.org/python-program-to-convert-camel-case-string-to-snake-case/
        snake_cased = stringcase.snakecase(command_str)
        return getattr(self, snake_cased)

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    snapshot = ChoiceArrayField(
        models.CharField(max_length=255, choices=AlertSubTypeChoices.choices),
        help_text="Fires on web camera <strong>Snapshot</strong> command",
        default=(AlertSubTypeChoices.FAILED, AlertSubTypeChoices.SUCCESS),
        blank=True,
    )

    stop_monitoring = ChoiceArrayField(
        models.CharField(max_length=255, choices=AlertSubTypeChoices.choices),
        help_text="Fires on <strong>MonitoringStop<strong> updates. \n Helps debug unexpected Print Nanny crashes.",
        blank=True,
        default=(AlertSubTypeChoices.FAILED,),
    )

    start_monitoring = ChoiceArrayField(
        models.CharField(max_length=255, choices=AlertSubTypeChoices.choices),
        help_text="Fires on <strong>MonitoringStop</strong> updates. Helpful if you want to confirm monitoring started without a problem.",
        blank=True,
        default=(AlertSubTypeChoices.FAILED,),
    )

    stop_print = ChoiceArrayField(
        models.CharField(max_length=255, choices=AlertSubTypeChoices.choices),
        help_text="Fires on <strong>StopPrint</strong> updates. Get notified as soon as a print job finishes. ",
        blank=True,
        default=(AlertSubTypeChoices.FAILED,),
    )

    start_print = ChoiceArrayField(
        models.CharField(max_length=255, choices=AlertSubTypeChoices.choices),
        help_text="Fires on <strong>PrintStart</strong> command status changes. Helpful for verifying a print job started without a problem.",
        blank=True,
        default=(AlertSubTypeChoices.FAILED,),
    )

    move_nozzle = ChoiceArrayField(
        models.CharField(max_length=255, choices=AlertSubTypeChoices.choices),
        help_text="Fires on <strong>MoveNozzle</strong>command status changes. Helpful for debugging connectivity between Print Nanny and OctoPrint",
        blank=True,
        default=(AlertSubTypeChoices.FAILED,),
    )
    pause_print = ChoiceArrayField(
        models.CharField(max_length=255, choices=AlertSubTypeChoices.choices),
        help_text="Fires on <strong>PausePrint</strong> command status changes. Helpful for verifying a print was paused successfully.",
        default=(AlertSubTypeChoices.FAILED,),
        blank=True,
    )

    resume_print = ChoiceArrayField(
        models.CharField(max_length=255, choices=AlertSubTypeChoices.choices),
        help_text="Fires on <strong>ResumePrint</strong> command status changes Helpful for verifying a print was resumed.",
        default=(AlertSubTypeChoices.FAILED,),
        blank=True,
    )


##
# Alert Models
##


class DefectAlert(Alert):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, alert_type=Alert.AlertTypeChoices.DEFECT, **kwargs)


class ProgressAlert(Alert):
    """
    Fires on print job progress
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, alert_type=Alert.AlertTypeChoices.PROGRESS, **kwargs)

    progress_percent = models.IntegerField(
        default=25,
        validators=[MinValueValidator(1), MaxValueValidator(100)],
        help_text="Progress notification interval. Example: 25 will notify you at 25%, 50%, 75%, and 100% progress",
    )

    device = models.ForeignKey(
        "remote_control.OctoPrintDevice", on_delete=models.CASCADE
    )

    @property
    def title(self):
        unformatted = (
            f"{self.progress_percent}% complete: {capfirst(self.command.device.name)}"
        )
        return unformatted

    @property
    def description(self):
        return f"{str(self.get_alert_display())} {self.command.device.name}"

    @property
    def color(self):
        return self.COLOR_CSS[self.alert_subtype]

    @property
    def icon(self):
        return self.ICON_CSS[self.alert_subtype]


class RemoteControlCommandAlert(Alert):
    """
    Fires on remote control events
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, alert_type=Alert.AlertTypeChoices.COMMAND, **kwargs)
        self.alert_trigger_method_map = {
            Alert.AlertMethodChoices.UI: self.trigger_ui_alert,
            Alert.AlertMethodChoices.EMAIL: self.trigger_email_alert,
            Alert.AlertMethodChoices.DISCORD: self.trigger_discord_alert,
        }

    def trigger_alert(self):
        from print_nanny_webapp.alerts.api.serializers import AlertPolymorphicSerializer

        alert_serializer = AlertPolymorphicSerializer(self)
        data = alert_serializer.data
        return self.alert_trigger_method_map[self.alert_method](data)

    def trigger_ui_alert(self, data):
        channel_layer = get_channel_layer()

        # vuex namespace
        data["namespace"] = "alerts_dropdown"
        # required by websocket message handler in vue app(s)
        data["action"] = "alertMessage"

        async_to_sync(channel_layer.group_send)(
            f"alerts_{self.user.id}",
            {
                "type": "alert.message",
                # https://github.com/nathantsoi/vue-native-websocket#with-format-json-enabled
                "data": JSONRenderer().render(data),
            },
        )

    def trigger_email_alert(self, data):

        snapshot = self.command.snapshots.order_by("-created_dt").first()
        merge_data = {
            "SNAPSHOT_URL": snapshot.image.url,
            "FIRST_NAME": self.user.first_name or "Maker",
            "DEVICE_NAME": self.command.device.name,
            "COMMAND": self.command.command,
            "SUBTYPE": self.alert_subtype,
            "PROGRESS": self.command.metadata.get("progress"),
        }

        text_body = render_to_string(
            "email/remote_control_command_body.txt", merge_data
        )
        subject = render_to_string(
            "email/remote_control_command_subject.txt", merge_data
        )

        message = AnymailMessage(
            subject=subject,
            body=text_body,
            to=[self.user.email],
            tags=[
                "RemoteControlCommandAlert",
                self.command.command,
                self.alert_subtype,
                f"User:{self.user.id}",
            ],
        )
        message.send()

        return message

    def trigger_discord_alert(self, data):

        discord_settings = DiscordMethodSettings.objects.filter(user=self.user)

        channel_ids = []
        user_ids = []

        for setting in discord_settings:
            if setting.target_id_type == DiscordMethodSettings.TargetIDTypeChoices.USER:
                user_ids.append(setting.target_id)
            elif setting.target_id_type == DiscordMethodSettings.TargetIDTypeChoices.CHANNEL:
                channel_ids.append(setting.target_id)

        logger.info(f"Sending Discord alert to channels: {channel_ids} and users: {user_ids}")

        message = f"{data['title']}: {data['description']}"
        if data["snapshot_url"] is not None:
            message += "\n"+data["snapshot_url"]

        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.send)(
            "discord", {
                "type": "trigger.alert",
                "user_ids": user_ids,
                "channel_ids": channel_ids,
                "message": message,
        })

    class AlertSubtypeChoices(models.TextChoices):
        RECEIVED = "RECEIVED", "Command was received by"
        SUCCESS = "SUCCESS", "Command succeeded"
        FAILED = "FAILED", "Command failed"

    COLOR_CSS = {
        AlertSubtypeChoices.RECEIVED: "info",
        AlertSubtypeChoices.SUCCESS: "success",
        AlertSubtypeChoices.FAILED: "danger",
    }

    ICON_CSS = {
        AlertSubtypeChoices.RECEIVED: "mdi mdi-upload",
        AlertSubtypeChoices.SUCCESS: "mdi mdi-check",
        AlertSubtypeChoices.FAILED: "mdi mdi-close",
    }

    command = models.ForeignKey(
        "remote_control.RemoteControlCommand", on_delete=models.CASCADE
    )
    alert_subtype = models.CharField(
        max_length=255, choices=AlertSubtypeChoices.choices
    )

    @property
    def title(self):
        unformatted = f"{self.command.command}: {capfirst(self.command.device.name)}"
        return unformatted

    @property
    def description(self):
        return f"{str(self.get_alert_subtype_display())} {self.command.device.name}"

    @property
    def color(self):
        return self.COLOR_CSS[self.alert_subtype]

    @property
    def icon(self):
        return self.ICON_CSS[self.alert_subtype]

    @classmethod
    def get_alert_subtype(cls, remote_control_command_data):
        keys = remote_control_command_data.keys()
        if "received" in keys:
            return cls.AlertSubtypeChoices.RECEIVED
        if "success" in keys:
            if remote_control_command_data.get("success") == True:
                return cls.AlertSubtypeChoices.SUCCESS
            elif remote_control_command_data.get("success") == False:
                return cls.AlertSubtypeChoices.FAILED


class ManualVideoUploadAlert(Alert):
    """
    Base class for a prediction alert .gif or timelapse mp4 / mjpeg
    """

    def __init__(self, *args, **kwargs):
        super().__init__(
            *args, alert_type=Alert.AlertTypeChoices.MANUAL_VIDEO_UPLOAD, **kwargs
        )

    # class SourceChoices(models.TextChoices):
    #     WEB_UPLOAD = 'WEB_UPLOAD', 'Uploaded manually'
    #     OCTOPRINT = 'OCTOPRINT', 'Sent by OctoPrint'

    # source = models.CharField(max_length=32, choices=SourceChoices.choices)
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
        super().__init(*args, alert_type=Alert.AlertTypeChoices.COMMAND, **kwargs)

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

    @property
    def annotated_video_url(self):
        logger.info(self.original_video)
        logger.info(self.annotated_video)
        # if self.annotated_video is not None:
        #     return self.annotated_video.storage.url(
        #         self.annotated_video.name
        #     )


class AlertPlot(models.Model):
    image = models.ImageField(upload_to=_upload_to)
    html = models.FileField(upload_to=_upload_to)
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=255)
    function = models.CharField(max_length=65)
    alert = models.ForeignKey(ManualVideoUploadAlert, on_delete=models.CASCADE)
