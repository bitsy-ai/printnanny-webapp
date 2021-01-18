from django.forms import ModelForm

from .models import (
    ProgressAlertSettings,
    DefectAlertSettings,
    RemoteControlCommandAlertSettings,
)


class ProgressAlertSettingsForm(ModelForm):
    class Meta:
        model = ProgressAlertSettings
        fields = ("enabled", "on_progress_percent", "alert_methods")


class DefectAlertSettingsForm(ModelForm):
    class Meta:
        model = DefectAlertSettings

        fields = ("enabled", "alert_methods")


class CommandAlertSettingsForm(ModelForm):
    class Meta:
        model = RemoteControlCommandAlertSettings
        unique_together = ("user", "alert_type")
        fields = (
            "enabled",
            "alert_methods",
            "start_print",
            "stop_print",
            "pause_print",
            "resume_print",
            "move_nozzle",
            "start_monitoring",
            "stop_monitoring",
        )
