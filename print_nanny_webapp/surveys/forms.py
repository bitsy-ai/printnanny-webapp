from django.forms import ModelForm
from .models import RemoteAccessSurvey1


class RemoteAccessSurvey1Form(ModelForm):
    class Meta:
        model = RemoteAccessSurvey1
        exclude = ["user", "user_agent"]
