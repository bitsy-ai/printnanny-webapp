from anymail.message import AnymailMessage
from django.apps import AppConfig
from django.contrib.auth import get_user_model
from django.template.loader import render_to_string
from django.urls import reverse
from djstripe import webhooks

# from .models import User

# import djstripe.models
import logging

logger = logging.getLogger(__name__)

@webhooks.handler("customer.subscription.trial_will_end")
def subscriptions_trial_will_end(event, **kwargs):
    print("*** subscription trial ends! ***")

@webhooks.handler("customer.subscription.payment_failed")
def subscriptions_payment_failed(event, **kwargs):
    print("*** subscription payment failed! ***")

@webhooks.handler("customer.subscription.deleted")
def subscriptions_cancelled(event):
    # user = User.objects.get(email=event.customer.email)
    merge_data = {
        "REPORT_URL": reverse("subscriptions:list"),
        "FIRST_NAME": event.customer.name or "Maker",
    }

    text_body = render_to_string("email/timelapse_alert_body.txt", merge_data)
    html_body = render_to_string("email/timelapse_alert_body.html", merge_data)
    subject = render_to_string("email/timelapse_alert_subject.txt", merge_data)

    message = AnymailMessage(
        subject=subject,
        body=text_body,
        to=[event.customer.email],
        tags=["default-print-alert"],  # Anymail extra in constructor
    )
    message.attach_alternative(html_body, "text/html")
    message.send()

@webhooks.handler("subscription_schedule.expiring")
def subscriptions_subscription_expiring(event, **kwargs):
    print("*** subscription expiring! ***")

@webhooks.handler("invoice.upcoming")
def subscriptions_trial_will_end(event, **kwargs):
    print("*** invoice upcoming! ***")

# Payment action required is handled during the payment step inside the view
# There are both invoice.paid and invoice.payment_succeeded but docs lean on the first
# https://stripe.com/docs/billing/subscriptions/webhooks#tracking
@webhooks.handler("invoice.paid")
def subscriptions_invoice_paid(event, **kwargs):
    print("*** invoice paid! ***")
    # djstripe.models.Subscription.get


class SubscriptionsConfig(AppConfig):
    name = "print_nanny_webapp.subscriptions"
