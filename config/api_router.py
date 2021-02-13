from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter
from django.urls import include, path, re_path

from print_nanny_webapp.ml_ops.api.views import ModelArtifactViewSet, ExperimentDeviceConfigViewSet, DeviceCalibrationViewSet
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
    RemoteControlSnapshotViewSet
)

from print_nanny_webapp.alerts.api.views import AlertViewSet, AlertSettingsViewSet

router = DefaultRouter()

router.register("alerts", AlertViewSet)
router.register("alert_settings", AlertSettingsViewSet)

router.register("users", UserViewSet)

router.register(f"device-calibrations", DeviceCalibrationViewSet, basename="device-calibrations")
router.register(f"snapshots", RemoteControlSnapshotViewSet, basename='snapshot')
router.register(f"octoprint-devices", OctoPrintDeviceViewSet, basename='octoprint-device')
router.register(f"octoprint-events", OctoPrintEventViewSet, basename='octoprint-event')

router.register(r"printer-profiles", PrinterProfileViewSet, basename='printer-profile')
router.register(r"print-jobs", PrintJobViewSet, basename='print-job')
router.register(r"gcode-files", GcodeFileViewSet, basename='gcode-file')
router.register(r"commands", CommandViewSet, basename='command')
router.register(r"model-artifacts", ModelArtifactViewSet, basename='model-artifact')
router.register(r"experiment-device-configs", ExperimentDeviceConfigViewSet, basename="experiment-device-config")

app_name = "api"
urlpatterns = router.urls
