from django.urls import include, path

from print_nanny_webapp.subscriptions.views import (
    SubscriptionsListView,
    SubscriptionSoldoutView,
    SubscriptionFoundingMemberView,
    FoundingMemberSignupView,
    FoundingMemberCheckoutView,
    subscriptions_payment_intent_view_create,
)

app_name = "subscriptions"

urlpatterns = [
    path(
        "founding-member",
        SubscriptionFoundingMemberView.as_view(),
        name="founding_member_offer",
    ),
    path(
        "founding-member-signup",
        FoundingMemberSignupView.as_view(),
        name="signup",
    ),
    path(
        "founding-member-checkout",
        FoundingMemberCheckoutView.as_view(),
        name="checkout",
    ),
    path("sold-out", SubscriptionSoldoutView.as_view(), name="sold_out"),
    path("", SubscriptionsListView.as_view(), name="list"),
    path(
        "payment_intent",
        subscriptions_payment_intent_view_create,
        name="payment_intent",
    ),
]
