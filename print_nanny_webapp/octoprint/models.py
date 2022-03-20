from django.contrib.auth import get_user_model
from django.db import models
from safedelete.models import SafeDeleteModel, SOFT_DELETE

from print_nanny_webapp.utils.fields import file_field_upload_to

User = get_user_model()
# A bit of data model history:
# remote_control/models.py contains OctoPrintDevice, which is how an OctoPrint device is registered via "plugin alpha"
# devices/models.py contains Device, whichi is a generic Raspberry Pi / single-board computer with Print Nanny OS installed
# the models contained in the octoprint app are intended to bridge these two implementations, and eventually contain all octoprint-related models/services


class OctoPrintSettings(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="octoprint_settings"
    )
    sync_gcode = models.BooleanField(
        default=True, help_text="Sync Gcode files to PrintNanny Cloud"
    )
    sync_printer_profiles = models.BooleanField(
        default=True, help_text="Sync Printer Profiles to PrintNanny Cloud"
    )
    sync_backups = models.BooleanField(
        default=True, help_text="Upload OctoPrint backups to PrintNanny Cloud"
    )
    monitoring_auto_start = models.BooleanField(
        default=True,
        help_text="Start PrintNanny monitoring automatically when a print job begins",
    )
    monitoring_auto_pause = models.BooleanField(
        default=True,
        help_text="Pause failing print jobs automatically",
    )


class OctoPrintBackup(models.Model):
    """
    Create/restore an OctoPrint backup
    """

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
