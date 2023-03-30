import logging

from django.apps import apps
from django.contrib.auth import get_user_model
from rest_framework import serializers
from print_nanny_webapp.events.models.alerts import EmailAlertSettings, PrintJobAlert


logger = logging.getLogger(__name__)

Pi = apps.get_model("devices", "Pi")
User = get_user_model()


class EmailAlertSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailAlertSettings
        fields = "__all__"
        read_only_fields = (
            "created_dt",
            "updated_dt",
            "user",
        )


class PrintJobAlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrintJobAlert
        fields = "__all__"
        read_only_fields = ("user", "email_message_id", "celery_task_id", "id")
