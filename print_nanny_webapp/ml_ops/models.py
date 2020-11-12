from django.db import models
from django.contrib.postgres.fields import JSONField


class TFLiteModel(models.Model):

    created_dt = models.fields.DateTimeField(auto_now_add=True)
    modified_dt = models.fields.DateTimeField(auto_now=True)
    version = models.CharField(max_length=255)
    labels = models.FileField()
    model = models.FileField()
    metadata = JSONField()