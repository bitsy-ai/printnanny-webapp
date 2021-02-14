from rest_framework import serializers
from django.apps import apps
from drf_spectacular.utils import extend_schema_field

DeviceCalibration = apps.get_model("ml_ops", "DeviceCalibration")
ModelArtifact = apps.get_model("ml_ops", "ModelArtifact")
ExperimentDeviceConfig = apps.get_model("ml_ops", "ExperimentDeviceConfig")


@extend_schema_field(field={'type': 'array', 'items': {'type': 'number'}})
class JSONArrayField(serializers.JSONField):
    pass

class DeviceCalibrationSerializer(serializers.ModelSerializer):

    mask = JSONArrayField()

    class Meta:
        model = DeviceCalibration
        fields = [field.name for field in DeviceCalibration._meta.fields] + [
            "url",
        ]
        extra_kwargs = {
            "url": {"view_name": "api:device-calibration-detail", "lookup_field": "id"},
        }

    def update_or_create(self, validated_data):
        unique_together = ("octoprint_device",)
        defaults = {k: v for k, v in validated_data.items() if k not in unique_together}
        unique_together_fields = {
            k: v for k, v in validated_data.items() if k in unique_together
        }

        return DeviceCalibration.objects.filter(
            **unique_together_fields
        ).update_or_create(
            **unique_together_fields,
            defaults=defaults
        )


class ModelArtifactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelArtifact
        fields = [field.name for field in ModelArtifact._meta.fields] + [
            "url",
        ]
        extra_kwargs = {
            "url": {"view_name": "api:model-artifact-detail", "lookup_field": "id"},
        }

        read_only_fields = [field.name for field in ModelArtifact._meta.fields]


class ExperimentDeviceConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExperimentDeviceConfig
        fields = ["id", "created_dt", "experiment", "artifact"]
        depth = 1
