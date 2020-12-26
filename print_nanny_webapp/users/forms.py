from django.contrib.auth import forms as admin_forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django import forms
from django.contrib.postgres.fields import ArrayField

from print_nanny_webapp.users.models import InviteRequest, UserSettings

User = get_user_model()


class UserSettingsForm(forms.ModelForm):
    class Meta:
        model = UserSettings
        exclude = ["user"]


class InviteRequestForm(forms.ModelForm):
    opt_in = forms.BooleanField(
        required=True,
        label="I agree to receive email updates about Print Nanny development, patch notes, and upcoming features."
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


class UserCreationForm(admin_forms.UserCreationForm):

    error_message = admin_forms.UserCreationForm.error_messages.update(
        {"duplicate_email": _("An account with this email already exists")}
    )

    class Meta(admin_forms.UserCreationForm.Meta):
        model = User
        fields = ("email",)

    def clean_username(self):
        email = self.cleaned_data["email"]

        try:
            User.objects.get(email=email)
        except User.DoesNotExist:
            return email

        raise ValidationError(self.error_messages["duplicate_email"])
