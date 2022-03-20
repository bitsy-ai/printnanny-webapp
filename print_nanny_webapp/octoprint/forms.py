from django import forms
from .models import OctoPrintSettings


class OctoPrintSettingsForm(forms.ModelForm):
    class Meta:
        model = OctoPrintSettings
        exclude = ("user",)
