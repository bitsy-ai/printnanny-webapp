from typing import Optional
from rest_framework import serializers

from print_nanny_webapp.telemetry.models import (
    OctoPrintEvent,
    PrintStatusEvent,
    PrintNannyPluginEvent,
    RemoteCommandEvent,
    TelemetryEvent
)
from print_nanny_webapp.telemetry.types import PrintStatusEventType, TelemetryEventType
from rest_polymorphic.serializers import PolymorphicSerializer

class OctoprintFileSerializer(serializers.Serializer):
    name = serializers.CharField(allow_null=True)
    path = serializers.CharField(allow_null=True)
    display = serializers.CharField(required=False)
    origin = serializers.CharField(allow_null=True)
    size = serializers.IntegerField(allow_null=True)
    date = serializers.IntegerField(allow_null=True)

class OctoprintJobSerializer(serializers.Serializer):
    file = OctoprintFileSerializer()
    estimatedPrintTime = serializers.FloatField(required=False, allow_null=True)
    averagePrintTime = serializers.FloatField(required=False)
    lastPrintTime = serializers.FloatField(required=False, allow_null=True)
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
    octopi_version = serializers.CharField(required=False)

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
    completion = serializers.FloatField(allow_null=True)
    filepos = serializers.IntegerField(allow_null=True)
    printTime = serializers.IntegerField(allow_null=True)
    printTimeLeft = serializers.IntegerField(allow_null=True)
    printTimeOrigin = serializers.CharField(allow_null=True)

class OctoprintPrinterDataSerializer(serializers.Serializer):
    job = OctoprintJobSerializer()
    state = OctoprintPrinterStateSerializer()
    user = serializers.CharField(required=False, allow_null=True)
    currentZ = serializers.FloatField(required=False)
    progress = OctoprintProgressSerializer()
    resends = serializers.DictField()
    offsets = serializers.DictField()

class TelemetryEventSerializer(serializers.ModelSerializer):
    print_session = serializers.StringRelatedField(required=False)
    event_type = serializers.ChoiceField(choices=TelemetryEventType.choices)
    environment = OctoprintEnvironmentSerializer()
    printer_data = OctoprintPrinterDataSerializer()
    temperature = serializers.DictField()
    class Meta:
        model = TelemetryEvent
        fields = "__all__"
        read_only_fields = ("user", "event_source")

class PrintStatusEventSerializer(serializers.ModelSerializer):
    print_session = serializers.StringRelatedField(required=False)

    class Meta:
        model = PrintStatusEvent
        fields = "__all__"
        read_only_fields = ("user",)

class OctoPrintEventSerializer(serializers.ModelSerializer):
    print_session = serializers.StringRelatedField(required=False)

    class Meta:
        model = OctoPrintEvent
        fields = "__all__"
        read_only_fields = ("user",)


class PrintNannyPluginEventSerializer(serializers.ModelSerializer):
    print_session = serializers.StringRelatedField(required=False)

    class Meta:
        model = PrintNannyPluginEvent
        fields = "__all__"
        read_only_fields = ("user",)

class RemoteCommandEventSerializer(serializers.ModelSerializer):
    print_session = serializers.StringRelatedField(required=False)

    class Meta:
        model = RemoteCommandEvent
        fields = "__all__"
        read_only_fields = ("user",)

class TelemetryEventPolymorphicSerializer(PolymorphicSerializer):
    print_session = serializers.StringRelatedField(required=False)

    model_serializer_mapping = {
        TelemetryEvent: TelemetryEventSerializer,
        RemoteCommandEvent: RemoteCommandEventSerializer,
        PrintStatusEvent: PrintStatusEventSerializer,
        OctoPrintEvent: OctoPrintEventSerializer,
        PrintNannyPluginEvent: PrintNannyPluginEventSerializer
    }