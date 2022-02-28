import logging
from allauth.account.forms import SignupForm
from django.contrib.auth import forms as admin_forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django import forms
from print_nanny_webapp.referrals.models import ReferralCode, ReferralSignup
from print_nanny_webapp.users.models import User, InviteRequest, UserSettings

logger = logging.getLogger(__name__)


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

    error_messages = (
        admin_forms.UserCreationForm.error_messages
        | {"duplicate_email": _("An account with this email already exists")}
        | {"referral_code_invalid": _("Referral code was not found")}
    )

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
            ReferralCode.objects.get(code=referral_code)  # type: ignore
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
