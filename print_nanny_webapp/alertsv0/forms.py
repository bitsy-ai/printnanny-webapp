from django.apps import apps
from django.forms import ModelForm, Form


AlertSettings = apps.get_model("alerts", "AlertSettings")


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
