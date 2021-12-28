from django.forms import (
    ModelForm,
    CharField,
    MultipleChoiceField,
    CheckboxSelectMultiple,
)
from crispy_forms.helper import FormHelper, Layout
from crispy_forms.layout import Div, Field
from .choices import PrimaryOS, MobileOS, VPNExperience, UserScale, PrinterSoftware

from .models import RemoteAccessSurvey1


class Row(Div):
    css_class = "form-row"


class RemoteAccessSurvey1Form(ModelForm):
    primary_os = MultipleChoiceField(
        widget=CheckboxSelectMultiple,
        choices=PrimaryOS.choices,
        label="Which computer operating system do you use? Select all that apply.",
    )
    mobile_os = MultipleChoiceField(
        widget=CheckboxSelectMultiple,
        choices=MobileOS.choices,
        label="What kind of mobile phone do you use? Select all that apply",
    )
    vpn_experience = MultipleChoiceField(
        widget=CheckboxSelectMultiple,
        choices=VPNExperience.choices,
        label="Have you ever used a Virtual Private Network (VPN) or other remote access software? Select all that apply",
    )

    user_scale = MultipleChoiceField(
        widget=CheckboxSelectMultiple,
        choices=UserScale.choices,
        label="What are your goals for using Print Nanny OS + Network?",
    )

    user_scale_other = CharField(
        label="If you checked Other, please add details here or email leigh@print-nanny.com",
        required=False,
    )

    printer_software = MultipleChoiceField(
        widget=CheckboxSelectMultiple,
        choices=PrinterSoftware.choices,
        label="Which printer management software do you use? Select all that apply",
    )

    printer_software_other = CharField(
        label="If you checked Other, please add details here or email leigh@print-nanny.com",
        required=False,
    )

    class Meta:
        model = RemoteAccessSurvey1
        exclude = ["user", "user_agent"]
