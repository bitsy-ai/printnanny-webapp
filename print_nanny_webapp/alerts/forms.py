from enum import unique
from print_nanny_webapp.utils import fields
from print_nanny_webapp.users.models import GeeksToken
from django.forms import ModelForm

from .models import (
    ProgressAlertSettings,
    RemoteControlCommandAlertSettings,
    DiscordMethodSettings,
)


class ProgressAlertSettingsForm(ModelForm):
    class Meta:
        model = ProgressAlertSettings
        fields = ("enabled", "on_progress_percent", "alert_methods")


class CommandAlertSettingsForm(ModelForm):
    class Meta:
        model = RemoteControlCommandAlertSettings
        unique_together = ("user", "alert_type")
        fields = (
            "enabled",
            "alert_methods",
            "print_start",
            "print_stop",
            "print_pause",
            "print_resume",
            "monitoring_start",
            "monitoring_stop",
            "move_nozzle",
        )


class DiscordMethodSettingsForm(ModelForm):
    class Meta:
        model = DiscordMethodSettings
        unique_together = ("user", "target_id", "target_id_type")
        fields = ("target_id", "target_id_type")


class GeeksMethodSettingsForm(ModelForm):
    class Meta:
        model = GeeksToken
        fields = ("token", "octoprint_device")
