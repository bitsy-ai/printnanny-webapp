import logging

from rest_framework import serializers

from rest_polymorphic.serializers import PolymorphicSerializer

from ..models import ManualVideoUploadAlert, RemoteControlCommandAlert, Alert

logger = logging.getLogger(__name__)

class AlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alert
        fields = ["created_dt", "updated_dt", "user", "dismissed"] 
        read_only_fields = ("user",)


class RemoteControlCommandAlertSerializer(serializers.ModelSerializer):

    class Meta:
        model = RemoteControlCommandAlert
        fields = ["created_dt", "updated_dt", "user", "dismissed", "alert_type", "css_class", "alert_type"] 
        read_only_fields = ("user",)
 
class ManualVideoUploadAlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManualVideoUploadAlert
        fields = ["created_dt", "updated_dt", "user", "dismissed", "alert_type"]
        read_only_fields = ("user",)

class AlertPolymorphicSerializer(PolymorphicSerializer):
    resource_type_field_name = 'type'

    model_serializer_mapping = {
        Alert: AlertSerializer,
        RemoteControlCommandAlert: RemoteControlCommandAlertSerializer,
        ManualVideoUploadAlert: ManualVideoUploadAlertSerializer
    }

    def to_resource_type(self, model_or_instance):

        logger.info(model_or_instance)
        return model_or_instance.alert_type