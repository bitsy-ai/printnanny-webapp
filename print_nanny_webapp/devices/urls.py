from django.urls import path, include

from .views import DeviceListView, DeviceDetailView, DeviceCreateView

app_name = "devices"

urlpatterns = [
    path("register", DeviceCreateView.as_view(), name="create"),
    path("", DeviceListView.as_view(), name="list"),
    path("<slug:pk>", DeviceDetailView.as_view(), name="detail"),
]
