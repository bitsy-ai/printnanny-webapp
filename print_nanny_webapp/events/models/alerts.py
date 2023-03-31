from typing import Dict
from uuid import uuid4

from django.contrib.auth import get_user_model
from django.db import models
from print_nanny_webapp.utils.fields import ChoiceArrayField
from django.utils import timezone

from .enum import AlertEventType, EventSource

User = get_user_model()


def print_job_alert_filepath(instance, filename):
    path = timezone.now().strftime("uploads/print_job_alerts/%Y/%m/%d")
    return f"{path}/{instance.id}.jpg"


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

    EMAIL_TEMPLATE_ID = "print-job-alert"

    class Meta:
        ordering = ["-created_dt"]
        index_together = [
            ["id", "user", "pi", "created_dt"],
            ["id", "email_message_id"],
        ]

    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    created_dt = models.DateTimeField(auto_now_add=True)
    event_type = models.CharField(choices=AlertEventType.choices, max_length=32)
    event_source = models.CharField(choices=EventSource.choices, max_length=32)

    payload = models.JSONField(null=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)  # type: ignore[var-annotated]
    pi = models.ForeignKey("devices.Pi", on_delete=models.CASCADE)

    # unique identifier from email message provider, used to build associations on send status
    email_message_id = models.CharField(max_length=255, null=True)
    # unique identifier associated with celery task
    celery_task_id = models.CharField(max_length=255, null=True)

    def email_subject(self) -> str:
        if self.event_type == AlertEventType.PRINT_PROGRESS:
            completion = self.payload.get("progress", {}).get("completion")
            if completion is None:
                raise ValueError(
                    "PrintJobAlert.payload missing progress.completion field for PRINT_PROGRESS"
                )
            return f"[PrintNanny] 🎉 Your print job is {completion}% complete"
        elif self.event_type == AlertEventType.PRINT_STARTED:
            return "[PrintNanny] 🏁 Your print job was started"
        elif self.event_type == AlertEventType.PRINT_DONE:
            return "[PrintNanny] 🏁 Your print job is finished"
        elif self.event_type == AlertEventType.PRINT_PAUSED:
            return "[PrintNanny] ⏸️ Your print job was paused"
        elif self.event_type == AlertEventType.PRINT_CANCELLED:
            return "[PrintNanny] ⏸️ Your print job was cancelled"
        raise ValueError(f"No email_subject configured for {self.event_type}")

    def email_alert_header(self) -> str:
        if self.event_type == AlertEventType.PRINT_PROGRESS:
            completion = self.payload.get("progress", {}).get("completion")
            if completion is None:
                raise ValueError(
                    "PrintJobAlert.email_alert_header missing progress.completion field for PRINT_PROGRESS"
                )
            return f"[PrintNanny] 🎉 Your print job is {completion}% complete"
        elif self.event_type == AlertEventType.PRINT_STARTED:
            return "[PrintNanny] 🏁 Your print job was started"
        elif self.event_type == AlertEventType.PRINT_DONE:
            return "[PrintNanny] 🏁 Your print job is finished"
        elif self.event_type == AlertEventType.PRINT_PAUSED:
            return "[PrintNanny] ⏸️ Your print job was paused"
        elif self.event_type == AlertEventType.PRINT_CANCELLED:
            return "[PrintNanny] ⏸️ Your print job was cancelled"
        raise ValueError(f"No email_subject configured for {self.event_type}")

    def email_alert_body(self) -> str:
        return "Log into PrintNanny Cloud to manage your 3D printer."

    def email_merge_data(self) -> Dict[str, str]:
        if self.pi.latest_camera_snapshot():
            return {
                "alertHeader": self.email_alert_header(),
                "alertBody": self.email_alert_body(),
                "alertImageUrl": self.pi.latest_camera_snapshot().image.url,
            }
        return {
            "alertHeader": self.email_alert_header(),
            "alertBody": self.email_alert_body(),
            "alertImageUrl": None,
        }
