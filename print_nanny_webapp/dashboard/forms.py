

from django import forms
from crispy_forms.helper import FormHelper

from django.core.files.uploadedfile import SimpleUploadedFile

class TimelapseUploadForm(forms.Form):

    video_file = forms.FileField(label="Select a video to upload", required=True)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'