from django.urls import path, include

from .views import (
    CameraCreateView,
    DeviceListView,
    DeviceDeleteView,
    DeviceDetailView,
    DeviceCreateView,
    DeviceLicenseDownload,
)

app_name = "devices"

urlpatterns = [
    path(
        "<slug:device_id>/add-camera", CameraCreateView.as_view(), name="create-camera"
    ),
    path("register", DeviceCreateView.as_view(), name="create"),
    path("", DeviceListView.as_view(), name="list"),
    path("<slug:pk>", DeviceDetailView.as_view(), name="detail"),
    path("<slug:pk>/delete", DeviceDeleteView.as_view(), name="delete"),
    path("<slug:pk>/license", DeviceLicenseDownload.as_view(), name="license"),
]
