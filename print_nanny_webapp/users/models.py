from typing import Dict, Union, List

import djstripe
from djstripe.sync import sync_subscriber

from django.db.models import QuerySet
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.db import models

from rest_framework import serializers
from print_nanny_webapp.utils.fields import ChoiceArrayField
from print_nanny_webapp.users.managers import CustomUserManager
from print_nanny_webapp.users.enum import EmailListInterest
from print_nanny_webapp.workspaces.models import (
    WorkspaceUser,
    WorkspaceInvitation,
    Workspace,
)


class EmailWaitlist(models.Model):
    created_dt = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(unique=True)
    interest = models.CharField(
        choices=EmailListInterest.choices,
        default=EmailListInterest.PRINTNANNY,
        max_length=32,
    )


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
    # type annotations
    workspaces_workspaceuser: "QuerySet[WorkspaceUser]"
    workspaces_workspaceinvitation_sent_invitations: "QuerySet[WorkspaceInvitation]"
    workspaces_workspaceinvitation_invitations: "QuerySet[WorkspaceInvitation]"
    workspaces_workspace: "QuerySet[Workspace]"

    username = None  # type: ignore
    is_serviceuser = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_demo = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    email = models.EmailField(_("email address"), unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS: List[str] = []

    objects = CustomUserManager()  # type: ignore[assignment]

    def to_ghost_member(self):
        name = f"{self.first_name} {self.last_name}"
        data: Dict[str, Union[str, bool]] = {
            "name": name,
            "email": self.email,
            "subscribed": True,
        }
        return data

    def __str__(self):
        return self.email

    @property
    def events_channel(self) -> str:
        return f"events_{self.id}"

    @property
    def is_subscribed(self) -> bool:
        try:
            customer = djstripe.models.Customer.objects.get(subscriber=self)
            return customer.has_any_active_subscription()
        except djstripe.models.Customer.DoesNotExist:
            # try getting customer by email
            # if Customer checkout out anonymously and later created an acccount, subscriber will not be set
            try:
                customer = djstripe.models.Customer.objects.get(email=self.email)
                # set subscriber
                customer.subscriber = self
                customer.save()
                customer = sync_subscriber(self)
                return customer.has_any_active_subscription()

            except djstripe.models.Customer.DoesNotExist:
                return False

    @property
    def is_beta_tester(self) -> bool:
        return self.is_subscribed or self.is_superuser or self.is_staff or self.is_demo


class UserSettings(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, unique=True, primary_key=True
    )


class GhostMember(models.Model):
    """
    Periodically synced with Ghost's user/member API
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
