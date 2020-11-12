from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.postgres.fields import JSONField

User = get_user_model()

#TFLiteModel = apps.get_model('ml_ops', 'TFLiteModel')

class Printer(models.Model):

    display = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    extra = JSONField()

class PrintJob(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    printer = models.ForeignKey(Printer, on_delete=models.CASCADE)
    gcode = models.FileField()
    state = models.CharField(max_length=255)



class PredictEvent(models.Model):
    dt = models.DateTimeField()
    #model = models.ForeignKey(TFLiteModel)
    image = models.ImageField()
    event_data = JSONField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    printer = models.ForeignKey(Printer, null=True, on_delete=models.CASCADE)
    print_job = models.ForeignKey(PrintJob, null=True, on_delete=models.CASCADE)
    plugin_version = models.CharField(max_length=30)
    octoprint_version = models.CharField(max_length=30)

class OctoPrintEvent(models.Model):
    dt = models.DateTimeField()
    event_type = models.CharField(max_length=30)
    event_data = JSONField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    printer = models.ForeignKey(Printer, null=True, on_delete=models.CASCADE)
    print_job = models.ForeignKey(PrintJob, null=True, on_delete=models.CASCADE)
    plugin_version = models.CharField(max_length=30)
    octoprint_version = models.CharField(max_length=30)
