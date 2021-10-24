from django.urls import path, include

from .views import ApplianceListView

app_name = "devices"

appliance_urls = [
    path("/", ApplianceListView.as_view(), name="list"),
]

urlpatterns = [
    path("appliances", include((appliance_urls, app_name), namespace="appliances"))
]
