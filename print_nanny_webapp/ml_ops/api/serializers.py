from rest_framework import serializers
from print_nanny_webapp.ml_ops.models import TFLiteModel

class TFLiteModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TFLiteModel
        fields = [field.name for field in TFLiteModel._meta.fields] + [
            "url",
        ]
        extra_kwargs = {
            "url": {"view_name": "api:command-detail", "lookup_field": "id"},
        }

        read_only_fields = [field.name for field in TFLiteModel._meta.fields]
