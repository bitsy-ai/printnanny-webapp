from django.urls import path

from views import ReleaseListView, ReleaseDetailView

app_name = "releases"

urlpatterns = [
    path("", ReleaseListView, name="list"),
    path("<slug:variant>/<slug:name>", ReleaseDetailView, name="detail"),
]
