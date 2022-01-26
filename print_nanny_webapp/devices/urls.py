from django.urls import path

from .views import (
    CameraCreateView,
    DeviceListView,
    DeviceDeleteView,
    DeviceDetailView,
    DeviceCreateView,
    DeviceWelcomeView,
    DeviceWelcomeDetailView,
    ReleaseListView,
)

app_name = "devices"

urlpatterns = [
    path(
        "<slug:device_id>/add-camera", CameraCreateView.as_view(), name="create-camera"
    ),
    path("register", DeviceCreateView.as_view(), name="create"),
    path("", DeviceListView.as_view(), name="list"),
    path("releases/", ReleaseListView.as_view(), name="releases-list"),
    path("welcome/", DeviceWelcomeView.as_view(), name="welcome"),
    path(
        "welcome/<slug:pk>/", DeviceWelcomeDetailView.as_view(), name="welcome-detail"
    ),
    path("<slug:pk>/", DeviceDetailView.as_view(), name="detail"),
    path("<slug:pk>/delete", DeviceDeleteView.as_view(), name="delete"),
]
