from django.contrib.auth import get_user_model
from django.db import models

from print_nanny_webapp.utils.fields import file_field_upload_to

User = get_user_model()
# A bit of data model history:
# remote_control/models.py contains OctoPrintDevice, which is how an OctoPrint device is registered via "plugin alpha"
# devices/models.py contains Device, whichi is a generic Raspberry Pi / single-board computer with Print Nanny OS installed
# the models contained in the octoprint app are intended to bridge these two implementations, and eventually contain all octoprint-related models/services


class OctoPrintBackup(models.Model):
    """
    Create/restore an OctoPrint backup
    """

    created_dt = models.DateTimeField(auto_now_add=True, db_index=True)
    hostname = models.CharField(max_length=64)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    octoprint_version = models.CharField(max_length=64)
    file = models.FileField(upload_to=file_field_upload_to)
