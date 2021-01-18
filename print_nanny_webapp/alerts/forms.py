from django.forms import ModelForm

from .models import (ProgressAlertSettings, DefectAlertSettings, RemoteControlCommandAlertSettings)

class ProgressAlertSettingsForm(ModelForm):
    class Meta:
        model = ProgressAlertSettings
        fields = ('enabled', 'on_progress_percent')

class DefectAlertSettingsForm(ModelForm):
    class Meta:
        model = DefectAlertSettings

        fields = ('enabled',)

class CommandAlertSettingsForm(ModelForm):

    class Meta:
        model = RemoteControlCommandAlertSettings
        fields = ('enabled',)