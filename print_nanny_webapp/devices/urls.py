from django.urls import path

from .views import (
    DeviceDeleteView,
    DeviceDetailView,
    DeviceVideoView,
    DeviceCreateView,
    ConfigDownloadView,
    DeviceSettingsView,
)

app_name = "devices"

urlpatterns = [
    path(
        "config/<slug:pk>/download",
        ConfigDownloadView.as_view(),
        name="config-download",
    ),
    path("<slug:pk>/settings", DeviceSettingsView.as_view(), name="settings"),
    path("<slug:pk>/", DeviceDetailView.as_view(), name="detail"),
    path("<slug:pk>/delete", DeviceDeleteView.as_view(), name="delete"),
    path("<slug:pk>/video", DeviceVideoView.as_view(), name="video"),
    path("connect", DeviceCreateView.as_view(), name="create"),
]
