import os 
from django.contrib.auth import get_user_model
from django.db import models
from django.apps import apps
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone, dateformat
from polymorphic.models import PolymorphicModel

from print_nanny_webapp.remote_control.models import PrintJob

User = get_user_model()
    

class AnnotatedVideo(models.Model):
    '''
        Base class for a prediction alert .gif or timelapse mp4 / mjpeg
    '''
    def _upload_to(self, filename):
        return os.path.join(
           dateformat.format(timezone.now(), 'uploads/annotated_video/%Y/%m/%d/'),
           filename
        )
    created_dt = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_dt = models.DateTimeField(auto_now=True, db_index=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True)
    original_video = models.FileField(upload_to=_upload_to, null=True)
    annotated_video = models.FileField(upload_to=_upload_to, null=True)
    dataframe = models.JSONField(null=True)
    summary = models.JSONField(null=True)
    feedback = models.BooleanField(null=True)
    class Meta:
        abstract = True

class AlertMessage(PolymorphicModel):
    """
        outgoing message to user
    """
    # action_basename = 'feedback'
    class Backend(models.TextChoices):
        EMAIL = 'EMAIL', 'Email'

    user = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True)

    provider_id = models.CharField(max_length=255, null=True, db_index=True)
    seen = models.BooleanField(default=False)


class DefectAlert(AlertMessage, AnnotatedVideo):
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
 
    def _upload_to(self, filename):
        return os.path.join(
           dateformat.format(timezone.now(), 'uploads/defect_alert/%Y/%m/%d/'),
           filename
        )

    tags = ArrayField(
        models.CharField(max_length=255),
        default=list(["defect-alert"])
    )

class TimelapseAlert(AlertMessage, AnnotatedVideo):
    """
        outgoing message to user indicating timelapse video is done
    """
    def _upload_to(self, filename):
        return os.path.join(
           dateformat.format(timezone.now(), 'uploads/timelapse_alert/%Y/%m/%d/'),
           filename
        )
    tags = ArrayField(
        models.CharField(max_length=255),
        default=list(["timelapse-alert"])
    )

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
#     alert_message = models.ForeignKey(AlertMessage, on_delete=models.CASCADE)
#     provider_id = models.CharField(max_length=255)
#     event_data = models.JSONField()
