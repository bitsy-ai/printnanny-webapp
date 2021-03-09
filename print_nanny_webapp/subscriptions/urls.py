from django.urls import include, path

from print_nanny_webapp.subscriptions.views import SubscriptionsSuccessView, SubscriptionsListView, subscriptions_payment_intent_view_create

app_name = "subscriptions"

urlpatterns = [
    path(r"^stripe/", include("djstripe.urls", namespace="djstripe")),
    path("", SubscriptionsListView.as_view(), name="list"),
    path("success/<id>", SubscriptionsSuccessView.as_view(), name="success"),
    path("payment_intent", subscriptions_payment_intent_view_create, name="payment_intent"),
]
