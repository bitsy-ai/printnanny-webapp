from enum import unique
from print_nanny_webapp.utils import fields
from print_nanny_webapp.partners.models import GeeksToken
from django.forms import ModelForm
from django.forms import modelformset_factory
from .models import AlertEventSettings


class AlertEventSettingsForm(ModelForm):
    class Meta:
        model = AlertEventSettings
        fields = ("event_types", "print_progress_percent")


class AlertMethodSettingsForm(ModelForm):
    class Meta:
        model = AlertEventSettings
        fields = ("alert_methods", "discord_webhook")
