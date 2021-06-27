from django.http.response import JsonResponse
from typing import Any
from django.views.generic.base import RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin
import stripe
import json, logging
from django.urls import reverse
from django.http import HttpRequest, HttpResponse
from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from djstripe import webhooks
from django.views.generic import TemplateView
from django.conf import settings
from allauth.account.views import SignupView
import djstripe.models
import djstripe.enums
import djstripe.settings
from anymail.message import AnymailMessage
from django.template.loader import render_to_string

from print_nanny_webapp.utils.views import DashboardView
from print_nanny_webapp.remote_control.models import OctoPrintDevice

logger = logging.getLogger(__name__)
User = get_user_model()


class SubscriptionSoldoutView(TemplateView):
    template_name = "subscriptions/sold-out.html"


class FoundingMemberSignupView(SignupView):
    template_name = "subscriptions/founding-member-signup.html"
    success_url = "checkout"

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        sold_out = (
            djstripe.models.Subscription.objects.filter(
                status=djstripe.enums.SubscriptionStatus.active
            ).count()
            >= settings.PAID_BETA_SUBSCRIPTION_LIMIT
        )
        if sold_out:
            return redirect(reverse("subscriptions:sold_out"))
        return super().dispatch(request, *args, **kwargs)


class FoundingMemberCheckoutView(LoginRequiredMixin, TemplateView):
    login_url = "subscriptions:signup"
    template_name = "subscriptions/founding-member-checkout.html"

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        sold_out = (
            djstripe.models.Subscription.objects.filter(
                status=djstripe.enums.SubscriptionStatus.active
            ).count()
            >= settings.PAID_BETA_SUBSCRIPTION_LIMIT
        )
        if sold_out:
            return redirect(reverse("subscriptions:sold_out"))
        return super().dispatch(request, *args, **kwargs)


class SubscriptionsListView(DashboardView):
    template_name = "subscriptions/list.html"

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)

        try:
            customer = djstripe.models.Customer.objects.get(
                subscriber=self.request.user
            )
        except djstripe.models.Customer.DoesNotExist:
            # start_trial(self.request.user, instance=self.request.user, created=True)
            customer = djstripe.models.Customer.objects.get(
                subscriber=self.request.user
            )

        # Populate template with current subscriptions and stripe public key
        ctx["STRIPE_PUBLIC_KEY"] = djstripe.settings.STRIPE_PUBLIC_KEY
        ctx["SUBSCRIPTIONS"] = customer.subscriptions.all().order_by("-created")
        ctx["PRODUCTS"] = djstripe.models.Product.objects.filter(active=True)
        for p in ctx["PRODUCTS"]:
            p.prices_list = p.prices.filter(active=True)

        ctx["DEVICES"] = OctoPrintDevice.objects.filter(user=self.request.user)

        return ctx


def subscriptions_payment_intent_view_create(request: HttpRequest):
    if request.method != "POST":
        return redirect("subscriptions:list")

    data = json.loads(request.body)

    if "price_id" not in data.keys():
        return JsonResponse(
            {"err": "No plan selected. Please select a subscription plan"}, status=400
        )
    if "devices" not in data.keys() or not len(data["devices"]):
        return JsonResponse(
            {
                "err": "No device selected. Please select a device to apply the subscription to"
            },
            status=400,
        )

    devices = OctoPrintDevice.objects.filter(user=request.user, pk__in=data["devices"])
    if not len(devices) or len(devices) != len(data["devices"]):
        return JsonResponse(
            {
                "err": "The selected devices are not valid or do not exist. Please select at least one valid device - but we like your curiosity :)"
            },
            status=400,
        )

    customer = djstripe.models.Customer.objects.get(subscriber=request.user)
    session = stripe.checkout.Session.create(
        customer=customer.id,
        payment_method_types=["card"],
        mode="subscription",
        success_url=request.build_absolute_uri(reverse("subscriptions:list")),
        cancel_url=request.build_absolute_uri(reverse("subscriptions:list")),
        line_items=[
            {
                "price": data["price_id"],
                "quantity": len(devices),
                "description": "Print-Nanny Subscription",
            }
        ],
        api_key=djstripe.settings.STRIPE_SECRET_KEY,
        allow_promotion_codes=True,
        metadata={"devices": ",".join([str(x.id) for x in devices])},
    )
    return JsonResponse({"session_id": session.id}, status=200)


@webhooks.handler("customer.subscription.trial_will_end")
def subscriptions_trial_will_end(event):
    logger.info(
        f"Sending email to user {event.customer.email} that their trial is ending"
    )
    user = User.objects.get(email=event.customer.email)

    merge_data = {
        "FIRST_NAME": user.first_name or "Maker",
    }

    text_body = render_to_string(
        "email/subscriptions_trial_ending_body.txt", merge_data
    )
    # html_body = render_to_string("email/subscriptions_trial_ending_body.html", merge_data)
    subject = render_to_string(
        "email/subscriptions_trial_ending_subject.txt", merge_data
    )

    message = AnymailMessage(
        subject=subject,
        body=text_body,
        to=[event.customer.email],
    )
    # message.attach_alternative(html_body, "text/html")
    message.send()


@webhooks.handler("subscription_schedule.expiring")
def subscriptions_subscription_expiring(event):
    logger.info(
        f"User {event.customer.email} subscription <X> is expiring, sending email"
    )
    user = User.objects.get(email=event.customer.email)

    merge_data = {
        "FIRST_NAME": user.first_name or "Maker",
    }

    text_body = render_to_string(
        "email/subscriptions_subscription_expiring_body.txt", merge_data
    )
    # html_body = render_to_string("email/subscriptions_subscription_expiring_body.html", merge_data)
    subject = render_to_string(
        "email/subscriptions_subscription_expiring_subject.txt", merge_data
    )

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
    logger.info(
        f"User's {event.customer.email} subscription <X> payment <X> failed, sending email"
    )
    user = User.objects.get(email=event.customer.email)

    merge_data = {
        "FIRST_NAME": user.first_name or "Maker",
    }

    text_body = render_to_string(
        "email/subscriptions_payment_failed_body.txt", merge_data
    )
    # html_body = render_to_string("email/subscriptions_subscription_expiring_body.html", merge_data)
    subject = render_to_string(
        "email/subscriptions_payment_failed_subject.txt", merge_data
    )

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
    logger.info(
        f"User {event.customer.email} paid subscription <X> successfully, sending email"
    )
    user = User.objects.get(email=event.customer.email)

    merge_data = {
        "FIRST_NAME": user.first_name or "Maker",
    }

    text_body = render_to_string(
        "email/subscriptions_payment_succeeded_body.txt", merge_data
    )
    # html_body = render_to_string("email/subscriptions_subscription_expiring_body.html", merge_data)
    subject = render_to_string(
        "email/subscriptions_payment_succeeded_subject.txt", merge_data
    )

    message = AnymailMessage(
        subject=subject,
        body=text_body,
        to=[event.customer.email],
    )
    # message.attach_alternative(html_body, "text/html")
    message.send()
