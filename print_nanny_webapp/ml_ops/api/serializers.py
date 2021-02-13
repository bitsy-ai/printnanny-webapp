from rest_framework import serializers
from django.apps import apps

DeviceCalibration = apps.get_model("ml_ops", "DeviceCalibration")
ModelArtifact = apps.get_model("ml_ops", "ModelArtifact")
ExperimentDeviceConfig = apps.get_model("ml_ops", "ExperimentDeviceConfig")


class DeviceCalibrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceCalibration
        fields = [field.name for field in DeviceCalibration._meta.fields] + [
            "url",
        ]
        extra_kwargs = {
            "url": {"view_name": "api:device-calibration-detail", "lookup_field": "id"},
        }

    def update_or_create(self, validated_data):
        return DeviceCalibration.objects.update_or_create(defaults=validated_data)


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
