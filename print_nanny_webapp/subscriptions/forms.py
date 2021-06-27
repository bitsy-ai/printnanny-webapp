from django import forms


class StripeCheckoutForm(forms.Form):
    """
    Create a Stripe Checkout Session & then redirect to checkout page
    https://stripe.com/docs/payments/accept-a-payment?platform=web&ui=checkout
    """

    pass
