from print_nanny_webapp.subscriptions.models import MemberBadge
from typing import Dict, Union, List
from django.apps import apps
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.db import models
from rest_framework import serializers
from anymail.message import AnymailMessage
from rest_framework.authtoken.models import Token

from print_nanny_webapp.utils.fields import ChoiceArrayField
from print_nanny_webapp.subscriptions.models import MemberBadge

import json

from .managers import CustomUserManager


class InviteRequest(models.Model):
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

    class PrinterType(models.TextChoices):
        FDM = "FDM", "Fused filament fabrication (FFF & FDM)"
        SLA = "SLA", "Stereolithography (SLA)"

    class FilamentType(models.TextChoices):
        PLA = "PLA", "PLA"
        PETG = "PETG", "PETG"
        ABS = "ABS", "ASA/ABS"
        BVOH = "BVOH", "Soluble (BVOH)"
        WOOD = "WOOD", "Wood Composite"
        METAL = "Metal", "Metal Composite"
        OTHER = "OTHER", "Other"

    class PrintFrequency(models.TextChoices):
        DAILY = "DAILY", "At least once per day"
        WEEKLY = "WEEKLY", "At least once per week"
        MONTHLY = "MONTHLY", "At least once per month"
        YEARLY = "YEARLY", "Occasionally, a few times a year"

    created_dt = models.DateTimeField(auto_now_add=True)
    invited = models.BooleanField(default=False)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    referrer = models.CharField(max_length=255, help_text="How did you hear about us?")
    print_frequency = models.CharField(max_length=32, choices=PrintFrequency.choices)
    printer_models = ChoiceArrayField(
        models.CharField(max_length=32, choices=PrinterBrand.choices),
        help_text="Check all that apply",
    )
    num_printers = models.IntegerField()

    printer_models_other = models.CharField(max_length=255)
    filament_type = ChoiceArrayField(
        models.CharField(max_length=32, choices=FilamentType.choices),
        help_text="Check all that apply",
    )
    other = models.TextField(
        blank=True,
        null=True,
        help_text='If you checked "Other", say more about your printer and materials',
    )

    business = models.BooleanField(
        help_text="Have you ever sold a finished print or source models?"
    )
    num_employees = models.IntegerField(
        null=True,
        blank=True,
        help_text="If you peddle your wares, many people (besides you) support the business?",
    )

    usage = models.TextField(
        help_text="Describe your 3D printer usage. What type of things to you make?"
    )

    worst = models.TextField(
        blank=True,
        null=True,
        help_text="Alternatively, tell us the WORST part of 3D printing today",
    )

    def _admin_email_notification(self):
        """
        Sends emails to admins in settings.BETA_NOTIFY_EMAIL = ['leigh+testing@bitsy.ai']
        """

        subject = "New invite request"
        text_body = json.dumps(InviteRequestSerializer(self).data, indent=2)

        message = AnymailMessage(
            subject=subject,
            body=text_body,
            to=settings.BETA_NOTIFY_EMAIL,
            tags=["print-nanny-beta-request"],  # Anymail extra in constructor
        )
        return message.send()

    def to_ghost_member(self):
        return {
            "name": f"{self.first_name} {self.last_name}",
            "email": self.email,
            "subscribed": True,
        }


class InviteRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = InviteRequest
        fields = "__all__"


class User(AbstractUser):
    username = None  # type: ignore

    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(default=timezone.now)  # type: ignore
    first_name = models.CharField(blank=True, null=True, max_length=30)  # type: ignore
    last_name = models.CharField(blank=True, null=True, max_length=30)  # type: ignore
    email = models.EmailField(_("email address"), unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS: List[str] = []

    objects = CustomUserManager()  # type: ignore

    def to_ghost_member(self):
        name = f"{self.first_name} {self.last_name}"  # type: ignore
        data: Dict[str, Union[str, bool]] = {
            "name": name,
            "email": self.email,
            "subscribed": True,
        }

    def __str__(self):
        return self.email

    # @property
    # def is_subscribed(self) -> bool:
    #     customer = djstripe.models.Customer.objects.get(subscriber=self)
    #     return customer.has_any_active_subscription()

    @property
    def is_paid_beta_tester(self) -> bool:
        badge = self.member_badges.filter(type=MemberBadge.Types.PAID_BETA).first()
        return badge is not None

    @property
    def is_free_beta_tester(self) -> bool:
        badge = self.member_badges.filter(type=MemberBadge.Types.FREE_BETA).first()
        return badge is not None

    @property
    def is_beta_tester(self) -> bool:
        return self.is_free_beta_tester or self.is_paid_beta_tester


class UserSettings(models.Model):

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, unique=True, primary_key=True
    )


class GhostMember(models.Model):
    """
    Periodically synced with Ghost's user/member API @ help.print-nanny.com
    """

    class SiteChoices(models.TextChoices):
        BLOG = "blog", "blog.print-nanny.com"
        HELP = "help", "help.print-nanny.com"

    site = models.CharField(max_length=32, choices=SiteChoices.choices)
    email = models.EmailField(db_index=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True, null=True)
    invite_request = models.OneToOneField(
        InviteRequest, on_delete=models.CASCADE, unique=True, null=True
    )

    uuid = models.CharField(max_length=255)
    email_count = models.IntegerField()
    email_opened_count = models.IntegerField()
    email_open_rate = models.FloatField(null=True)
    subscribed = models.BooleanField(default=True)
