from django.contrib.auth import get_user_model
from rest_framework import serializers

from print_nanny_webapp.client_events.models import (
    OctoPrintEvent,
    ObjectDetectEvent,
    ObjectDetectEventFile,
)

# @extend_schema_field(OpenApiTypes.OBJECT)  # also takes basic python types
# class JSONField(serializers.JSONField):
#     pass


class OctoPrintEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = OctoPrintEvent
        fields = [field.name for field in OctoPrintEvent._meta.fields] + ["url"]
        extra_kwargs = {
            "url": {"view_name": "api:octoprint-event-detail", "lookup_field": "id"}
        }
        read_only_fields = ("user",)


class ObjectDetectEventFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObjectDetectEventFile
        fields = [field.name for field in ObjectDetectEventFile._meta.fields] + ["url"]
        extra_kwargs = {
            "url": {"view_name": "api:predict-event-file-detail", "lookup_field": "id"}
        }


class ObjectDetectEventSerializer(serializers.ModelSerializer):

    # event_data = JSONField()

    class Meta:
        model = ObjectDetectEvent
        fields = [field.name for field in ObjectDetectEvent._meta.fields] + ["url"]
        extra_kwargs = {
            "url": {"view_name": "api:predict-event-detail", "lookup_field": "id"}
        }

        read_only_fields = ("user",)
