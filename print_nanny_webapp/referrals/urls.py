from django.conf.urls import include
from django.urls import path
from .views import TrialView

app_name = "referrals"

urlpatterns = [path("trial", TrialView.as_view(), name="trial")]
