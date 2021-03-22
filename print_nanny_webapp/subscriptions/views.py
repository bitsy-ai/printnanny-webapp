from datetime import datetime
from django.http.response import JsonResponse
import stripe
import json, logging
from django.http import HttpResponse, HttpRequest
from django.contrib.auth import get_user_model
from django.template.response import TemplateResponse
from djstripe import webhooks

import djstripe.models
import djstripe.settings
from anymail.message import AnymailMessage
from django.template.loader import render_to_string

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
        ctx = {"STRIPE_PUBLIC_KEY": djstripe.settings.STRIPE_PUBLIC_KEY}
        return TemplateResponse(request, SubscriptionsListView.template_name, ctx)

    intent = None
    data = json.loads(request.body)
    # TODO: Put this in the form
    data["plan"] = djstripe.models.Plan.objects.first().id
    try:
        customer, created = djstripe.models.Customer.get_or_create(subscriber=request.user)
        # TODO: This is just ugly
        if "payment_method_id" in data:
            customer.add_payment_method(data["payment_method_id"])

            # Using the Stripe API, create a subscription for this customer,
            # using the customer's default payment source
            stripe_subscription = stripe.Subscription.create(
                customer=customer.id,
                items=[{"plan": data["plan"]}],
                collection_method="charge_automatically",
                # tax_percent=15,
                api_key=djstripe.settings.STRIPE_SECRET_KEY,
            )

            # Sync the Stripe API return data to the database,
            # this way we don't need to wait for a webhook-triggered sync
            subscription = djstripe.models.Subscription.sync_from_stripe_data(
                stripe_subscription
            )

            intent = stripe_subscription
        elif "payment_intent_id" in data:
            intent = stripe.PaymentIntent.confirm(
                data["payment_intent_id"],
                api_key=djstripe.settings.STRIPE_SECRET_KEY,
            )
        else:
            session = stripe.checkout.Session.create(
                customer=customer.id,
                payment_method_types=['card'],
                # success_url='http://example.com/success',
                # cancel_url='http://example.com/cancelled',
                subscription_data={
                    'items': [{
                        'plan': request.data["plan"],
                    }],
                },
            )
            return JsonResponse({"session_id", session.id}, status=200)
    except stripe.error.CardError as e:
        # Display error on client
        return_data = json.dumps({"error": e.user_message}), 400
        return HttpResponse(
            return_data[0], content_type="application/json", status=return_data[1]
        )

    # For more: https://stripe.com/docs/payments/intents#intent-statuses
    if intent.status == "requires_action" and intent.next_action.type == "use_stripe_sdk":
        # Tell the client to handle the action
        return_data = (
            json.dumps(
                {
                    "requires_action": True,
                    "payment_intent_client_secret": intent.client_secret,
                }
            ),
            200,
        )
    elif intent.status == "succeeded" or intent.status == "active":
        # The payment did not need any additional actions and completed!
        # Handle post-payment fulfillment
        return_data = json.dumps({"success": True}), 200
    else:
        print(intent.status)
        # Invalid status
        return_data = json.dumps({"error": "Invalid PaymentIntent status"}), 500
    return HttpResponse(return_data[0], content_type="application/json", status=return_data[1])

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
