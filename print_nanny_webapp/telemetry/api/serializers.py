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

class OctoprintJobSerializer(serializers.DictField):
    file = serializers.DictField(
        name = serializers.CharField(),
        path = serializers.CharField(),
        display = serializers.CharField(),
        origin = serializers.CharField(),
        size = serializers.IntegerField(),
        date = serializers.IntegerField()
    )
    estimatedPrintTime = serializers.FloatField()
    averagePrintTime = serializers.FloatField()
    lastPrintTime = serializers.FloatField()
    filament = serializers.DictField()

class OctoprintEnvironmentSerializer(serializers.DictField):
    os = serializers.DictField(
        id=serializers.CharField(),
        platform=serializers.CharField(),
        bits=serializers.CharField()
    )
    python = serializers.DictField(
        version=serializers.CharField(),
        pip=serializers.CharField(),
        virtualenv=serializers.CharField()
    )
    hardware = serializers.DictField(
        cores=serializers.IntegerField(),
        freq=serializers.FloatField(),
        ram=serializers.IntegerField(),
    )
    plugins = serializers.DictField(
        pi_support=serializers.DictField(
            model = serializers.CharField(),
            throttle_state = serializers.CharField(),
            octopi_version = serializers.CharField()
        )
    )

class TelemetryEventSerializer(serializers.ModelSerializer):
    print_session = serializers.StringRelatedField()
    event_type = serializers.ChoiceField(choices=TelemetryEventType.choices)
    environment = OctoprintEnvironmentSerializer()
    octoprint_job = OctoprintJobSerializer()
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
