from django.urls import path

from .views import OctoPrintPluginView


app_name = "octoprint"

urlpatterns = [
    path("", OctoPrintPluginView.as_view(), name="dashboard"),
]
