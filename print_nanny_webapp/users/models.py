from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.db import models
from django.contrib.postgres.fields import ArrayField
from django import forms

from .managers import CustomUserManager

class ChoiceArrayField(ArrayField):
    """
    A postgres ArrayField that supports the choices property.

    Ref. https://gist.github.com/danni/f55c4ce19598b2b345ef.
    """

    def formfield(self, **kwargs):
        defaults = {
            "form_class": forms.MultipleChoiceField,
            "choices": self.base_field.choices,
            "widget": forms.CheckboxSelectMultiple
        }
        defaults.update(kwargs)
        return super(ArrayField, self).formfield(**defaults)

    def to_python(self, value):
        res = super().to_python(value)
        if isinstance(res, list):
            value = [self.base_field.to_python(val) for val in res]
        return value

    def validate(self, value, model_instance):
        if not self.editable:
            # Skip validation for non-editable fields.
            return

        if self.choices is not None and value not in self.empty_values:
            if set(value).issubset({option_key for option_key, _ in self.choices}):
                return
            raise exceptions.ValidationError(
                self.error_messages["invalid_choice"],
                code="invalid_choice",
                params={"value": value},
            )

        if value is None and not self.null:
            raise exceptions.ValidationError(self.error_messages["null"], code="null")

        if not self.blank and value in self.empty_values:
            raise exceptions.ValidationError(self.error_messages["blank"], code="blank")
        

class InviteRequest(models.Model):
    
    class PrinterBrand(models.TextChoices):
        PRUSA = 'PRUSA', 'Prusa'
        CREALITY = 'CREALITY', 'Creality'
        FLASHFORGE = 'FLASHFORGE', 'Flashforge'
        MONOPRICE = 'MONOPRICE', 'Monoprice'
        FORMLABS = 'FORMLABS', 'Formlabs'
        LULZBOT = 'LULZBOT', 'LulzBot'
        ULTIMAKER = 'ULTIMAKER', 'Ultimaker'
        MARKFORGED = 'MARKFORGED', 'Markforged'
        PEOPOLY = 'PEOPOLY', 'Peopoly'
        TOYBOX = 'TOYBOX', 'Toybox'
        MAKERBOT = 'MAKERBOT', 'Makerbot'
        DREMEL = 'DREMEL', 'Dremel'
        OTHER = 'OTHER', 'Other'

    class PrinterType(models.TextChoices):
        FDM = 'FDM', 'Fused filament fabrication (FFF & FDM)'
        SLA = 'SLA', 'Stereolithography (SLA)'

    class FilamentType(models.TextChoices
    ):
        PLA = 'PLA', 'PLA'
        PETG = 'PETG', 'PETG'
        ABS = 'ABS', 'ASA/ABS'
        BVOH = 'BVOH', 'Soluble (BVOH)'
        WOOD = 'WOOD', 'Wood Composite'
        METAL = 'Metal', 'Metal Composite'
        OTHER = 'OTHER', 'Other'

    class PrintFrequency(models.TextChoices):
        DAILY = 'DAILY', 'At least once per day'
        WEEKLY = 'WEEKLY', 'At least once per week'
        MONTHLY = 'MONTHLY', 'At least once per month'
        YEARLY = 'YEARLY', 'Occasionally, a few times a year'

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    referrer = models.CharField(max_length=255, help_text='How did you hear about us?')
    print_frequency = models.CharField(max_length=32, choices=PrintFrequency.choices)
    printer_models = ChoiceArrayField(
        models.CharField(max_length=32,choices=PrinterBrand.choices),
        help_text='Check all that apply',
    )
    num_printers = models.IntegerField()

    printer_models_other = models.CharField(max_length=255)
    filament_type = ChoiceArrayField(
        models.CharField(max_length=32, choices=FilamentType.choices),
        help_text='Check all that apply'
    )
    other = models.TextField(blank=True, null=True, help_text='If you checked "Other", say more about your printer and materials')

    business = models.BooleanField(help_text="Have you ever sold a finished print or source models?")
    num_employees = models.IntegerField(null=True, blank=True, help_text="If you peddle your wares, many people (besides you) support the business?")

    usage = models.TextField(help_text="Describe your 3D printer usage. What type of things to you make?")

    worst = models.TextField(blank=True, null=True, help_text='Alternatively, tell us the WORST part of 3D printing today')


class User(AbstractUser):
    username = None

    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(default=timezone.now)
    first_name = models.CharField(blank=True, null=True, max_length=30)
    last_name = models.CharField(blank=True, null=True, max_length=30)
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"email": self.email})