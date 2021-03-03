from django.urls import include, path

from print_nanny_webapp.subscriptions.views import SubscriptionsListView

app_name = "subscriptions"

urlpatterns = [
    path(r"^stripe/", include("djstripe.urls", namespace="djstripe")),
    path("", SubscriptionsListView.as_view(), name="list"),
]
