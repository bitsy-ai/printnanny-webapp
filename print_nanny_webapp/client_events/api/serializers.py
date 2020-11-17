from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.decorators import action

from drf_spectacular.utils import extend_schema_field
from drf_spectacular.types import OpenApiTypes

from ..models import OctoPrintEvent, PredictEvent, GcodeFile, PrintJob, PrinterProfile, PredictEventFile

# @extend_schema_field(OpenApiTypes.OBJECT)  # also takes basic python types
# class JSONField(serializers.JSONField):
#     pass

class OctoPrintEventSerializer(serializers.ModelSerializer):

    class Meta:
        model = OctoPrintEvent
        fields = '__all__'
        read_only_fields = ('user',)
        extra_kwargs = {
            'url': {'view_name': 'octoprint_events_list', 'lookup_field': 'id'},
        }
    


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

        extra_kwargs = {
            "url": {"view_name": "api:printer-profile-detail", "lookup_field": "id"}
        }
    def update_or_create(self, validated_data, user):
        unique_together = ('user', 'name',)
        defaults = {k:v for k,v in validated_data.items() if k not in unique_together }
        unique_together_fields = { k:v for k,v in validated_data.items() if k in unique_together }
        return PrinterProfile.objects.filter(
            **unique_together_fields,
            user=user
        ).update_or_create(**unique_together_fields, user=user, defaults=defaults)


class PredictEventFileSerializer(serializers.ModelSerializer):

    class Meta:
        model = PredictEventFile
        fields = '__all__'

        

class PredictEventSerializer(serializers.ModelSerializer):

    #event_data = JSONField()

    class Meta:
        model = PredictEvent
        fields = '__all__'

        read_only_fields = ('user',)
        