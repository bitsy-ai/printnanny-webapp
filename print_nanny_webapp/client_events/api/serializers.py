from django.contrib.auth import get_user_model
from rest_framework import serializers

from ..models import (
    OctoPrintEvent, 
    PredictEvent, 
    PredictEventFile
)

# @extend_schema_field(OpenApiTypes.OBJECT)  # also takes basic python types
# class JSONField(serializers.JSONField):
#     pass

class OctoPrintEventSerializer(serializers.ModelSerializer):

    class Meta:
        model = OctoPrintEvent
        fields = [ field.name for field in OctoPrintEvent._meta.fields ] + ["url"]
        extra_kwargs = {
            "url": {"view_name": "api:octoprint-event-detail", "lookup_field": "id"}
        }
        read_only_fields = ('user',)

class PredictEventFileSerializer(serializers.ModelSerializer):

    class Meta:
        model = PredictEventFile
        fields = [ field.name for field in PredictEventFile._meta.fields ] + ["url"]
        extra_kwargs = {
            "url": {"view_name": "api:predict-event-file-detail", "lookup_field": "id"}
        }
        

class PredictEventSerializer(serializers.ModelSerializer):

    #event_data = JSONField()

    class Meta:
        model = PredictEvent
        fields = [ field.name for field in PredictEvent._meta.fields ] + ["url"]
        extra_kwargs = {
            "url": {"view_name": "api:predict-event-detail", "lookup_field": "id"}
        }
        
        read_only_fields = ('user',)
        