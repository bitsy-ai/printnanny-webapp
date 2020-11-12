from django.contrib.auth import get_user_model
from rest_framework import serializers

from ..models import OctoPrintEvent, PredictEvent

class OctoPrintEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = OctoPrintEvent
        fields = '__all__'


        # extra_kwargs = {
        #     "url": {"view_name": "api:user-detail", "lookup_field": "id"}
        # }

class PredictEventSerializer(serializers.ModelSerializer):

    class Meta:
        model = PredictEvent
        fields = '__all__'

        read_only_fields = ('user', 'printer', 'print_job')
        
        # extra_kwargs = {
        #     "url": {"view_name": "api:user-detail", "lookup_field": "id"}
        # }

