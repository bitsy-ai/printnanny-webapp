from django.urls import path, include


from .views import (
    AlertSettingsView,
    AlertListView
)

app_name = "alerts"

urlpatterns = [
    path("/settings", AlertSettingsView.as_view(), name="settings"),
    path("", AlertListView.as_view(), name="list")

]