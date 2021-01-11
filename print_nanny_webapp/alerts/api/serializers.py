from rest_framework import serializers

from ..models import ManualVideoUploadAlert, RemoteControlCommandAlert

class RemoteControlCommandAlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = RemoteControlCommandAlert
        fields = [field.name for field in ManualVideoUploadAlert._meta.fields] + ["url"]
        extra_kwargs = {
            "url": {"view_name": "api:alert-message-detail", "lookup_field": "id"}
        } 



class ManualVideoUploadAlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManualVideoUploadAlert
        fields = [field.name for field in ManualVideoUploadAlert._meta.fields] + ["url"]
        extra_kwargs = {
            "url": {"view_name": "api:alert-message-detail", "lookup_field": "id"}
        }
        read_only_fields = ("user",)

