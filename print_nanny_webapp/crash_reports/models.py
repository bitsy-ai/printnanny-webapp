from uuid import uuid4
from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType

from safedelete.models import SafeDeleteModel, SOFT_DELETE

from print_nanny_webapp.crash_reports.enum import CrashReportStatusType

UserModel = get_user_model()


def crash_report_filepath(instance, filename):
    path = instance.created_dt.strftime("uploads/crash_reports/%Y/%m/%d")
    return f"{path}/{instance.id}/{filename}"


class CrashReport(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE

    id = models.UUIDField(primary_key=True, default=uuid4)
    created_dt = models.DateTimeField(auto_now_add=True)
    updated_dt = models.DateTimeField(auto_now=True)

    description = models.TextField(null=True)
    email = models.EmailField(null=True)
    user = models.ForeignKey(
        UserModel, null=True, on_delete=models.CASCADE, related_name="crash_reports"
    )
    pi = models.ForeignKey(
        "devices.Pi", null=True, on_delete=models.CASCADE, related_name="crash_reports"
    )
    os_version = models.CharField(null=True, max_length=255)
    os_logs = models.FileField(upload_to=crash_report_filepath, null=True)
    browser_version = models.CharField(null=True, max_length=255)
    browser_logs = models.FileField(upload_to=crash_report_filepath, null=True)
    serial = models.CharField(max_length=255, null=True)
    posthog_session = models.CharField(max_length=255, null=True)

    def get_admin_url(self):
        content_type = ContentType.objects.get_for_model(self.__class__)
        return reverse(
            f"admin:{content_type.app_label}_{content_type.model}_change",
            args=(self.id,),
        )

    status = models.CharField(
        max_length=255,
        choices=CrashReportStatusType.choices,
        default=CrashReportStatusType.INVESTIGATING,
    )
    support_comment = models.TextField(null=True)
