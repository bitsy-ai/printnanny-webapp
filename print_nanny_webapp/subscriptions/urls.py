from django.urls import include, path

from print_nanny_webapp.subscriptions.views import (
    SubscriptionsListView,
    SubscriptionSoldoutView,
    FoundingMemberSignupView,
    FoundingMemberCheckoutView,
)

app_name = "subscriptions"

urlpatterns = [
    path(
        "signup",
        FoundingMemberSignupView.as_view(),
        name="signup",
    ),
    path(
        "checkout",
        FoundingMemberCheckoutView.as_view(),
        name="checkout",
    ),
    path("sold-out", SubscriptionSoldoutView.as_view(), name="sold_out"),
    path("", SubscriptionsListView.as_view(), name="list"),
]
