from anymail.message import AnymailMessage
from django.apps import AppConfig
from django.template.loader import render_to_string
from djstripe import webhooks

import logging

logger = logging.getLogger(__name__)

@webhooks.handler("customer.subscription.trial_will_end")
def subscriptions_trial_will_end(event):
    merge_data = {
        "FIRST_NAME": event.account_name or "Maker",
    }

    text_body = render_to_string("email/subscriptions_trial_ending_body.txt", merge_data)
    # html_body = render_to_string("email/subscriptions_trial_ending_body.html", merge_data)
    subject = render_to_string("email/subscriptions_trial_ending_subject.txt", merge_data)

    message = AnymailMessage(
        subject=subject,
        body=text_body,
        to=[event.customer.email],
    )
    # message.attach_alternative(html_body, "text/html")
    message.send()

@webhooks.handler("subscription_schedule.expiring")
def subscriptions_subscription_expiring(event):
    merge_data = {
        "FIRST_NAME": event.account_name or "Maker",
    }

    text_body = render_to_string("email/subscriptions_subscription_expiring_body.txt", merge_data)
    # html_body = render_to_string("email/subscriptions_subscription_expiring_body.html", merge_data)
    subject = render_to_string("email/subscriptions_subscription_expiring_subject.txt", merge_data)

    message = AnymailMessage(
        subject=subject,
        body=text_body,
        to=[event.customer.email],
    )
    # message.attach_alternative(html_body, "text/html")
    message.send()

@webhooks.handler("charge.failed")
def subscriptions_payment_failed(event):
    merge_data = {
        "FIRST_NAME": event.account_name or "Maker",
    }

    text_body = render_to_string("email/subscriptions_payment_failed_body.txt", merge_data)
    # html_body = render_to_string("email/subscriptions_subscription_expiring_body.html", merge_data)
    subject = render_to_string("email/subscriptions_payment_failed_subject.txt", merge_data)

    message = AnymailMessage(
        subject=subject,
        body=text_body,
        to=[event.customer.email],
    )
    # message.attach_alternative(html_body, "text/html")
    message.send()

# Payment action required is handled during the payment step inside the view
# There are both invoice.paid and invoice.payment_succeeded but docs lean on the first
# https://stripe.com/docs/billing/subscriptions/webhooks#tracking
@webhooks.handler("charge.succeeded")
def subscriptions_invoice_paid(event):
    merge_data = {
        "FIRST_NAME": event.customer.name or "Maker",
    }

    text_body = render_to_string("email/subscriptions_payment_succeeded_body.txt", merge_data)
    # html_body = render_to_string("email/subscriptions_subscription_expiring_body.html", merge_data)
    subject = render_to_string("email/subscriptions_payment_succeeded_subject.txt", merge_data)

    message = AnymailMessage(
        subject=subject,
        body=text_body,
        to=[event.customer.email],
    )
    # message.attach_alternative(html_body, "text/html")
    message.send()


class SubscriptionsConfig(AppConfig):
    name = "print_nanny_webapp.subscriptions"
