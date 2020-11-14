from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.decorators import action

from drf_spectacular.utils import extend_schema_field
from drf_spectacular.types import OpenApiTypes

from ..models import OctoPrintEvent, PredictEvent, GcodeFile, PrintJob, PrinterProfile

@extend_schema_field(OpenApiTypes.STR)  # also takes basic python types
class JSONField(serializers.JSONField):
    pass

class OctoPrintEventSerializer(serializers.ModelSerializer):

    class Meta:
        model = OctoPrintEvent
        fields = '__all__'
        read_only_fields = ('user',)


class GcodeFileSerializer(serializers.ModelSerializer):

    class Meta:
        model = GcodeFile
        fields = '__all__'
        read_only_fields = ('user',)


    def update_or_create(self, validated_data, user):
        unique_together = ('user', 'file_hash')
        defaults = {k:v for k,v in validated_data.items() if k not in unique_together }
        unique_together_fields = { k:v for k,v in validated_data.items() if k in unique_together }
        return GcodeFile.objects.filter(
            **unique_together_fields,
            user=user
        ).update_or_create(**unique_together_fields, user=user, defaults=defaults)

class PrintJobSerializer(serializers.ModelSerializer):

    class Meta:
        model = PrintJob
        fields = '__all__'
        read_only_fields = ('user',)

class PrinterProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = PrinterProfile
        fields = '__all__'
        read_only_fields = ('user',)

    def update_or_create(self, validated_data, user):
        return PrinterProfile.objects.update_or_create(**validated_data, user=user)


class PredictEventSerializer(serializers.ModelSerializer):

    event_data = JSONField()

    class Meta:
        model = PredictEvent
        fields = (
            'dt', 'original_image', 'annotated_image', 'event_data', 'plugin_version', 'octoprint_version',
            'user', 'print_job'
        )

        read_only_fields = ('user',)
        