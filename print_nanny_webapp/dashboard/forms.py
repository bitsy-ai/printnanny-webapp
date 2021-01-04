import logging
from django import forms
from django.apps import apps

from crispy_forms.helper import FormHelper

from django.core.files.uploadedfile import SimpleUploadedFile

logger = logging.getLogger(__name__)
RemoteControlCommand = apps.get_model("remote_control", "RemoteControlCommand")


class TimelapseUploadForm(forms.Form):

    video_file = forms.FileField(label="Select a video file (.mp4)", required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"


class TimelapseCancelForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"


class FeedbackForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"


class AppNotificationForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"


class RemoteControlCommandForm(forms.Form):

    command = forms.ChoiceField()

    def __init__(self, *args, **kwargs):

        # django metaclass magic to construct fields

        command_choices = kwargs.pop("command_choices")
        super().__init__(*args, **kwargs)
        self.fields["command"].choices = [(x.label, x.value) for x in command_choices]
