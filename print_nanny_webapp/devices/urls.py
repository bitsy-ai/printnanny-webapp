from django.urls import path, include

from .views import ApplianceListView, ApplianceDetailView

app_name = "devices"

appliance_urls = [
    path("/", ApplianceListView.as_view(), name="list"),
    path("/<slug:pk>", ApplianceDetailView.as_view(), name="detail"),
]

urlpatterns = [
    path("appliances", include((appliance_urls, app_name), namespace="appliances"))
]
