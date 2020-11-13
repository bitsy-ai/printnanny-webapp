from django.contrib.auth import get_user_model
from rest_framework import serializers
from drf_spectacular.utils import extend_schema_field
from drf_spectacular.types import OpenApiTypes

from ..models import OctoPrintEvent, PredictEvent

@extend_schema_field(OpenApiTypes.STR)  # also takes basic python types
class JSONField(serializers.JSONField):
    pass
    # def to_representation(self, value):


class OctoPrintEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = OctoPrintEvent
        fields = '__all__'


        # extra_kwargs = {
        #     "url": {"view_name": "api:user-detail", "lookup_field": "id"}
        # }

class PredictEventSerializer(serializers.ModelSerializer):

    event_data = JSONField()
    class Meta:
        model = PredictEvent
        fields = '__all__'

        read_only_fields = ('user', 'printer', 'print_job')
        
        # extra_kwargs = {
        #     "url": {"view_name": "api:user-detail", "lookup_field": "id"}
        # }

