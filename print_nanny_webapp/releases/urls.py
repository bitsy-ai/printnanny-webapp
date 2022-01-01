from django.urls import path

from .views import ReleaseListView

app_name = "releases"

urlpatterns = [
    path("", ReleaseListView.as_view(), name="list"),
]
