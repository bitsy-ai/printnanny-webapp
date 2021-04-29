import logging
import inspect

from django.apps import apps
from django.urls import reverse
from rest_framework import serializers
from django.contrib.humanize.templatetags.humanize import naturaltime


logger = logging.getLogger(__name__)

Alert = apps.get_model("alerts", "AlertMessage")
AlertSettings = apps.get_model("alerts", "AlertSettings")


class AlertSerializer(serializers.ModelSerializer):

    time = serializers.SerializerMethodField()

    def get_time(self, obj):
        return naturaltime(obj.updated_dt)

    class Meta:
        model = Alert
        fields = "__all__"
        read_only_fields = ("user",)



class AlertBulkRequestSerializer(serializers.Serializer):
    """
    Serializer used in POST /api/alerts/seen and POST /api/alerts/dismiss requests
    """

    ids = serializers.ListField(child=serializers.IntegerField())


class AlertBulkResponseSerializer(serializers.Serializer):
    """
    Serializer used in POST /api/alerts/seen and POST /api/alerts/dismiss requests
    """

    received = serializers.IntegerField()
    updated = serializers.IntegerField()
