from django.urls import include, path

from print_nanny_webapp.subscriptions.views import (
    SubscriptionsListView,
    SubscriptionSoldoutView,
    subscriptions_payment_intent_view_create,
)

app_name = "subscriptions"

urlpatterns = [
    path("sold-out", SubscriptionSoldoutView.as_view(), name="sold-out"),
    path("", SubscriptionsListView.as_view(), name="list"),
    path(
        "payment_intent",
        subscriptions_payment_intent_view_create,
        name="payment_intent",
    ),
]
