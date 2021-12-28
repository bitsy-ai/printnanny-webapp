from django.db import models

from print_nanny_webapp.utils.fields import ChoiceArrayField
from .choices import PrimaryOS, PrinterSoftware, UserScale, VPNExperience, NetworkType

# Create your models here.


class RemoteAccessSurvey1(models.Model):

    created_dt = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(unique=True)
    user = models.ForeignKey("users.User", null=True, on_delete=models.SET_NULL)

    primary_os = ChoiceArrayField(
        models.CharField(
            max_length=32,
            choices=PrimaryOS.choices,
            help_text="What kind of mobile phone do you use?",
        )
    )
    mobile_os = ChoiceArrayField(
        models.CharField(
            max_length=32,
            choices=PrimaryOS.choices,
            help_text="Which computer operating system do you use? Select all that apply.",
        )
    )

    vpn_experience = ChoiceArrayField(
        models.CharField(
            max_length=32,
            choices=VPNExperience.choices,
            help_text="Have you ever used a Virtual Private Network (VPN) or other remote access software? Select all that apply",
        )
    )

    network_type = ChoiceArrayField(
        models.CharField(
            max_length=32,
            choices=NetworkType.choices,
            help_text="What kind of network are your 3D printers on? Select all that apply",
        )
    )

    user_scale = ChoiceArrayField(
        models.CharField(
            max_length=32,
            choices=UserScale.choices,
            help_text="Select all that apply. Please email leigh@print-nanny.com or add extra details in the 'other' field below",
        )
    )
    user_scale_other = models.CharField(
        max_length=255, null=True, help_text="Add details here if you selected 'Other'"
    )

    printer_software = ChoiceArrayField(
        models.CharField(
            max_length=32,
            choices=PrinterSoftware.choices,
            help_text="Which 3D printer managers are you using? Select all that apply. Please email leigh@print-nanny.com if you are using software not on this list, or enter details in the 'other' box below.",
        )
    )
    printer_software_other = models.CharField(
        max_length=255, null=True, help_text="Add details here if you selected 'Other'"
    )

    user_agent = models.JSONField()
