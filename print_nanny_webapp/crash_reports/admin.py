from django.contrib import admin

from print_nanny_webapp.crash_reports.models import CrashReport
from print_nanny_webapp.crash_reports.enum import CrashReportStatusType


@admin.action(description="Mark fixed")
def mark_fixed(modeladmin, request, queryset):
    queryset.update(status=CrashReportStatusType.FIXED)


# Register your models here.
@admin.register(CrashReport)
class CrashReportAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "created_dt",
        "email",
        "user",
        "pi",
        "os_version",
        "browser_version",
    )
    model = CrashReport
    actions = [mark_fixed]
