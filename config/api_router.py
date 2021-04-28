from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter
from django.urls import include, path, re_path
from print_nanny_webapp.ml_ops.api.views import (
    ModelArtifactViewSet, ExperimentDeviceConfigViewSet, DeviceCalibrationViewSet, ExperimentViewSet
)
from print_nanny_webapp.users.api.views import UserViewSet

from print_nanny_webapp.remote_control.api.views import (
    GcodeFileViewSet,
    PrinterProfileViewSet,
    PrintSessionViewSet,
    OctoPrintDeviceViewSet,
    CommandViewSet
)

# from print_nanny_webapp.alerts.api.views import (
#     AlertViewSet, PrintSessionAlertViewSet
# )

from print_nanny_webapp.partners.api.views import ( GeeksViewSet )

router = DefaultRouter()

# router.register("alerts", AlertViewSet)
# router.register("print-session-alerts", PrintSessionAlertViewSet, basename="print-session-alerts")

router.register("users", UserViewSet)

router.register(f"device-calibrations", DeviceCalibrationViewSet, basename="device-calibration")
router.register(f"octoprint-devices", OctoPrintDeviceViewSet, basename='octoprint-device')

router.register(r"printer-profiles", PrinterProfileViewSet, basename='printer-profile')
router.register(r"print-sessions", PrintSessionViewSet, basename='print-session')
router.register(r"gcode-files", GcodeFileViewSet, basename='gcode-file')
router.register(r"commands", CommandViewSet, basename='command')
router.register(r"model-artifacts", ModelArtifactViewSet, basename='model-artifact')
router.register(r"experiment-device-configs", ExperimentDeviceConfigViewSet, basename="experiment-device-config")
router.register(r"experiments", ExperimentViewSet, basename="experiment")
router.register(r"partners/3d-geeks", GeeksViewSet, basename='partner-3d-geeks')

app_name = "api"

urlpatterns = router.urls
