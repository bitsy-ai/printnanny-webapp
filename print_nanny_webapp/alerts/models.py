from django.contrib.auth import get_user_model
from django.db import models
from django.apps import apps
from django.contrib.postgres.fields import ArrayField

from print_nanny_webapp.remote_control.models import PrintJob

User = get_user_model()


class AlertMessage(models.Model):
    """
        outgoing message to user
    """

    # action_basename = 'feedback'
    class Backend(models.TextChoices):
        EMAIL = 'EMAIL', 'Email'
    
    class ActionChoices(models.TextChoices):
        PENDING = 'PENDING', 'Pending User Action'
        RESUME_ALERTS = 'RESUME_ALERTS', 'Resume for Print Job'
        CANCEL_PRINT = 'CANCEL_PRINT', 'Cancel Print Job Cancel'
    
    created_dt = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_dt = models.DateTimeField(auto_now=True, db_index=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True)
    
    print_job = models.ForeignKey(PrintJob, on_delete=models.CASCADE, db_index=True)
    video = models.ImageField(upload_to='uploads/alert/%Y/%m/%d/')
    provider_id = models.CharField(max_length=255, null=True, db_index=True)
    seen = models.BooleanField(default=False)
    last_action = models.CharField(
        max_length=16,
        choices=ActionChoices.choices,
        default=ActionChoices.PENDING
    )

    tags = ArrayField(
        models.CharField(max_length=255),
        default=list(["default-alert-message"])
    )

    dataframe = models.JSONField()

class AlertEvent(models.Model):
    """
        inbound alert events, like open and click on an email
    """

    class AnymailStatusChoices(models.TextChoices):
        DELIVERED = 'DELIEVERED', 'Delivered'
        REJECTED = 'REJECTED', 'Rejected'
        BOUNCED = 'BOUNCED', 'Bounced',
        COMPLAINED = 'COMPLAINED','Complained',
        UNSUBSCRIBED = 'UNSUBSCRIBED', 'Unsubscribed'
        OPENED = 'OPENED', 'Opened',
        CLICKED = 'CLICKED', 'Clicked'

    event_type = models.CharField(
        max_length=12,
        choices=AnymailStatusChoices.choices,
    )
    dt = models.DateTimeField(db_index=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True)
    alert_message = models.ForeignKey(AlertMessage, on_delete=models.CASCADE)
    provider_id = models.CharField(max_length=255)
    event_data = models.JSONField()
