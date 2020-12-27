from django.contrib.auth import get_user_model

from rest_framework import serializers

from print_nanny_webapp.client_events.models import (
    OctoPrintEvent,
    OctoPrintDevice
)

class OctoPrintEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = OctoPrintEvent
        fields = [field.name for field in OctoPrintEvent._meta.fields] + ["url"]
        extra_kwargs = {
            "url": {"view_name": "api:octoprint-event-detail", "lookup_field": "id"}
        }
        read_only_fields = ("user",)

class  OctoPrintDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = OctoPrintDevice
        fields = [field.name for field in OctoPrintDevice._meta.fields] + ["url"]
        extra_kwargs = {
            "url": {"view_name": "api:octoprint-device-detail", "lookup_field": "id"}
        }

        read_only_fields = ("user", "private_key", "public_key")
