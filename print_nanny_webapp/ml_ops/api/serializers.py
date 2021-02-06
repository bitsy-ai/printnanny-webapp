from rest_framework import serializers
from print_nanny_webapp.ml_ops.models import ModelArtifact


class ModelArtifactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelArtifact
        fields = [field.name for field in ModelArtifact._meta.fields] + [
            "url",
        ]
        extra_kwargs = {
            "url": {"view_name": "api:command-detail", "lookup_field": "id"},
        }

        read_only_fields = [field.name for field in ModelArtifact._meta.fields]
