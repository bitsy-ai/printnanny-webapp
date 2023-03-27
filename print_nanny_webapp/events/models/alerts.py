from django.contrib.auth import get_user_model
from django.db import models
from print_nanny_webapp.utils.fields import ChoiceArrayField

from .enum import AlertEventType, EventSource

User = get_user_model()


class BaseAlertSettings(models.Model):
    created_dt = models.DateTimeField(auto_now_add=True)
    updated_dt = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    progress_percent = models.IntegerField(default=25)

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    enabled = models.BooleanField(default=True)
    event_types = ChoiceArrayField(
        models.CharField(choices=AlertEventType.choices, max_length=255),
        blank=True,
        default=list(
            [
                AlertEventType.PRINT_QUALITY,
                AlertEventType.PRINT_DONE,
                AlertEventType.PRINT_PROGRESS,
            ]
        ),
    )


class EmailAlertSettings(BaseAlertSettings):
    pass


class PrintJobAlert(models.Model):
    """
    User-facing print job notification alerts
    """

    class Meta:
        ordering = ["-created_dt"]
        index_together = [
            ["id", "user", "pi", "created_dt"],
            ["id", "email_message_id"],
        ]

    id = models.UUIDField(primary_key=True, editable=False)
    created_dt = models.DateTimeField(auto_now_add=True)
    event_type = models.CharField(choices=AlertEventType.choices, max_length=32)
    event_source = models.CharField(choices=EventSource.choices, max_length=32)

    payload = models.JSONField(null=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)  # type: ignore[var-annotated]
    pi = models.ForeignKey("devices.Pi", on_delete=models.CASCADE)

    # unique identifier from email message provider, used to build associations on send status
    email_message_id = models.CharField(max_length=255, null=True)
