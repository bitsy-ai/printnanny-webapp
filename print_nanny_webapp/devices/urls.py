from django.urls import path

from .views import (
    DeviceDeleteView,
    DeviceDetailView,
    DeviceWelcomeView,
    DeviceWelcomeDetailView,
    ReleaseListView,
)

app_name = "devices"

urlpatterns = [
    path("releases/", ReleaseListView.as_view(), name="releases-list"),
    path("welcome/", DeviceWelcomeView.as_view(), name="welcome"),
    path(
        "welcome/<slug:pk>/", DeviceWelcomeDetailView.as_view(), name="welcome-detail"
    ),
    path("<slug:pk>/", DeviceDetailView.as_view(), name="detail"),
    path("<slug:pk>/delete", DeviceDeleteView.as_view(), name="delete"),
]
