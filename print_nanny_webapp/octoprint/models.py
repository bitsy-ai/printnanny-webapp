import os
from django.contrib.auth import get_user_model
from django.conf import settings
from django.db import models
from django.db.models import UniqueConstraint
from safedelete.models import SafeDeleteModel, SOFT_DELETE

from print_nanny_webapp.utils.fields import file_field_upload_to

User = get_user_model()
# A bit of data model history:
# remote_control/models.py contains OctoPrintDevice, which is how an OctoPrint pi is registered via "plugin alpha"
# pis/models.py contains Device, whichi is a generic Raspberry Pi / single-board computer with Print Nanny OS installed
# the models contained in the octoprint app are intended to bridge these two implementations, and eventually contain all octoprint-related models/services


class OctoPrintServer(SafeDeleteModel):
    class Meta:
        index_together = (
            ("created_dt", "user", "pi", "updated_dt"),
            (
                "printnanny_plugin_version",
                "octoprint_version",
                "pip_version",
                "python_version",
                "pi",
            ),
        )
        constraints = [
            UniqueConstraint(
                fields=["pi"],
                condition=models.Q(deleted=None),
                name="unique_octoprint_server_per_pi",
            )
        ]

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="octoprint_servers"
    )
    pi = models.ForeignKey(
        "devices.Pi", on_delete=models.CASCADE, related_name="octoprint_servers"
    )
    octoprint_version = models.CharField(max_length=32, default="")
    pip_version = models.CharField(max_length=32, default="")
    python_version = models.CharField(max_length=32, default="")
    printnanny_plugin_version = models.CharField(max_length=64, default="")

    created_dt = models.DateTimeField(auto_now_add=True)
    updated_dt = models.DateTimeField(auto_now=True)
    api_key = models.CharField(max_length=255, null=True)

    @property
    def base_url(self) -> str:
        return self.pi.urls["octoprint"]

    @property
    def base_path(self) -> str:
        return "/home/printnanny/.octoprint/"

    @property
    def venv_path(self) -> str:
        return os.path.join(self.base_path, ".venv")

    @property
    def python_path(self) -> str:
        return os.path.join(self.venv_path, "bin/python")

    @property
    def pip_path(self) -> str:
        return os.path.join(self.venv_path, "bin/pip")

    @property
    def settings(self):
        return OctoPrintSettings.objects.get(octoprint_server=self)


class OctoPrintSettings(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE

    octoprint_server = models.OneToOneField(
        OctoPrintServer, on_delete=models.CASCADE, related_name="settings"
    )
    octoprint_enabled = models.BooleanField(
        default=True, help_text="Start OctoPrint service"
    )
    events_enabled = models.BooleanField(
        default=True,
        help_text="Send OctoPrint events related to print job status/progress to PrintNanny Cloud https://docs.octoprint.org/en/master/events/index.html",
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
    updated_dt = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="octoprint_settings", null=True
    )


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

    volume_custom_box = models.JSONField(default=dict)
    volume_depth = models.FloatField(null=True)
    volume_formfactor = models.CharField(null=True, max_length=255)
    volume_height = models.FloatField(null=True)
    volume_origin = models.CharField(null=True, max_length=255)
    volume_width = models.FloatField(null=True)
    created_dt = models.DateTimeField(auto_now_add=True)
    updated_dt = models.DateTimeField(auto_now=True)
