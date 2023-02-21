from django.contrib import admin
from print_nanny_webapp.octoprint.models import (
    OctoPrintBackup,
    OctoPrintServer,
    OctoPrinterProfile,
    OctoPrintSettings,
    GcodeFile,
    OctoPrintServerStatus,
    OctoPrintPrinterStatus,
    OctoPrintPrintJobStatus,
    OctoPrintGcodeEvent,
)


@admin.register(OctoPrintServerStatus)
class OctoPrintServerStatusAdmin(admin.ModelAdmin):
    list_display = (
        "event_type",
        "pi",
        "subject_pattern",
        "octoprint_server",
        "created_dt",
    )
    model = OctoPrintServerStatus


@admin.register(OctoPrintGcodeEvent)
class OctoPrintGcodeEventAdmin(admin.ModelAdmin):
    list_display = (
        "event_type",
        "pi",
        "subject_pattern",
        "octoprint_server",
        "created_dt",
    )
    model = OctoPrintGcodeEvent


@admin.register(OctoPrintPrinterStatus)
class OctoPrintPrinterStatusAdmin(admin.ModelAdmin):
    list_display = (
        "event_type",
        "pi",
        "subject_pattern",
        "octoprint_server",
        "created_dt",
    )
    model = OctoPrintPrinterStatus


@admin.register(OctoPrintPrintJobStatus)
class OctoPrintPrintJobStatusAdmin(admin.ModelAdmin):
    list_display = (
        "event_type",
        "pi",
        "subject_pattern",
        "octoprint_server",
        "created_dt",
    )
    model = OctoPrintPrintJobStatus


@admin.register(OctoPrintBackup)
class OctoPrintBackupAdmin(admin.ModelAdmin):
    list_display = ("name", "user", "created_dt")
    model = OctoPrintBackup


@admin.register(OctoPrintServer)
class OctoPrintServerAdmin(admin.ModelAdmin):
    list_display = (
        "pi",
        "user",
        "octoprint_version",
        "printnanny_plugin_version",
        "created_dt",
        "updated_dt",
    )
    model = OctoPrintServer


@admin.register(OctoPrinterProfile)
class OctoPrinterProfileAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "name",
        "created_dt",
        "updated_dt",
    )
    model = OctoPrinterProfile


@admin.register(OctoPrintSettings)
class OctoPrintSettingsAdmin(admin.ModelAdmin):
    list_display = (
        "octoprint_server",
        "events_enabled",
        "updated_dt",
    )
    model = OctoPrintSettings


@admin.register(GcodeFile)
class GcodeFileAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "name",
        "created_dt",
    )
    model = GcodeFile
