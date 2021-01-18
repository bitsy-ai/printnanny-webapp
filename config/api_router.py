from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter
from django.urls import include, path, re_path

from print_nanny_webapp.users.api.views import UserViewSet #, MeViewSet
from print_nanny_webapp.client_events.api.views import (
    OctoPrintEventViewSet, 
)

from print_nanny_webapp.remote_control.api.views import (
    GcodeFileViewSet, 
    PrinterProfileViewSet, 
    PrintJobViewSet,
    OctoPrintDeviceViewSet,
    CommandViewSet,
)

from print_nanny_webapp.alerts.api.views import AlertViewSet, AlertSettingsViewSet

router = DefaultRouter()

router.register("alerts", AlertViewSet)
router.register("alert_settings", AlertSettingsViewSet)

router.register("users", UserViewSet)

router.register(f"octoprint-devices", OctoPrintDeviceViewSet, basename='octoprint-device')
router.register(f"octoprint-events", OctoPrintEventViewSet, basename='octoprint-event')

router.register(r"printer-profiles", PrinterProfileViewSet, basename='printer-profile')
router.register(r"print-jobs", PrintJobViewSet, basename='print-job')
router.register(r"gcode-files", GcodeFileViewSet, basename='gcode-file')
router.register(r"commands", CommandViewSet, basename='command')

app_name = "api"
urlpatterns = router.urls
