from datetime import datetime
from django.http.response import JsonResponse
import stripe
import json, logging
from django.http import HttpResponse, HttpRequest
from django.contrib.auth import get_user_model
from django.template.response import TemplateResponse
from django.shortcuts import redirect
from djstripe import webhooks

import djstripe.models
import djstripe.settings
from anymail.message import AnymailMessage
from django.template.loader import render_to_string
from stripe.api_resources import line_item

from print_nanny_webapp.dashboard.views import DashboardView
from print_nanny_webapp.remote_control.models import OctoPrintDevice

logger = logging.getLogger(__name__)
User = get_user_model()


class SubscriptionsListView(DashboardView):
    template_name = "subscriptions/list.html"
    # template_name = "components/base-ui/cards.html"

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        customer = djstripe.models.Customer.objects.get(subscriber=self.request.user)

        # Populate template with current subscriptions and stripe public key
        ctx["STRIPE_PUBLIC_KEY"] = djstripe.settings.STRIPE_PUBLIC_KEY
        ctx["SUBSCRIPTIONS"] = customer.subscriptions.all().order_by('-created')
        ctx["PRODUCTS"] = djstripe.models.Product.objects.filter(active=True)
        for p in ctx["PRODUCTS"]:
            p.prices_list = p.prices.filter(active=True)

        try:
            ctx["DEVICES"] = OctoPrintDevice.objects.get(user=self.request.user)
        except OctoPrintDevice.DoesNotExist:
            ctx["DEVICES"] = None

        return ctx


def subscriptions_payment_intent_view_create(request: HttpRequest):
    if request.method != "POST":
        return redirect("subscriptions:list")

    data = json.loads(request.body)

    customer, created = djstripe.models.Customer.objects.get(subscriber=request.user)
    session = stripe.checkout.Session.create(
        customer=customer.id,
        payment_method_types=["card"],
        mode="subscription",
        success_url="http://localhost:8000/subscriptions",
        cancel_url="http://localhost:8000/subscriptions/asdf",
        line_items=[{
            "price": data["price_id"],
            "quantity": 1,
        }],
        api_key=djstripe.settings.STRIPE_SECRET_KEY,
    )
    return JsonResponse({"session_id": session.id}, status=200)

@webhooks.handler("customer.subscription.trial_will_end")
def subscriptions_trial_will_end(event):
    logger.info(f"Sending email to user {event.customer.email} that their trial is ending")
    user = User.objects.get(email=event.customer.email)

    merge_data = {
        "FIRST_NAME": user.first_name or "Maker",
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
    logger.info(f"User {event.customer.email} subscription <X> is expiring, sending email")
    user = User.objects.get(email=event.customer.email)

    merge_data = {
        "FIRST_NAME": user.first_name or "Maker",
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

# @webhooks.handler("charge.failed")
@webhooks.handler("invoice.payment_failed")
def subscriptions_payment_failed(event):
    logger.info(f"User's {event.customer.email} subscription <X> payment <X> failed, sending email")
    user = User.objects.get(email=event.customer.email)

    merge_data = {
        "FIRST_NAME": user.first_name or "Maker",
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
# @webhooks.handler("charge.succeeded")
@webhooks.handler("invoice.paid")
def subscriptions_invoice_paid(event):
    # TODO: When a trial was paid, do nothing
    logger.info(f"User {event.customer.email} paid subscription <X> successfully, sending email")
    user = User.objects.get(email=event.customer.email)

    merge_data = {
        "FIRST_NAME": user.first_name or "Maker",
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
