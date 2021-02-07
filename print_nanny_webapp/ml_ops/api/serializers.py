from rest_framework import serializers
from django.apps import apps

ModelArtifact = apps.get_model('ml_ops', 'ModelArtifact')

ExperimentDeviceConfig = apps.get_model('ml_ops', 'ExperimentDeviceConfig')


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
        fields = [
            "id",
            "created_dt",
            "experiment",
            "artifact"
        ]
        depth = 1