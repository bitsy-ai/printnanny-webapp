from django.urls import path

from .views import ReleaseListView, ReleaseDetailView

app_name = "releases"

urlpatterns = [
    path("", ReleaseListView.as_view(), name="list"),
    path("<slug:variant>/<slug:name>", ReleaseDetailView.as_view(), name="detail"),
]
