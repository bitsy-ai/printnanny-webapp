from django.db import models

from print_nanny_webapp.utils.fields import ChoiceArrayField
from .choices import (
    PrimaryOS,
    PrinterSoftware,
    UserScale,
    VPNExperience,
    NetworkType,
    MobileOS,
)

# Create your models here.


class RemoteAccessSurvey1(models.Model):
    class PrintFrequency(models.TextChoices):
        DAILY = "DAILY", "At least once per day"
        WEEKLY = "WEEKLY", "At least once per week"
        MONTHLY = "MONTHLY", "At least once per month"
        YEARLY = "YEARLY", "Occasionally, a few times a year"

    class PrinterBrand(models.TextChoices):
        PRUSA = "PRUSA", "Prusa"
        CREALITY = "CREALITY", "Creality"
        FLASHFORGE = "FLASHFORGE", "Flashforge"
        MONOPRICE = "MONOPRICE", "Monoprice"
        FORMLABS = "FORMLABS", "Formlabs"
        LULZBOT = "LULZBOT", "LulzBot"
        ULTIMAKER = "ULTIMAKER", "Ultimaker"
        MARKFORGED = "MARKFORGED", "Markforged"
        PEOPOLY = "PEOPOLY", "Peopoly"
        TOYBOX = "TOYBOX", "Toybox"
        MAKERBOT = "MAKERBOT", "Makerbot"
        DREMEL = "DREMEL", "Dremel"
        OTHER = "OTHER", "Other"

    created_dt = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    referrer = models.CharField(
        max_length=255, help_text="How did you hear about Print Nanny?"
    )
    user = models.ForeignKey("users.User", null=True, on_delete=models.SET_NULL)

    print_frequency = models.CharField(max_length=32, choices=PrintFrequency.choices)
    num_printers = models.PositiveSmallIntegerField()
    business = models.BooleanField(
        help_text="Do you operate a 3D printing or model design business?"
    )
    usage = models.TextField(
        help_text="Describe your 3D printer usage. What type of things to you make?"
    )
    printer_models = ChoiceArrayField(
        models.CharField(max_length=32, choices=PrinterBrand.choices),
        help_text="Check all that apply",
    )
    printer_models_other = models.CharField(max_length=255, null=True)

    primary_os = ChoiceArrayField(
        models.CharField(
            max_length=32,
            choices=PrimaryOS.choices,
        )
    )
    mobile_os = ChoiceArrayField(
        models.CharField(
            max_length=32,
            choices=MobileOS.choices,
        )
    )

    vpn_experience = ChoiceArrayField(
        models.CharField(
            max_length=32,
            choices=VPNExperience.choices,
        )
    )

    network_type = ChoiceArrayField(
        models.CharField(
            max_length=32,
            choices=NetworkType.choices,
            help_text="What kind of network are your 3D printers on? Select all that apply",
        )
    )
    worst = models.TextField(
        blank=True,
        null=True,
        help_text="Tell me what you hate most about 3D printing today",
    )
    user_scale = ChoiceArrayField(
        models.CharField(
            max_length=32,
            choices=UserScale.choices,
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
