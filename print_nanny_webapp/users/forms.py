import logging
from typing import List
from allauth.account.forms import SignupForm
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.contrib.auth import forms as admin_forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _
from django import forms
from print_nanny_webapp.subscriptions.models import ReferralCode, ReferralSignup
from print_nanny_webapp.users.models import User, InviteRequest, UserSettings

logger = logging.getLogger(__name__)

# https://stackoverflow.com/a/3964824
# Create ModelForm based on the Group model.
class GroupAdminForm(forms.ModelForm):
    class Meta:
        model = Group
        exclude: List[str] = []

    # Add the users field.
    users = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),  # type: ignore[has-type]
        required=False,
        # Use the pretty 'filter_horizontal widget'.
        widget=FilteredSelectMultiple("users", False),
    )

    def __init__(self, *args, **kwargs):
        # Do the normal form initialisation.
        super(GroupAdminForm, self).__init__(*args, **kwargs)
        # If it is an existing group (saved objects have a pk).
        if self.instance.pk:
            # Populate the users field with the current Group users.
            self.fields["users"].initial = self.instance.user_set.all()

    def save_m2m(self):
        # Add the users to the Group.
        self.instance.user_set.set(self.cleaned_data["users"])

    def save(self, *args, **kwargs):
        # Default save
        instance = super(GroupAdminForm, self).save()
        # Save many-to-many data
        self.save_m2m()
        return instance


class UserSettingsForm(forms.ModelForm):
    class Meta:
        model = UserSettings
        exclude = ["user"]


class InviteRequestForm(forms.ModelForm):
    opt_in = forms.BooleanField(
        required=True,
        label="I agree to receive email updates about Print Nanny development, patch notes, and upcoming features.",
    )
    worst = forms.CharField(
        label="If you could wave a magic wand and change ONE thing about 3D printing, what would that be?",
        widget=forms.Textarea,
        help_text="Or tell us the WORST part about 3D printing",
        required=False,
    )

    class Meta:
        model = InviteRequest
        fields = [
            "first_name",
            "last_name",
            "email",
            "referrer",
            "usage",
            "num_printers",
            "business",
            "num_employees",
            "print_frequency",
            "filament_type",
            "printer_models",
            "other",
            "worst",
        ]


class UserChangeForm(admin_forms.UserChangeForm):
    class Meta(admin_forms.UserChangeForm.Meta):
        model = User
        fields = ("email",)


class UserCreationForm(SignupForm):

    error_messages = {
        "password_mismatch": _("The two password fields didn’t match."),
        "duplicate_email": _("An account with this email already exists"),
        "referral_code_invalid": _("Referral code was not found"),
    }

    field_order = ("email", "password1", "password2", "referral_code")

    referral_code = forms.CharField(
        label=_("Referral Code"),
        required=False,
    )

    class Meta:
        model = User
        fields = ("email", "password1", "password2", "referral_code")

    def clean_referral_code(self):
        referral_code = self.cleaned_data["referral_code"]
        if referral_code == "":
            return referral_code
        logger.info("Got referral_code %s", referral_code)
        try:
            ReferralCode.objects.get(code=referral_code)
        except ReferralCode.DoesNotExist:
            raise ValidationError(self.error_messages["referral_code_invalid"])
        return referral_code

    def save(self, request):
        logger.info("Using custom signup form")
        # Ensure you call the parent class's save.
        # .save() returns a User object.
        user = super(UserCreationForm, self).save(request)

        # Add your own processing here.
        referral_code = self.cleaned_data["referral_code"]
        if referral_code != "":
            code = ReferralCode.objects.get(code=referral_code)
            referral_signup = ReferralSignup.objects.create(
                code=code, referrer=code.user, recipient=user
            )
            logger.info("Created ReferralSignup %s", referral_signup)
        return user
