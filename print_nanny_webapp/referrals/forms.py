from django import forms
from .models import ReferralCode, ReferralInvite


class ReferralCodeCreateForm(forms.ModelForm):
    class Meta:
        model = ReferralCode
        fields = ("code",)


class ReferralInviteCreateForm(forms.ModelForm):
    class Meta:
        model = ReferralInvite
        fields = ("email",)
