from collections.abc import Mapping
from print_nanny_webapp.dashboard.views import OctoPrintDevice
from rest_framework import serializers
from django.apps import apps
from print_nanny_webapp.telemetry.models import (
    OctoPrintEvent,
    PrintJobEvent,
    PrintNannyPluginEvent,
    PrinterEvent,
    RemoteCommandEvent,
    TelemetryEvent,
)
from print_nanny_webapp.telemetry.types import (
    EventSource,
    PrintJobEventType,
    TelemetryEventType,
    PrintNannyPluginEventType,
    OctoprintEventType,
    RemoteCommandEventType,
    PrinterEventType,
)
from rest_polymorphic.serializers import PolymorphicSerializer


class OctoprintFileSerializer(serializers.Serializer):
    name = serializers.CharField(allow_null=True)
    path = serializers.CharField(allow_null=True)
    display = serializers.CharField(required=False, allow_null=True)
    origin = serializers.CharField(allow_null=True)
    size = serializers.IntegerField(allow_null=True)
    date = serializers.IntegerField(allow_null=True)


class OctoprintJobSerializer(serializers.Serializer):
    file = OctoprintFileSerializer(required=False, allow_null=True)
    estimatedPrintTime = serializers.FloatField(required=False, allow_null=True)
    averagePrintTime = serializers.FloatField(required=False, allow_null=True)
    lastPrintTime = serializers.FloatField(required=False, allow_null=True)
    filament = serializers.DictField(allow_null=True)


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
    printTimeOrigin = serializers.CharField(allow_null=True, required=False)


class OctoprintPrinterDataSerializer(serializers.Serializer):
    job = OctoprintJobSerializer()
    state = OctoprintPrinterStateSerializer()
    user = serializers.CharField(required=False, allow_null=True)
    currentZ = serializers.FloatField(required=False)
    progress = OctoprintProgressSerializer()
    resends = serializers.DictField()
    offsets = serializers.DictField()


class TelemetryEventSerializer(serializers.ModelSerializer):

    ts = serializers.FloatField(required=False)
    event_source = serializers.ChoiceField(
        choices=EventSource.choices,
        default=EventSource.PRINT_NANNY_PLUGIN,
        read_only=True,
    )
    event_type = serializers.ChoiceField(
        choices=TelemetryEventType.choices, default=TelemetryEventType.CONNECT_TEST_NOOP
    )
    octoprint_environment = OctoprintEnvironmentSerializer()
    octoprint_printer_data = OctoprintPrinterDataSerializer()

    class Meta:
        model = TelemetryEvent
        fields = "__all__"
        read_only_fields = ("id", "user", "event_source", "polymorphic_ctype")


class PrinterEventSerializer(TelemetryEventSerializer):
    event_type = serializers.ChoiceField(
        choices=PrinterEventType.choices, default=PrinterEventType.DISCONNECTED
    )
    event_source = serializers.ChoiceField(
        choices=EventSource.choices,
        default=EventSource.OCTOPRINT,
        read_only=True,
    )

    class Meta:
        model = PrinterEvent
        fields = "__all__"
        read_only_fields = ("id", "user", "event_source", "polymorphic_ctype")


class PrintJobEventSerializer(TelemetryEventSerializer):
    event_type = serializers.ChoiceField(
        choices=PrintJobEventType.choices, default=PrintJobEventType.PRINT_STARTED
    )
    event_source = serializers.ChoiceField(
        choices=EventSource.choices,
        default=EventSource.OCTOPRINT,
        read_only=True,
    )

    class Meta:
        model = PrintJobEvent
        fields = "__all__"
        read_only_fields = ("id", "user", "event_source", "polymorphic_ctype")


class OctoPrintEventSerializer(TelemetryEventSerializer):

    event_type = serializers.ChoiceField(
        choices=OctoprintEventType.choices, default=OctoprintEventType.STARTUP
    )
    event_source = serializers.ChoiceField(
        choices=EventSource.choices,
        default=EventSource.OCTOPRINT,
        read_only=True,
    )

    class Meta:
        model = OctoPrintEvent
        fields = "__all__"
        read_only_fields = ("id", "user", "event_source", "polymorphic_ctype")


class PrintNannyPluginEventSerializer(TelemetryEventSerializer):
    event_type = serializers.ChoiceField(
        choices=PrintNannyPluginEventType.choices,
        default=PrintNannyPluginEventType.MONITORING_START,
    )
    event_source = serializers.ChoiceField(
        choices=EventSource.choices,
        default=EventSource.OCTOPRINT,
        read_only=True,
    )

    class Meta:
        model = PrintNannyPluginEvent
        fields = "__all__"
        read_only_fields = ("id", "user", "event_source", "polymorphic_ctype")


class RemoteCommandEventSerializer(TelemetryEventSerializer):
    event_type = serializers.ChoiceField(
        choices=RemoteCommandEventType.choices,
        default=RemoteCommandEventType.REMOTE_COMMAND_FAILED,
    )
    event_source = serializers.ChoiceField(
        choices=EventSource.choices,
        default=EventSource.PRINT_NANNY_PLUGIN,
        read_only=True,
    )

    class Meta:
        model = RemoteCommandEvent
        fields = "__all__"
        read_only_fields = ("id", "user", "event_source", "polymorphic_ctype")


class TelemetryEventPolymorphicSerializer(PolymorphicSerializer):

    model_serializer_mapping = {
        TelemetryEvent: TelemetryEventSerializer,
        RemoteCommandEvent: RemoteCommandEventSerializer,
        PrintJobEvent: PrintJobEventSerializer,
        PrinterEvent: PrinterEventSerializer,
        OctoPrintEvent: OctoPrintEventSerializer,
        PrintNannyPluginEvent: PrintNannyPluginEventSerializer,
    }

    def to_representation(self, instance):
        if isinstance(instance, Mapping):
            resource_type = self._get_resource_type_from_mapping(instance)
            serializer = self._get_serializer_from_resource_type(resource_type)
        else:
            resource_type = self.to_resource_type(instance)
            serializer = self._get_serializer_from_model_or_instance(instance)

        ret = serializer.to_representation(instance)
        return ret
