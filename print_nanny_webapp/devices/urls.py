from django.urls import path

from .views import (
    DeviceDeleteView,
    DeviceDetailView,
    DeviceVideoView,
    DeviceWelcomeDetailView,
    DeviceWelcomeView,
    ReleaseListView,
    LicenseDeleteView,
    LicenseDownloadView,
)

app_name = "devices"

urlpatterns = [
    path(
        "licenses/<slug:pk>/delete", LicenseDeleteView.as_view(), name="license-delete"
    ),
    path(
        "licenses/<slug:pk>/download",
        LicenseDownloadView.as_view(),
        name="license-download",
    ),
    path("releases/", ReleaseListView.as_view(), name="releases-list"),
    path("welcome/", DeviceWelcomeView.as_view(), name="welcome"),
    path(
        "welcome/<slug:pk>/", DeviceWelcomeDetailView.as_view(), name="welcome-detail"
    ),
    path("<slug:pk>/", DeviceDetailView.as_view(), name="detail"),
    path("<slug:pk>/delete", DeviceDeleteView.as_view(), name="delete"),
    path("<slug:pk>/video", DeviceVideoView.as_view(), name="video"),
]
