from django.contrib.auth import get_user_model
from django.conf import settings
from django.db import models
from django.db.models import UniqueConstraint
from safedelete.models import SafeDeleteModel, SOFT_DELETE

from print_nanny_webapp.utils.fields import file_field_upload_to

User = get_user_model()
# A bit of data model history:
# remote_control/models.py contains OctoPrintDevice, which is how an OctoPrint device is registered via "plugin alpha"
# devices/models.py contains Device, whichi is a generic Raspberry Pi / single-board computer with Print Nanny OS installed
# the models contained in the octoprint app are intended to bridge these two implementations, and eventually contain all octoprint-related models/services


class OctoPrintInstall(SafeDeleteModel):
    class Meta:
        index_together = (
            ("created_dt", "user", "device", "updated_dt"),
            (
                "printnanny_plugin_version",
                "octoprint_version",
                "pip_version",
                "python_version",
                "device",
            ),
        )
        constraints = [
            UniqueConstraint(
                fields=["device"],
                condition=models.Q(deleted=None),
                name="unique_octoprint_install_per_device",
            )
        ]

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="octoprint_installs"
    )
    device = models.ForeignKey(
        "devices.Device", on_delete=models.CASCADE, related_name="octoprint_installs"
    )
    octoprint_version = models.CharField(max_length=32)
    pip_version = models.CharField(max_length=32)
    python_version = models.CharField(max_length=32)
    printnanny_plugin_version = models.CharField(max_length=32)
    created_dt = models.DateTimeField(auto_now_add=True)
    updated_dt = models.DateTimeField(auto_now=True)

    # @property
    # def settings(self):
    #     return OctoPrintSettings.objects.get(octoprint_install=self)


class OctoPrintSettings(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE

    octoprint_install = models.OneToOneField(
        OctoPrintInstall, on_delete=models.CASCADE, related_name="settings"
    )
    events_enabled = models.BooleanField(
        default=False,
        help_text="Send OctoPrint events to PrintNanny Cloud https://docs.octoprint.org/en/master/events/index.html",
    )
    telemetry_enabled = models.BooleanField(
        default=False,
        help_text="Send telemetry data to PrintNanny Cloud for debugging/analytics purposes",
    )
    sync_gcode = models.BooleanField(
        default=True, help_text="Sync Gcode files to/from PrintNanny Cloud"
    )
    sync_printer_profiles = models.BooleanField(
        default=True, help_text="Sync Printer Profiles to/from PrintNanny Cloud"
    )
    sync_backups = models.BooleanField(
        default=True, help_text="Upload OctoPrint backups to PrintNanny Cloud"
    )
    auto_backup = models.CharField(
        max_length=64, default=settings.PRINTNANNY_OS_DEFAULT_BACKUP_SCHEDULE
    )
    monitoring_auto_start = models.BooleanField(
        default=True,
        help_text="Start PrintNanny monitoring automatically when a print job begins",
    )
    monitoring_auto_pause = models.BooleanField(
        default=True,
        help_text="Pause failing print jobs automatically",
    )
    created_dt = models.DateTimeField(auto_now_add=True)
    updated_dt = models.DateTimeField(auto_now=True)


class GcodeFile(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE

    class Meta:
        unique_together = ("user", "name", "hash")
        constraints = [
            UniqueConstraint(
                fields=["user", "hash"],
                condition=models.Q(deleted=None),
                name="unique_gcode_file_hash_per_user",
            )
        ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="gcode_files")
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to="uploads/gcode_file/%Y/%m/%d/")
    hash = models.CharField(max_length=255)
    created_dt = models.DateTimeField(auto_now_add=True)


class OctoPrintBackup(SafeDeleteModel):
    """
    Create/restore an OctoPrint backup
    """

    _safedelete_policy = SOFT_DELETE

    created_dt = models.DateTimeField(auto_now_add=True, db_index=True)
    hostname = models.CharField(max_length=64)
    name = models.CharField(max_length=255)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="octoprint_backups"
    )
    octoprint_version = models.CharField(max_length=64)
    file = models.FileField(upload_to=file_field_upload_to)

    class Meta:
        ordering = ["-created_dt"]


class OctoPrinterProfile(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=["user", "octoprint_key"],
                condition=models.Q(deleted=None),
                name="unique_printer_profile_name_per_user",
            )
        ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        db_index=True,
        related_name="octo_printer_profiles",
    )

    axes_e_inverted = models.BooleanField(null=True)
    axes_e_speed = models.IntegerField(null=True)

    axes_x_speed = models.IntegerField(null=True)
    axes_x_inverted = models.BooleanField(null=True)

    axes_y_inverted = models.BooleanField(null=True)
    axes_y_speed = models.IntegerField(null=True)

    axes_z_inverted = models.BooleanField(null=True)
    axes_z_speed = models.IntegerField(null=True)

    extruder_count = models.IntegerField(null=True)
    extruder_nozzle_diameter = models.FloatField(null=True)
    extruder_shared_nozzle = models.BooleanField(null=True)

    heated_bed = models.BooleanField(null=True)
    heated_chamber = models.BooleanField(null=True)

    model = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255)
    octoprint_key = models.CharField(max_length=255, db_index=True)

    volume_custom_box = models.JSONField(default={})
    volume_depth = models.FloatField(null=True)
    volume_formfactor = models.CharField(null=True, max_length=255)
    volume_height = models.FloatField(null=True)
    volume_origin = models.CharField(null=True, max_length=255)
    volume_width = models.FloatField(null=True)
    created_dt = models.DateTimeField(auto_now_add=True)
    updated_dt = models.DateTimeField(auto_now=True)
