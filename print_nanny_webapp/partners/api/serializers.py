from django.apps import apps
from rest_framework import serializers

OctoPrintDevice = apps.get_model('remote_control', 'OctoPrintDevice')

class GeeksMetadataSerializer(serializers.ModelSerializer):
    """
        Please do not include any personally-identifying info or sensitive info in partner serializers
    """
    class Meta:
        model = OctoPrintDevice
        fields = (
            "name", "model", "platform", 
            "octoprint_version",
            "plugin_version",
            "print_nanny_client_version"
        )
