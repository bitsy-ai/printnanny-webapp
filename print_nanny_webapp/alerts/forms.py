from enum import unique
from print_nanny_webapp.utils import fields
from print_nanny_webapp.partners.models import GeeksToken
from django.forms import ModelForm, Form
from django.forms import modelformset_factory
from .models import AlertSettings


class AlertTestForm(Form):
    pass

class AlertSettingsForm(ModelForm):
    class Meta:
        model = AlertSettings
        fields = ("event_types", "print_progress_percent")


class AlertMethodSettingsForm(ModelForm):
    class Meta:
        model = AlertSettings
        fields = ("alert_methods", "discord_webhook")
