from typing import Any, Dict, TYPE_CHECKING
import json
import logging
import stripe
from allauth.account.views import SignupView
from django.http.response import JsonResponse
from django.apps import apps
from django.views.generic.base import RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.http import HttpRequest, HttpResponse
from django.contrib.auth import get_user_model
from django.views.generic import TemplateView
from django.conf import settings
from django.db.models import Q
import djstripe.models
import djstripe.enums
import djstripe.settings
from djstripe.settings import djstripe_settings

from print_nanny_webapp.utils.views import DashboardView

logger = logging.getLogger(__name__)

# https://github.com/typeddjango/django-stubs/issues/599
if TYPE_CHECKING:
    from print_nanny_webapp.users.models import User as UserType
User = get_user_model()

# set stripe api_key for all api calls
# djstripe_settings automatically selects between test/live key based on STRIPE_LIVE_MODE setting
stripe.api_key = djstripe_settings.STRIPE_SECRET_KEY


class FoundingMemberSignupView(SignupView):
    template_name = "subscriptions/founding-member-signup.html"
    success_url = "/subscriptions/checkout"

    def get_initial(self) -> Dict[str, Any]:

        email = self.request.GET.get("email")
        referral_code = self.request.GET.get("code")
        if not email and not referral_code:
            return super().get_initial()
        initial: Dict[str, str] = dict()
        if email:
            initial.update(email=self.request.GET["email"])
        if referral_code:
            initial.update(referral_code=referral_code)
        logger.info("Form initialized with data %s", initial)
        return initial


class CheckoutSuccessView(RedirectView):

    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        session_id = kwargs.get("session_id")
        if not session_id:
            return reverse("subscriptions:checkout")

        MemberBadge = apps.get_model("subscriptions", "MemberBadge")

        session = stripe.checkout.Session.retrieve(session_id)
        logger.info("Checkout session succeeded %s", session)
        customer = stripe.Customer.retrieve(session.customer)
        user = User.objects.get(email=customer.email)  # type: ignore
        logger.info("Customer info stripee customer=%s user=%s", customer, user)

        badge, created = MemberBadge.objects.get_or_create(
            type=MemberBadge.MemberBadgeType.PAID_BETA, user_id=user.id
        )
        logger.info("Created MemberBadge=%s", badge)

        return reverse("dashboard:home")


class FoundingMemberCheckoutView(LoginRequiredMixin, TemplateView):
    login_url = "subscriptions:signup"
    template_name = "subscriptions/founding-member-signup.html"

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        ctx["PRODUCTS"] = djstripe.models.Product.objects.filter(active=True)
        for p in ctx["PRODUCTS"]:
            p.prices_list = p.prices.filter(active=True)
        return ctx

    def post(self, request: HttpRequest, *args: Any, **kwargs: Dict) -> HttpResponse:
        data = json.loads(request.body)

        if "price_id" not in data.keys():
            return JsonResponse(
                {"err": "No plan selected. Please select a subscription plan"},
                status=400,
            )

        success_url_base = request.build_absolute_uri(
            reverse("subscriptions:checkout_success")
        )
        success_url_query = "/{CHECKOUT_SESSION_ID}"
        success_url = success_url_base + success_url_query

        session = stripe.checkout.Session.create(
            customer_email=request.user.email,  # type: ignore
            payment_method_types=["card"],
            mode="subscription",
            success_url=success_url,
            cancel_url=request.build_absolute_uri(reverse("subscriptions:checkout")),
            line_items=[
                {
                    "price": data["price_id"],
                    "description": "Print Nanny Founding Membership",
                    "quantity": 1,
                }
            ],
            api_key=djstripe_settings.STRIPE_SECRET_KEY,
            metadata=dict(user=request.user),
            subscription_data=dict(trial_period_days=settings.TRIAL_PERIOD_DAYS),
            client_reference_id=request.user.id,
            billing_address_collection="required",
            allow_promotion_codes=True,
        )

        return JsonResponse({"session_id": session.id}, status=200)


def link_customer_by_email(user) -> djstripe.models.Customer:
    customer = djstripe.models.Customer.objects.get(email=user.email)
    if customer.subscriber is None:
        customer.subscriber = user
        customer.save()
    elif customer.subscriber_id != user.id:
        logger.warning(
            "Tried to associate djstripe.models.Customer with email=%s with user=%s, but customer already linked to user=%s",
            customer.email,
            user,
            customer.subscriber,
        )
    return customer


class SubscriptionsListView(DashboardView):
    template_name = "subscriptions/list.html"

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        user = self.request.user
        try:
            query = Q(subscriber=self.request.user) | Q(email=user.email)  # type: ignore
            customer = djstripe.models.Customer.objects.get(query)
            if not customer.subscriber:
                link_customer_by_email(user)
            # attempt to link customer by email
        except djstripe.models.Customer.DoesNotExist:
            logger.warning("No stripe customer associated with user=%s", user)
            customer = None
        if customer:
            ctx["SUBSCRIPTIONS"] = customer.subscriptions.all().order_by("-created")
        else:
            ctx["SUBSCRIPTIONS"] = None

        ctx["PRODUCTS"] = djstripe.models.Product.objects.filter(active=True)
        for p in ctx["PRODUCTS"]:
            p.prices_list = p.prices.filter(active=True)

        return ctx


# @webhooks.handler("subscription_schedule.expiring")
# def subscriptions_subscription_expiring(event):
#     logger.info(
#         f"User {event.customer.email} subscription <X> is expiring, sending email"
#     )
#     user = User.objects.get(email=event.customer.email)

#     merge_data = {
#         "FIRST_NAME": user.first_name or "Maker",
#     }

#     text_body = render_to_string(
#         "email/subscriptions_subscription_expiring_body.txt", merge_data
#     )
#     # html_body = render_to_string("email/subscriptions_subscription_expiring_body.html", merge_data)
#     subject = render_to_string(
#         "email/subscriptions_subscription_expiring_subject.txt", merge_data
#     )

#     message = AnymailMessage(
#         subject=subject,
#         body=text_body,
#         to=[event.customer.email],
#     )
#     # message.attach_alternative(html_body, "text/html")
#     message.send()


# # @webhooks.handler("charge.failed")
# @webhooks.handler("invoice.payment_failed")
# def subscriptions_payment_failed(event):
#     logger.info(
#         f"User's {event.customer.email} subscription <X> payment <X> failed, sending email"
#     )
#     user = User.objects.get(email=event.customer.email)

#     merge_data = {
#         "FIRST_NAME": user.first_name or "Maker",
#     }

#     text_body = render_to_string(
#         "email/subscriptions_payment_failed_body.txt", merge_data
#     )
#     # html_body = render_to_string("email/subscriptions_subscription_expiring_body.html", merge_data)
#     subject = render_to_string(
#         "email/subscriptions_payment_failed_subject.txt", merge_data
#     )

#     message = AnymailMessage(
#         subject=subject,
#         body=text_body,
#         to=[event.customer.email],
#     )
#     # message.attach_alternative(html_body, "text/html")
#     message.send()


# # Payment action required is handled during the payment step inside the view
# # There are both invoice.paid and invoice.payment_succeeded but docs lean on the first
# # https://stripe.com/docs/billing/subscriptions/webhooks#tracking
# # @webhooks.handler("charge.succeeded")
# @webhooks.handler("invoice.paid")
# def subscriptions_invoice_paid(event):
#     # TODO: When a trial was paid, do nothing
#     logger.info(
#         f"User {event.customer.email} paid subscription <X> successfully, sending email"
#     )
#     user = User.objects.get(email=event.customer.email)

#     merge_data = {
#         "FIRST_NAME": user.first_name or "Maker",
#     }

#     text_body = render_to_string(
#         "email/subscriptions_payment_succeeded_body.txt", merge_data
#     )
#     # html_body = render_to_string("email/subscriptions_subscription_expiring_body.html", merge_data)
#     subject = render_to_string(
#         "email/subscriptions_payment_succeeded_subject.txt", merge_data
#     )

#     message = AnymailMessage(
#         subject=subject,
#         body=text_body,
#         to=[event.customer.email],
#     )
#     # message.attach_alternative(html_body, "text/html")
#     message.send()
