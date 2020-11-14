from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.postgres.fields import ArrayField

User = get_user_model()

#TFLiteModel = apps.get_model('ml_ops', 'TFLiteModel')

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

    extruder_offsets = ArrayField(
        models.FloatField()
    )
    extruder_shared_nozzle = models.BooleanField()

    heated_bed = models.BooleanField()
    heated_chamber = models.BooleanField()

    model = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

    volume_custom_box = models.BooleanField()
    volume_depth = models.FloatField()
    volume_formfactor = models.CharField(max_length=255)
    volume_height = models.FloatField()
    volume_origin = models.CharField(max_length=255)
    volume_width = models.FloatField

class GcodeFile(models.Model):
    class Meta:
        unique_together = ('user', 'file_hash')

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    file = models.FileField()
    file_hash = models.CharField(max_length=255)

class PrintJob(models.Model):
    class Meta:
        unique_together = ('user', 'name', 'dt')

    dt = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    printer_profile = models.ForeignKey(PrinterProfile, on_delete=models.RESTRICT)
    name = models.CharField(max_length=255)
    gcode_file_hash = models.CharField(max_length=255, null=True)
    gcode_file = models.ForeignKey(GcodeFile, on_delete=models.RESTRICT, null=True)
        
class PredictEvent(models.Model):
    dt = models.DateTimeField()
    #model = models.ForeignKey(TFLiteModel)
    original_image = models.ImageField()
    annotated_image = models.ImageField()
    event_data = models.JSONField()

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    print_job = models.ForeignKey(PrintJob, null=True, on_delete=models.SET_NULL)


    plugin_version = models.CharField(max_length=30)
    octoprint_version = models.CharField(max_length=30)

class OctoPrintEvent(models.Model):
    dt = models.DateTimeField()
    event_type = models.CharField(max_length=30)
    event_data = models.JSONField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plugin_version = models.CharField(max_length=30)
    octoprint_version = models.CharField(max_length=30)
