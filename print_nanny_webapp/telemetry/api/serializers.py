from rest_framework import serializers

from print_nanny_webapp.telemetry.models import (
    OctoPrintEvent,
    PrintStatusEvent,
    OctoPrintPluginEvent,
    TelemetryEventTypes,
)


class TelemetryEventSerializer(serializers.ModelSerializer):
    event_type = serializers.SerializerMethodField()

    def get_event_type(self, obj) -> TelemetryEventTypes:
        return obj.event_type


class OctoPrintEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = OctoPrintEvent
        fields = [field.name for field in OctoPrintEvent._meta.fields] + ["url"]
        extra_kwargs = {
            "url": {"view_name": "api:octoprint-event-detail", "lookup_field": "id"}
        }
        read_only_fields = ("user",)


class OctoPrintPluginEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = OctoPrintPluginEvent
        fields = [field.name for field in OctoPrintPluginEvent._meta.fields] + ["url"]
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
