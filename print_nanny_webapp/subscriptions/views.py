import stripe
import json, logging
from django.conf import settings
from django.http import HttpResponse
from django.template.response import TemplateResponse

import djstripe.models
import djstripe.settings

from print_nanny_webapp.dashboard.views import DashboardView

logger = logging.getLogger(__name__)

class SubscriptionsListView(DashboardView):
    template_name = "subscriptions/list.html"

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        ctx["STRIPE_PUBLIC_KEY"] = settings.STRIPE_PUBLIC_KEY
        return ctx

def subscriptions_payment_view_create(request):
    if request.method == "POST":
        intent = None
        data = json.loads(request.body)
        try:
            if "payment_method_id" in data:
                # Create the PaymentIntent
                intent = stripe.PaymentIntent.create(
                    payment_method=data["payment_method_id"],
                    amount=500,
                    currency="usd",
                    confirmation_method="manual",
                    confirm=True,
                    api_key=djstripe.settings.STRIPE_SECRET_KEY,
                )
            elif "payment_intent_id" in data:
                intent = stripe.PaymentIntent.confirm(
                    data["payment_intent_id"],
                    api_key=djstripe.settings.STRIPE_SECRET_KEY,
                )
        except stripe.error.CardError as e:
            # Display error on client
            # TODO: Change response code?
            return_data = json.dumps({"error": e.user_message}), 200
            return HttpResponse(
                return_data[0], content_type="application/json", status=return_data[1]
            )

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
        elif intent.status == "succeeded":
            # The payment did not need any additional actions and completed!
            # Handle post-payment fulfillment
            return_data = json.dumps({"success": True}), 200
        else:
            # Invalid status
            return_data = json.dumps({"error": "Invalid PaymentIntent status"}), 500
        return HttpResponse(return_data[0], content_type="application/json", status=return_data[1])

    else:
        ctx = {"STRIPE_PUBLIC_KEY": djstripe.settings.STRIPE_PUBLIC_KEY}
        return TemplateResponse(request, "payment_intent.html", ctx)
