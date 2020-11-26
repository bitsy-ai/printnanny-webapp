from django.contrib.auth import get_user_model
from django.db import models
from django.apps import apps
from django.utils import timezone

from urllib.parse import urljoin
from django.contrib.postgres.fields import ArrayField
from django.contrib.sites.shortcuts import get_current_site
from print_nanny_webapp.remote_control.models import PrintJob

User = get_user_model()


class PredictEventFile(models.Model):

    annotated_image = models.ImageField(upload_to='uploads/predict_event/%Y/%m/%d/')
    hash = models.CharField(max_length=255)
    original_image = models.ImageField(upload_to='uploads/predict_event/%Y/%m/%d/')


class PredictEvent(models.Model):

    dt = models.DateTimeField(db_index=True, default=timezone.now)
    #model = models.ForeignKey(TFLiteModel)
    event_data = models.JSONField(null=True)
    predict_data = models.JSONField()

    user = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True)
    files = models.ForeignKey(PredictEventFile, on_delete=models.CASCADE)
    print_job = models.ForeignKey(PrintJob, on_delete=models.CASCADE)

    plugin_version = models.CharField(max_length=30)
    octoprint_version = models.CharField(max_length=30)

class OctoPrintEvent(models.Model):

    dt = models.DateTimeField(db_index=True)
    event_type = models.CharField(max_length=30, db_index=True)
    event_data = models.JSONField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True)
    plugin_version = models.CharField(max_length=30)
    octoprint_version = models.CharField(max_length=30)
    print_job = models.ForeignKey(PrintJob, null=True, on_delete=models.SET_NULL, db_index=True)
