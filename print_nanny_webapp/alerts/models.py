import os
import logging

from django.contrib.auth import get_user_model
from django.db import models
from django.apps import apps
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone, dateformat
from polymorphic.models import PolymorphicModel

User = get_user_model()
logger = logging.getLogger(__name__)


def _upload_to(instance, filename):
    datesegment = dateformat.format(timezone.now(), "Y/M/d/")
    path = os.path.join(f"uploads/{instance.__class__.__name__}", datesegment, filename)
    logger.info("Uploading to path")
    return path

class Alert(PolymorphicModel):

    class AlertTypeChoices(models.TextChoices):
        COMMAND = "COMMAND", "Remote control command alerts (received, success, error)"
        MANUAL_VIDEO_UPLOAD = "MANUAL_VIDEO_UPLOAD", "Manually-uploaded video is ready for review"
    created_dt = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_dt = models.DateTimeField(auto_now=True, db_index=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True)
    dismissed = models.BooleanField(default=True)

    @property
    def alert_type(self):
        return "ALERT"

class RemoteControlCommandAlert(Alert):

    class AlertSubtypeChoices(models.TextChoices):
        RECEIVED = "RECEIVED", "Command was received by Raspberry Pi"
        SUCCESS = "SUCCESS", "Command succeeded"
        FAILED = "FAILED", "Command failed" 
    

    ACTION_CSS_CLASSES = {
        AlertSubtypeChoices.RECEIVED: "info",
        AlertSubtypeChoices.SUCCESS: "success",
        AlertSubtypeChoices.FAILED: "danger",
    }
    command = models.ForeignKey('remote_control.RemoteControlCommand', on_delete=models.CASCADE)
    alert_subtype = models.CharField(max_length=255, choices=AlertSubtypeChoices.choices)

    @property
    def css_class(self):
        return self.ACTION_CSS_CLASSES[self.alert_subtype]

    @property
    def alert_type(self):
        return Alert.AlertTypeChoices.COMMAND

    @classmethod
    def get_alert_type(self, remote_control_command_data):
        keys = remote_control_command_data.keys()
        if 'received' in keys:
            return self.AlertSubtypeChoices.RECEIVED
        if 'success' in keys:
            if remote_control_command_data.get('success') == True:
                return self.AlertSubtypeChoices.SUCCESS
            elif remote_control_command_data.get('success') == False:
                return self.AlertSubtypeChoices.FAILED
        


class ManualVideoUploadAlert(Alert):
    """
        Base class for a prediction alert .gif or timelapse mp4 / mjpeg
    """

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

    @property
    def alert_type(self):
        return Alert.AlertTypeChoices.MANUAL_VIDEO_UPLOAD

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


# class AlertEvent(models.Model):
#     """
#         inbound alert events, like open and click on an email
#     """

#     class AnymailStatusChoices(models.TextChoices):
#         DELIVERED = 'DELIEVERED', 'Delivered'
#         REJECTED = 'REJECTED', 'Rejected'
#         BOUNCED = 'BOUNCED', 'Bounced',
#         COMPLAINED = 'COMPLAINED','Complained',
#         UNSUBSCRIBED = 'UNSUBSCRIBED', 'Unsubscribed'
#         OPENED = 'OPENED', 'Opened',
#         CLICKED = 'CLICKED', 'Clicked'

#     event_type = models.CharField(
#         max_length=12,
#         choices=AnymailStatusChoices.choices,
#     )
#     dt = models.DateTimeField(db_index=True)
#     user = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True)
#     alert_message = models.ForeignKey(ManualVideoUploadAlert, on_delete=models.CASCADE)
#     provider_id = models.CharField(max_length=255)
#     event_data = models.JSONField()
