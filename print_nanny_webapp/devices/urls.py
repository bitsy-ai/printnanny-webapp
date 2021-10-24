from django.urls import path, include

from .views import DeviceListView, DeviceDetailView

app_name = "devices"

urlpatterns = [
    path("/", DeviceListView.as_view(), name="list"),
    path("/<slug:pk>", DeviceDetailView.as_view(), name="detail"),
]
