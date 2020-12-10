from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from urllib.parse import urljoin
from django.contrib.postgres.fields import ArrayField
from django.contrib.sites.shortcuts import get_current_site

User = get_user_model()

class GcodeFile(models.Model):
    class Meta:
        unique_together = ('user', 'file_hash')

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='uploads/gcode_file/%Y/%m/%d/')
    file_hash = models.CharField(max_length=255)

class PrinterProfile(models.Model):

    class Meta:
        unique_together = ('user', 'name',)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    axes_e_inverted = models.BooleanField()
    axes_e_speed = models.IntegerField()

    axes_x_speed = models.IntegerField()
    axes_x_inverted = models.BooleanField()

    axes_y_inverted = models.BooleanField()
    axes_y_speed = models.IntegerField()

    axes_z_inverted = models.BooleanField()
    axes_z_speed = models.IntegerField()

    extruder_count = models.IntegerField()
    extruder_nozzle_diameter = models.FloatField()
    extruder_shared_nozzle = models.BooleanField()

    heated_bed = models.BooleanField()
    heated_chamber = models.BooleanField()

    model = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255)

    volume_custom_box = models.BooleanField()
    volume_depth = models.FloatField()
    volume_formfactor = models.CharField(max_length=255)
    volume_height = models.FloatField()
    volume_origin = models.CharField(max_length=255)
    volume_width = models.FloatField()


class PrintJob(models.Model):
    class Meta:
        unique_together = ('user', 'name', 'dt')

    class StatusChoices(models.TextChoices):
        STARTED = 'STARTED', 'Started'
        DONE = 'DONE', 'Done'
        FAILED = 'FAILED', 'Failed'
        CANCELLING = 'CANCELLING', 'Cancelling'
        CANCELLED = 'CANCELLED', 'Cancelled'
        PAUSED = 'PAUSED', 'Paused'
        RESUMED = 'RESUMED', 'Resumed'

    dt = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    printer_profile = models.ForeignKey(PrinterProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    gcode_file_hash = models.CharField(max_length=255, null=True)
    gcode_file = models.ForeignKey(GcodeFile, on_delete=models.CASCADE, null=True)
    last_status = models.CharField(
        max_length=12,
        choices=StatusChoices.choices,
        default=StatusChoices.STARTED
    )
    last_seen = models.DateTimeField(auto_now=True)

    progress = models.IntegerField(default=0)


    @property
    def filename(self):
        return self.gcode_file.file.name