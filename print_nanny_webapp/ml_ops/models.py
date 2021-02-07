import json
import random

from google.cloud import iot_v1 as cloudiot_v1
from google.protobuf.json_format import MessageToDict

from django.db import models
from django.contrib.postgres.fields import JSONField

from print_nanny_webapp.utils.fields import ChoiceArrayField


class ModelArtifact(models.Model):
    class ArtifactTypes(models.TextChoices):
        TFLITE = "TFLITE", "TensorFlow Lite Flatbuffer"
        TF1 = "TF1", "TensorFlow v1 SavedModel format (legacy)"
        TF2_SAVED_MODEL = "TF2_SAVED_MODEL", "TensorFlow v2 SavedModel format"
        TF2_HDF5 = "TF2_HDF5", "TensorFlow v2 Keras H5 format"

    created_dt = models.fields.DateTimeField(auto_now_add=True)
    version = models.CharField(max_length=255)
    labels = models.FileField()
    artifacts = models.FileField()
    artifact_types = ChoiceArrayField(
        models.CharField(choices=ArtifactTypes.choices, max_length=255),
        default=(ArtifactTypes.TFLITE,),
    )
    metadata = JSONField()


class Experiment(models.Model):
    created_dt = models.fields.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    name = models.CharField(max_length=255)
    hypothesis = models.CharField(max_length=255)
    notion_url = models.CharField(max_length=255, null=True)

    control = models.ForeignKey(
        ModelArtifact, on_delete=models.CASCADE, related_name="control"
    )
    treatments = models.ManyToManyField(ModelArtifact, related_name="treatment", null=True, blank=True)

    def randomize_group(self):
        num_groups = len(self.treatments.all()) + 1
        return random.randrange(num_groups)

    def activate(self):
        self.__class__.objects.all().update(active=False)
        self.active = True
        self.save()
        return self.active


class ExperimentDeviceConfig(models.Model):
    created_dt = models.fields.DateTimeField(auto_now_add=True)
    device = models.ForeignKey(
        "remote_control.OctoPrintDevice", db_index=True, on_delete=models.CASCADE
    )
    experiment = models.ForeignKey(Experiment, db_index=True, on_delete=models.CASCADE)
    experiment_group = models.IntegerField()

    def publish(self):
        from print_nanny_webapp.ml_ops.api.serializers import (
            ExperimentDeviceConfigSerializer,
        )

        serializer = ExperimentDeviceConfigSerializer(instance=self)
        client = cloudiot_v1.DeviceManagerClient()
        data = json.dumps(serializer.data, sort_keys=True).encode("utf-8")
        return client.modify_cloud_to_device_config(
            request={
                "name": self.device.cloudiot_device_path,
                "binary_data": data,
                "version_to_update": 0,  # a value of 0 will always update the last version seen
            }
        )
