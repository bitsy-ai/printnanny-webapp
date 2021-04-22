import binascii
import os
from uuid import uuid4
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.db import models
from django.contrib.postgres.fields import ArrayField
from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator
from rest_framework import serializers
from anymail.message import AnymailMessage
from rest_framework.authtoken.models import Token

from print_nanny_webapp.utils.fields import ChoiceArrayField

import json

from .managers import CustomUserManager, InviteRequestManager


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
    username = None

    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(default=timezone.now)
    first_name = models.CharField(blank=True, null=True, max_length=30)
    last_name = models.CharField(blank=True, null=True, max_length=30)
    email = models.EmailField(_("email address"), unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def to_ghost_member(self):
        return {
            "name": f"{self.first_name} {self.last_name}",
            "email": self.email,
            "subscribed": True,
        }

    def __str__(self):
        return self.email


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


class GeeksToken(models.Model):
    # Grabbed code from rest_framework Token model

    key = models.UUIDField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    octoprint_device = models.OneToOneField("remote_control.OctoPrintDevice", null=True, on_delete=models.CASCADE)

    class Meta:
        # Work around for a bug in Django:
        # https://code.djangoproject.com/ticket/19422
        #
        # Also see corresponding ticket:
        # https://github.com/encode/django-rest-framework/issues/705
        abstract = 'rest_framework.authtoken' not in settings.INSTALLED_APPS

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key()
        return super().save(*args, **kwargs)

    @classmethod
    def generate_key(cls):
        return uuid4()

    def __str__(self):
        return self.key
