from typing import Optional
from rest_framework import serializers

from print_nanny_webapp.telemetry.models import (
    OctoPrintEvent,
    PrintStatusEvent,
    PrintNannyPluginEvent,
    RemoteCommandEvent,
    TelemetryEvent
)
from print_nanny_webapp.telemetry.types import TelemetryEventType

class OctoprintFileSerializer(serializers.Serializer):
    name = serializers.CharField()
    path = serializers.CharField()
    display = serializers.CharField()
    origin = serializers.CharField()
    size = serializers.IntegerField()
    date = serializers.IntegerField()

class OctoprintJobSerializer(serializers.Serializer):
    file = OctoprintFileSerializer()
    estimatedPrintTime = serializers.FloatField()
    averagePrintTime = serializers.FloatField()
    lastPrintTime = serializers.FloatField()
    filament = serializers.DictField()

class OctoprintPlatformSerializer(serializers.Serializer):
    id = serializers.CharField()
    platform = serializers.CharField()
    bits = serializers.CharField()  

class OctoprintPythonSerializer(serializers.Serializer):
    version = serializers.CharField()
    pip = serializers.CharField()
    virtualenv = serializers.CharField()

class OctoprintHardwareSerializer(serializers.Serializer):
    cores = serializers.IntegerField()
    freq = serializers.FloatField()
    ram = serializers.IntegerField()
    pi_model = serializers.CharField()
    throttle_state = serializers.CharField()
    octopi_version = serializers.CharField()

class OctoprintEnvironmentSerializer(serializers.Serializer):
    os = OctoprintPlatformSerializer()
    python = OctoprintPythonSerializer()
    hardware = OctoprintHardwareSerializer()

class TelemetryEventSerializer(serializers.ModelSerializer):
    print_session = serializers.StringRelatedField()
    event_type = serializers.ChoiceField(choices=TelemetryEventType.choices)
    environment = OctoprintEnvironmentSerializer()
    octoprint_job = OctoprintJobSerializer(required=False)
    class Meta:
        model = TelemetryEvent
        fields = "__all__"
        read_only_fields = ("user",)

class PrintStatusEventSerializer(serializers.ModelSerializer):
    print_session = serializers.StringRelatedField()
  
    class Meta:
        model = PrintStatusEvent
        fields = "__all__"
        read_only_fields = ("user",)

class OctoPrintEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = OctoPrintEvent
        fields = "__all__"
        read_only_fields = ("user",)


class PrintNannyPluginEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrintNannyPluginEvent
        fields = "__all__"
        read_only_fields = ("user",)

class RemoteCommandEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = RemoteCommandEvent
        fields = "__all__"
        read_only_fields = ("user",)
