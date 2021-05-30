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

class PlatformSerializer(serializers.DictField):
    id = serializers.StringField()

# 'environment': {'os': {'id': 'linux', 'platform': 'linux', 'bits': 32}, 'python': {'version': '3.7.3', 'pip': '21.1.2', 'virtualenv': '/home/pi/oprint'}, 
# 'hardware': {'cores': 4, 'freq': 1200.0, 'ram': 917016576}, 'plugins': 
# {'pi_support': {'model': 'Raspberry Pi 3 Model B Rev 1.2', 'throttle_state': '0x50000', 'octopi_version': '0.17.0'}}}, 'model_version': None}
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
