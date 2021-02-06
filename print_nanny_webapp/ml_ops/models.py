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

