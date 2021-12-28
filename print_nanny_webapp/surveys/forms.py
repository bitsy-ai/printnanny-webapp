from django.forms import (
    ModelForm,
    CharField,
    MultipleChoiceField,
    CheckboxSelectMultiple,
)
from crispy_forms.helper import FormHelper, Layout
from crispy_forms.layout import Div, Field
from print_nanny_webapp.utils.fields import ChoiceArrayField
from .choices import PrimaryOS, MobileOS

from .models import RemoteAccessSurvey1


class Row(Div):
    css_class = "form-row"


class RemoteAccessSurvey1Form(ModelForm):
    mobile_os = MultipleChoiceField(
        widget=CheckboxSelectMultiple,
        choices=PrimaryOS.choices,
        label="What kind of mobile phone do you use? Select all that apply",
    )
    mobile_os = MultipleChoiceField(
        widget=CheckboxSelectMultiple,
        choices=MobileOS.choices,
        label="Which computer operating system do you use? Select all that apply.",
    )

    class Meta:
        model = RemoteAccessSurvey1
        exclude = ["user", "user_agent"]
