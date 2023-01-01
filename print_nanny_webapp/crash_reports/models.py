from uuid import uuid4
from time import strftime
from django.db import models
from django.contrib.auth import get_user_model

from safedelete.models import SafeDeleteModel, SOFT_DELETE

UserModel = get_user_model()


def crash_report_filepath(instance, filename):
    path = strftime("uploads/crash_reports/%Y/%m/%d", instance.created_dt)
    return f"{path}/{instance.id}/{filename}"


class CrashReport(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE

    id = models.UUIDField(primary_key=True, default=uuid4)
    created_dt = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(
        UserModel, null=True, on_delete=models.CASCADE, related_name="crash_reports"
    )
    os_version = models.CharField(null=True)
    os_logs = models.FileField(upload_to=crash_report_filepath, null=True)
    browser_version = models.CharField(null=True)
    browser_logs = models.FileField(upload_to=crash_report_filepath, null=True)
