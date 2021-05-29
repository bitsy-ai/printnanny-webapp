from rest_framework import serializers

from print_nanny_webapp.telemetry.models import (
    OctoPrintEvent,
    PrintStatusEvent,
    PrintNannyPluginEvent,
)

from print_nanny_webapp.telemetry.types import TelemetryEventType


class OctoPrintEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = OctoPrintEvent
        fields = [field.name for field in OctoPrintEvent._meta.fields] + ["url"]
        extra_kwargs = {
            "url": {"view_name": "api:octoprint-event-detail", "lookup_field": "id"}
        }
        read_only_fields = ("user",)


class PrintNannyPluginEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrintNannyPluginEvent
        fields = [field.name for field in PrintNannyPluginEvent._meta.fields] + ["url"]
        extra_kwargs = {
            "url": {"view_name": "api:plugin-event-detail", "lookup_field": "id"}
        }
        read_only_fields = ("user",)


class PrintStatusEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrintStatusEvent
        fields = [field.name for field in PrintStatusEvent._meta.fields] + ["url"]
        extra_kwargs = {
            "url": {"view_name": "api:print-session-event-detail", "lookup_field": "id"}
        }
        read_only_fields = ("user",)
