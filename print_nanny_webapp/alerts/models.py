import os
import logging

from django.contrib.auth import get_user_model
from django.db import models
from django.apps import apps
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone, dateformat
from django.utils.text import capfirst
from polymorphic.models import PolymorphicModel
from polymorphic.managers import PolymorphicManager

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

    alert_type = models.CharField(choices=AlertTypeChoices.choices, max_length=255)

    created_dt = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_dt = models.DateTimeField(auto_now=True, db_index=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True)
    seen = models.BooleanField(default=False)
    dismissed = models.BooleanField(default=False)


class AlertSettings(PolymorphicModel):
    class AlertMethodChoices(models.TextChoices):
        UI = "UI", "Recive Print Nanny UI notifations"
        EMAIL = "EMAIL", "Receive email notifications"

    created_dt = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_dt = models.DateTimeField(auto_now=True, db_index=True)

    alert_type = models.CharField(
        choices=Alert.AlertTypeChoices.choices, max_length=255
    )
    alert_methods = ChoiceArrayField(
        models.CharField(choices=AlertMethodChoices.choices, max_length=255),
        blank=True,
        default=(AlertMethodChoices.UI,),
    )
    enabled = models.BooleanField(
        default=True, help_text="Enable or disable this alert channel"
    )


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
        RemoteControlCommand = apps.get_model('remote_control', 'RemoteControlCommand')

        progress = octoprint_event.event_data.get('progress')
        if progress % self.on_progress_percent == 0:
            command = RemoteControlCommand.objects.create(
                command=RemoteControlCommand.SNAPSHOT,
                device=octoprint_event.octoprint_device,
                user=octoprint_event.user,
            )
            logger.info(f'ProgressAlertSettings.on_print_progress issued command {command.__dict__}')

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
        snake_cased = ''.join(['_'+i.lower() if i.isupper()  
               else i for i in command_str]).lstrip('_')
        return getattr(self, snake_cased)


    user = models.OneToOneField(User, on_delete=models.CASCADE)

    snapshot = ChoiceArrayField(
        models.CharField(max_length=255, choices=AlertSubTypeChoices.choices),
        help_text="Fires on web camera <strong>Snapshot</strong> command",
        default=(AlertSubTypeChoices.FAILED,AlertSubTypeChoices.SUCCESS),
        blank=True,
    )

    stop_monitoring = ChoiceArrayField(
        models.CharField(max_length=255, choices=AlertSubTypeChoices.choices),
        help_text="Fires on <strong>StopMonitoring<strong> updates. \n Helps debug unexpected Print Nanny crashes.",
        blank=True,
        default=(AlertSubTypeChoices.FAILED,),
    )

    start_monitoring = ChoiceArrayField(
        models.CharField(max_length=255, choices=AlertSubTypeChoices.choices),
        help_text="Fires on <strong>StopMonitoring</strong> updates. Helpful if you want to confirm monitoring started without a problem.",
        blank=True,
        default=(AlertSubTypeChoices.FAILED,),
    )

    stop_print = ChoiceArrayField(
        models.CharField(max_length=255, choices=AlertSubTypeChoices.choices),
        help_text="Fires on <strong>StopPrint</strong> updates. Get notifed as soon as a print job finishes. ",
        blank=True,
        default=(AlertSubTypeChoices.FAILED,),
    )

    start_print = ChoiceArrayField(
        models.CharField(max_length=255, choices=AlertSubTypeChoices.choices),
        help_text="Fires on <strong>SartPrint</strong> command status changes. Helpful for verifying a print job started without a problem.",
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


class RemoteControlCommandAlert(models.Manager):
    def create(self, *args, **kwargs):
        instance = super().create(*args, **kwargs)
        
        alert_settings = RemoteControlCommandAlertSettings(user=instance.user)
        alert_settings_attr = alert_settings.command_to_attr(instance.command.command)
        if instance.alert_subtype in alert_settings_attr:
            instance.send_alerts(alert_settings.alert_methods)
        return instance

class RemoteControlCommandAlert(Alert):
    """
    Fires on remote control events
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, alert_type=Alert.AlertTypeChoices.COMMAND, **kwargs)

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


# ManualVideoUploadAlert._meta.get_field('alert_type').default = Alert.AlertTypeChoices.MANUAL_VIDEO_UPLOAD
# class DefectAlert(Alert):
#     print_job = models.ForeignKey(
#         "remote_control.PrintJob", on_delete=models.CASCADE, db_index=True
#     )

#     class ActionChoices(models.TextChoices):
#         PENDING = "PENDING", "Pending User Action"
#         RESUME_ALERTS = "RESUME_ALERTS", "Resume for Print Job"
#         CANCEL_PRINT = "CANCEL_PRINT", "Cancel Print Job Cancel"

#     last_action = models.CharField(
#         max_length=16, choices=ActionChoices.choices, default=ActionChoices.PENDING
#     )
#     tags = ArrayField(models.CharField(max_length=255), default=list(["defect-alert"]))

#     def source_display_name(self):
#         return f"Print Job {self.print_job.id}"


# class ProgressAlert(Alert):
#     class Meta:
#         unique_together = ("print_job_id", "progress")

#     print_job = models.ForeignKey(
#         "remote_control.PrintJob", on_delete=models.CASCADE, db_index=True
#     )
#     progress = models.IntegerField(default=0)

#     tags = ArrayField(
#         models.CharField(max_length=255), default=list(["progress-alert"])
#     )


class AlertPlot(models.Model):
    image = models.ImageField(upload_to=_upload_to)
    html = models.FileField(upload_to=_upload_to)
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=255)
    function = models.CharField(max_length=65)
    alert = models.ForeignKey(ManualVideoUploadAlert, on_delete=models.CASCADE)
