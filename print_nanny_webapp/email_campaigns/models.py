from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.postgres.fields import ArrayField

from safedelete.models import SafeDeleteModel, SOFT_DELETE

from print_nanny_webapp.devices.models import UserModel
from print_nanny_webapp.email_campaigns.enum import EventType, RejectReason, SendStatus

UserModel = get_user_model()


class Campaign(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE

    created_dt = models.DateTimeField(auto_now_add=True)
    template = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    send_fn = models.CharField(max_length=255)


class EmailTrackingEvent(SafeDeleteModel):
    """
    Fields map to normalized AnymailTrackingEvent
    https://anymail.dev/en/stable/sending/tracking/#normalized-tracking-event
    """

    _safedelete_policy = SOFT_DELETE

    class Meta:
        index_together = (("campaign", "user", "event_type"),)

    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, null=True)
    email_message = models.ForeignKey(
        "email_campaigns.EmailMessage", on_delete=models.CASCADE, null=True
    )

    event_type = models.CharField(max_length=255, choices=EventType.choices)
    message_id = models.CharField(max_length=255, db_index=True)
    ts = models.DateTimeField(null=True)
    event_id = models.CharField(max_length=255, null=True)
    recipient = models.EmailField(max_length=255, null=True)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True)
    metadata = models.JSONField()
    tags = ArrayField(models.CharField(max_length=255), default=list)
    reject_reason = models.CharField(
        max_length=255, choices=RejectReason.choices, null=True
    )
    description = models.CharField(max_length=255, null=True)
    mta_response = models.CharField(max_length=255, null=True)
    user_agent = models.CharField(max_length=255, null=True)
    click_url = models.CharField(max_length=255, null=True)
    esp_event = models.JSONField(null=True)


class EmailMessage(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE

    class Meta:
        index_together = (("campaign", "user", "email", "message_id"),)

    message_id = models.CharField(
        max_length=255, null=True
    )  # may be null if message send failed
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True)
    email = models.EmailField()
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    send_status = models.CharField(max_length=255, choices=SendStatus.choices)
