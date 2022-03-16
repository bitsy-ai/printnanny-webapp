from django import forms
from .models import ReferralCode, ReferralInvite


class PromoCodeForm(forms.Form):
    code = forms.CharField()


class StripeCheckoutForm(forms.Form):
    """
    Create a Stripe Checkout Session & then redirect to checkout page
    https://stripe.com/docs/payments/accept-a-payment?platform=web&ui=checkout
    """

    pass


class ReferralCodeCreateForm(forms.ModelForm):
    class Meta:
        model = ReferralCode
        fields = ("code",)


class ReferralInviteCreateForm(forms.ModelForm):
    class Meta:
        model = ReferralInvite
        fields = ("email",)
