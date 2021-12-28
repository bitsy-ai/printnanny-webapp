from django.urls import path, include
from .views import RemoteAccessSurvey1Success, RemoteAccessSurvey1Create

app_name = "surveys"

urlpatterns = [
    path(
        "remote-access-1", RemoteAccessSurvey1Create.as_view(), name="remote-access-1"
    ),
    path(
        "remote-access-thanks",
        RemoteAccessSurvey1Success.as_view(),
        name="remote-access",
    ),
]
