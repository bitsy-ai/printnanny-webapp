from django.contrib import admin
from print_nanny_webapp.octoprint.models import (
    OctoPrintBackup,
    OctoPrintInstall,
    OctoPrinterProfile,
    OctoPrintSettings,
    GcodeFile,
)


@admin.register(OctoPrintBackup)
class OctoPrintBackupAdmin(admin.ModelAdmin):
    list_display = ("name", "user", "created_dt")
    model = OctoPrintBackup


@admin.register(OctoPrintInstall)
class OctoPrintInstallAdmin(admin.ModelAdmin):
    list_display = (
        "device",
        "user",
        "octoprint_version",
        "printnanny_plugin_version",
        "created_dt",
        "updated_dt",
    )
    model = OctoPrintInstall


# @admin.register(OctoPrinterProfile)
# class OctoPrinterProfileAdmin(admin.ModelAdmin):
#     list_display = (
#         "user",
#         "name",
#         "printnanny_plugin_version",
#         "created_dt",
#         "updated_dt",
#     )
#     model = OctoPrinterProfile
