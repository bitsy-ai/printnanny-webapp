from uuid import uuid4
from time import strftime
from django.db import models
from django.contrib.auth import get_user_model

from safedelete.models import SafeDeleteModel, SOFT_DELETE

UserModel = get_user_model()


def crash_report_filepath(instance, filename):
    path = instance.created_dt.strftime("uploads/crash_reports/%Y/%m/%d")
    return f"{path}/{instance.id}/{filename}"


class CrashReport(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE

    id = models.UUIDField(primary_key=True, default=uuid4)
    created_dt = models.DateTimeField(auto_now_add=True)
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