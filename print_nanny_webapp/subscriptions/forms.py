from django import forms

import djstripe.models


class SubscriptionsPaymentForm(forms.Form):

    email = forms.EmailField()
    plan = forms.ModelChoiceField(queryset=djstripe.models.Plan.objects.all())
    stripe_source = forms.CharField(
        max_length="255", widget=forms.HiddenInput(), required=False
    )


class SubscriptionsPaymentIntentForm(forms.Form):
    pass
