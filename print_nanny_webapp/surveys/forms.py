from typing import TYPE_CHECKING, Optional
from django.contrib.auth import get_user_model
from django.forms import (
    ModelForm,
    CharField,
    MultipleChoiceField,
    CheckboxSelectMultiple,
    BooleanField,
    Textarea,
)
from .choices import PrimaryOS, MobileOS, VPNExperience, UserScale, PrinterSoftware

from .models import RemoteAccessSurvey1

if TYPE_CHECKING:
    from print_nanny_webapp.users.models import User as UserType
User = get_user_model()


class RemoteAccessSurvey1Form(ModelForm):
    opt_in = BooleanField(
        required=True,
        label="I agree to receive email updates about Print Nanny development, patch notes, and upcoming features.",
    )
    primary_os = MultipleChoiceField(
        widget=CheckboxSelectMultiple,
        choices=PrimaryOS.choices,
        label="Which computer operating system do you use? Select all that apply.",
    )
    printer_models_other = CharField(
        label="If you checked Other, please add details here",
        required=False,
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
        label="If you checked Other, please add details here",
        required=False,
    )

    printer_software = MultipleChoiceField(
        widget=CheckboxSelectMultiple,
        choices=PrinterSoftware.choices,
        label="Which printer management software do you use? Select all that apply",
    )

    printer_software_other = CharField(
        label="If you checked Other, please add details here or email leigh@printnanny.ai",
        required=False,
    )

    worst = CharField(
        label="If you could wave a magic wand and change ONE thing about 3D printing, what would that be?",
        widget=Textarea,
        help_text="Tell me what you hate most about 3D printing today",
        required=False,
    )

    class Meta:
        model = RemoteAccessSurvey1
        exclude = ["user", "user_agent"]

    def save(self, *args, **kwargs):
        request = kwargs.pop("request")
        if request is None:
            raise ValueError("request must be defined")
        # check to see if provided email matches user
        if request.user.is_anonymous:
            email = self.cleaned_data["email"]
            user = User.objects.filter(email=email).first()  # type: ignore
        else:
            user = request.user

        self.instance.user = user
        self.instance.user_agent = request.META
        return super(RemoteAccessSurvey1Form, self).save(*args, **kwargs)
