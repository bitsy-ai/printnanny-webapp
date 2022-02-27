from django.urls import include, path, re_path

from print_nanny_webapp.subscriptions.views import (
    SubscriptionsListView,
    SubscriptionSoldoutView,
    FoundingMemberSignupView,
    FoundingMemberCheckoutView,
    CheckoutSuccessView,
)

app_name = "subscriptions"

urlpatterns = [
    path(
        "signup",
        FoundingMemberSignupView.as_view(),
        name="signup",
    ),
    path(
        "trial",
        FoundingMemberCheckoutView.as_view(),
        name="trial",
    ),
    path(
        "checkout",
        FoundingMemberCheckoutView.as_view(),
        name="checkout",
    ),
    path(
        "checkout-success",
        CheckoutSuccessView.as_view(),
        name="checkout_success",
    ),
    path(
        "checkout-success/<slug:session_id>",
        CheckoutSuccessView.as_view(),
    ),
    path("sold-out", SubscriptionSoldoutView.as_view(), name="sold_out"),
    path("", SubscriptionsListView.as_view(), name="list"),
]
