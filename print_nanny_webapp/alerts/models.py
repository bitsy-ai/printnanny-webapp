import os 
import logging

from django.contrib.auth import get_user_model
from django.db import models
from django.apps import apps
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone, dateformat
from polymorphic.models import PolymorphicModel

from print_nanny_webapp.remote_control.models import PrintJob

User = get_user_model()
logger = logging.getLogger(__name__)

def _upload_to(instance, filename):
    datesegment = dateformat.format(timezone.now(), 'Y/M/d/')
    path = os.path.join(
        f'uploads/{instance.__class__.__name__}',
        datesegment,
        filename
    )
    logger.info('Uploading to path')
    return path
 

class AlertVideoMessage(PolymorphicModel):
    '''
        Base class for a prediction alert .gif or timelapse mp4 / mjpeg
    '''
    # class SourceChoices(models.TextChoices):
    #     WEB_UPLOAD = 'WEB_UPLOAD', 'Uploaded manually'
    #     OCTOPRINT = 'OCTOPRINT', 'Sent by OctoPrint'
    
    # source = models.CharField(max_length=32, choices=SourceChoices.choices)
    class JobStatusChoices(models.TextChoices):
        PROCESSING = 'Processing', 'Processing'
        SUCCESS = 'SUCCESS', 'Success'
        FAILURE = 'FAILURE', 'Failure'
        CANCELLED = 'CANCELLED', 'Cancelled'

    class Backend(models.TextChoices):
        EMAIL = 'EMAIL', 'Email'

    provider_id = models.CharField(max_length=255, null=True, db_index=True)
    seen = models.BooleanField(default=False)

    job_status = models.CharField(max_length=32, choices=JobStatusChoices.choices, default=JobStatusChoices.PROCESSING)
    created_dt = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_dt = models.DateTimeField(auto_now=True, db_index=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True)
    dataframe = models.FileField(upload_to=_upload_to, null=True)    
    original_video = models.FileField(upload_to=_upload_to, null=True)
    annotated_video = models.FileField(upload_to=_upload_to, null=True)

    feedback = models.BooleanField(null=True)
    length = models.FloatField(null=True)
    fps = models.FloatField(null=True)

    notify_seconds = models.IntegerField(null=True)
    notify_timecode = models.CharField(max_length=32, null=True)

    def original_filename(self):
        return os.path.basename(self.original_video.name)
    
    def annotated_video_url(self):
        logger.info(self.original_video)
        logger.info(self.annotated_video)
        # if self.annotated_video is not None:
        #     return self.annotated_video.storage.url(
        #         self.annotated_video.name
        #     )



class DefectAlert(AlertVideoMessage):
    print_job = models.ForeignKey(PrintJob, on_delete=models.CASCADE, db_index=True)

    class ActionChoices(models.TextChoices):
        PENDING = 'PENDING', 'Pending User Action'
        RESUME_ALERTS = 'RESUME_ALERTS', 'Resume for Print Job'
        CANCEL_PRINT = 'CANCEL_PRINT', 'Cancel Print Job Cancel'
    last_action = models.CharField(
        max_length=16,
        choices=ActionChoices.choices,
        default=ActionChoices.PENDING
    )
    tags = ArrayField(
        models.CharField(max_length=255),
        default=list(["defect-alert"])
    )
    def source_display_name(self):
        return f'Print Job {self.print_job.id}'

class ProgressAlert(AlertVideoMessage):

    class Meta:
        unique_together = ('print_job_id', 'progress')

    print_job = models.ForeignKey(PrintJob, on_delete=models.CASCADE, db_index=True)
    progress = models.IntegerField(default=0)

    tags = ArrayField(
        models.CharField(max_length=255),
        default=list(["progress-alert"])
    )



class TimelapseAlert(AlertVideoMessage):
    """
        outgoing message to user indicating timelapse video is done
    """
    tags = ArrayField(
        models.CharField(max_length=255),
        default=list(["timelapse-alert"])
    )
    def source_display_name(self):
        return 'Web Upload'

class AlertPlot(models.Model):
    image = models.ImageField(upload_to=_upload_to)
    html = models.FileField(upload_to=_upload_to)
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=255)
    function = models.CharField(max_length=65)
    alert = models.ForeignKey(AlertVideoMessage, on_delete=models.CASCADE)

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
#     alert_message = models.ForeignKey(AlertVideoMessage, on_delete=models.CASCADE)
#     provider_id = models.CharField(max_length=255)
#     event_data = models.JSONField()
