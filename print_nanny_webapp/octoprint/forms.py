from django import forms
from .models import OctoPrintSettings


class OctoPrintSettingsForm(forms.ModelForm):
    class Meta:
        model = OctoPrintSettings
        fields = ("octoprint_enabled", "events_enabled", "sync_backups")
