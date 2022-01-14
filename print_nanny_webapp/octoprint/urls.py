from django.urls import path

from .views import OctoPrintBackupsList

app_name = "octoprint"

urlpatterns = [path("backups", OctoPrintBackupsList.as_view(), name="backups-list")]
