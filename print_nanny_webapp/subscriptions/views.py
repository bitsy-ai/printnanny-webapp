from print_nanny_webapp.subscriptions.forms import SubscriptionsPaymentForm
import stripe
import json, logging
from django.conf import settings
from django.http import HttpResponse, HttpRequest
from django.urls import reverse
from django.template.response import TemplateResponse

import djstripe.models
import djstripe.settings

from print_nanny_webapp.dashboard.views import DashboardView

logger = logging.getLogger(__name__)

class SubscriptionsListView(DashboardView):
    template_name = "subscriptions/list.html"
    form_classes = {
        "payment": SubscriptionsPaymentForm,
    }

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        ctx["STRIPE_PUBLIC_KEY"] = settings.STRIPE_PUBLIC_KEY
        return ctx

    def form_valid(self, form):
        print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
        stripe_source = form.cleaned_data["stripe_source"]
        plan = form.cleaned_data["plan"]

        # Create the stripe Customer, by default subscriber Model is User,
        # this can be overridden with settings.DJSTRIPE_SUBSCRIBER_MODEL
        customer, created = djstripe.models.Customer.get_or_create(subscriber=self.request.user)

        # Add the source as the customer's default card
        customer.add_card(stripe_source)

        # Using the Stripe API, create a subscription for this customer,
        # using the customer's default payment source
        stripe_subscription = stripe.Subscription.create(
            customer=customer.id,
            items=[{"plan": plan.id}],
            collection_method="charge_automatically",
            # tax_percent=15,
            api_key=djstripe.settings.STRIPE_SECRET_KEY,
        )

        # Sync the Stripe API return data to the database,
        # this way we don't need to wait for a webhook-triggered sync
        subscription = djstripe.models.Subscription.sync_from_stripe_data(
            stripe_subscription
        )

        self.request.subscription = subscription

        return super().form_valid(form)

    def get_success_url(self):
        return reverse(
            "subscriptions:success",
            kwargs={"id": self.request.subscription.id},
        )


class SubscriptionsSuccessView(DashboardView):
    template_name = "subscriptions/success.html"

    queryset = djstripe.models.Subscription.objects.all()
    slug_field = "id"
    slug_url_kwarg = "id"
    context_object_name = "subscription"


# TODO: Maybe this needs to be a normal class? Maybe throw it above?
# Might not be possible due to "requires_action" but could use REST API thing
# TODO: Use crispy form
def subscriptions_payment_intent_view_create(request: HttpRequest):
    if request.method != "POST":
        ctx = {"STRIPE_PUBLIC_KEY": djstripe.settings.STRIPE_PUBLIC_KEY}
        return TemplateResponse(request, SubscriptionsListView.template_name, ctx)

    intent = None
    data = json.loads(request.body)
    # TODO: Put this in the form
    data["plan"] = djstripe.models.Plan.objects.first().id
    try:
        # TODO: This is just ugly
        if "payment_method_id" in data:
            customer, created = djstripe.models.Customer.get_or_create(subscriber=request.user)
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
