from django.urls import path, include


from .views import (
    AlertSettingsView,
    AlertListView
)

app_name = "alerts"

urlpatterns = [
    path("/alerts/settings", AlertSettingsView.as_view(), name="settings"),

    path("/alerts", AlertListView.as_view(), name="list")

]