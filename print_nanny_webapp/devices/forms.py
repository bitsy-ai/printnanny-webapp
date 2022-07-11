from django.apps import apps
from django.forms import ModelForm


DeviceSettings = apps.get_model("devices", "DeviceSettings")


class DeviceSettingsForm(ModelForm):
    class Meta:
        model = DeviceSettings
        fields = ("cloud_video_enabled", "telemetry_enabled")
