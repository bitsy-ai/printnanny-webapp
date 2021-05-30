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

class OctoprintPiSupportSerializer(serializers.Serializer):
    model = serializers.CharField()
    throttle_state = serializers.CharField()
    octopi_version = serializers.CharField()

class OctoprintEnvironmentSerializer(serializers.Serializer):
    os = OctoprintPlatformSerializer()
    python = OctoprintPythonSerializer()
    hardware = OctoprintHardwareSerializer()
    pi_support = OctoprintPiSupportSerializer()

class OctoprintPrinterFlagsSerializer(serializers.Serializer):
    operational = serializers.BooleanField()
    printing = serializers.BooleanField()
    cancelling = serializers.BooleanField()
    pausing = serializers.BooleanField()
    resuming = serializers.BooleanField()
    finishing = serializers.BooleanField()
    closedOrError = serializers.BooleanField()
    error = serializers.BooleanField()
    paused = serializers.BooleanField()
    ready = serializers.BooleanField()
    sdReady = serializers.BooleanField()

class OctoprintPrinterStateSerializer(serializers.Serializer):
    text = serializers.CharField()
    flags = OctoprintPrinterFlagsSerializer()

class OctoprintProgressSerializer(serializers.Serializer):
    completion = serializers.FloatField()
    filepos = serializers.IntegerField()
    printTime = serializers.IntegerField()
    printTimeLeft = serializers.IntegerField()
    printTimeOrigin = serializers.CharField()

class OctoprintPrinterDataSerializer(serializers.Serializer):
    job = OctoprintJobSerializer()
    state = OctoprintPrinterStateSerializer()
    user = serializers.CharField()
    currentZ = serializers.FloatField()
    progress = OctoprintProgressSerializer()
    resends = serializers.DictField()

class TelemetryEventSerializer(serializers.ModelSerializer):
    print_session = serializers.StringRelatedField()
    event_type = serializers.ChoiceField(choices=TelemetryEventType.choices)
    environment = OctoprintEnvironmentSerializer()
    printer_data = OctoprintPrinterDataSerializer()
    temperature = serializers.DictField()
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
