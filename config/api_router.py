from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedSimpleRouter
from print_nanny_webapp.devices.api.serializers import PrinterControllerSerializer

from print_nanny_webapp.devices.api.views import (
    CameraViewSet,
    CloudiotDeviceViewSet ,
    DeviceConfigViewSet,
    DeviceHostnameViewSet,
    DeviceInfoViewSet,
    DeviceViewSet,
    LicenseViewSet,
    PrinterControllerViewSet,
    SystemTaskViewSet,
)
from print_nanny_webapp.devices.models import DeviceInfo
from print_nanny_webapp.ml_ops.api.views import (
    ModelArtifactViewSet, ExperimentDeviceConfigViewSet, DeviceCalibrationViewSet, ExperimentViewSet
)
from print_nanny_webapp.users.api.views import UserViewSet

from print_nanny_webapp.remote_control.api.views import (
    GcodeFileViewSet,
    PrinterProfileViewSet as AlphaPrinterProfileViewSet,
    PrintSessionViewSet,
    OctoPrintDeviceViewSet,
    CommandViewSet
)

from print_nanny_webapp.telemetry.api.views import (
    OctoPrintEventViewSet,
    PrintNannyPluginEventViewSet,
    PrintJobEventViewSet,
    RemoteCommandEventViewSet,
    TelemetryEventViewSet
)

from print_nanny_webapp.alerts.api.views import (
    AlertViewSet #, PrintSessionAlertViewSet
)

from print_nanny_webapp.partners.api.views import ( GeeksViewSet )

from print_nanny_webapp.releases.api.views import ReleaseViewSet, LatestReleaseViewSet

router = DefaultRouter()

router.register("alerts", AlertViewSet)
router.register("devices", DeviceViewSet)
# enables /api/devices/:hostname lookup (no nested routing)
devices_by_hostname = [
    path("devices/<slug:hostname>", DeviceHostnameViewSet.as_view({'get': 'retrieve'})),
]

devices_router  = NestedSimpleRouter(router, r'devices', lookup='device')
devices_router.register("licenses", LicenseViewSet, basename='licenses')

devices_router.register(r'config', DeviceConfigViewSet, basename='config')
devices_router.register(r'system-tasks', SystemTaskViewSet, basename='system-tasks')
devices_router.register(r'info', DeviceInfoViewSet, basename='info')
devices_router.register(r'cameras', CameraViewSet, basename='cameras')
devices_router.register(r'cloud-iot-devices', CloudiotDeviceViewSet , basename='cloud-iot-devices')
devices_router.register(r'printer-controllers', PrinterControllerViewSet, basename='printer-controllers')

router.register("telemetry-events", TelemetryEventViewSet, basename="telemetry-events")
router.register("remote-command-events", RemoteCommandEventViewSet, basename="remote-command-events")
router.register("octoprint-events", OctoPrintEventViewSet, basename="octoprint-events")
router.register("print-nanny-plugin-events", PrintNannyPluginEventViewSet, basename="print-nanny-plugin-events")
router.register("print-job-events", PrintJobEventViewSet, basename="print-job-events")

router.register("users", UserViewSet)

router.register(f"device-calibrations", DeviceCalibrationViewSet, basename="device-calibration")
router.register(f"octoprint-devices", OctoPrintDeviceViewSet, basename='octoprint-device')

router.register(r"printer-profiles", AlphaPrinterProfileViewSet, basename='printer-profile')
router.register(r"print-sessions", PrintSessionViewSet, basename='print-session')
router.register(r"gcode-files", GcodeFileViewSet, basename='gcode-file')
router.register(r"commands", CommandViewSet, basename='command')
router.register(r"model-artifacts", ModelArtifactViewSet, basename='model-artifact')
router.register(r"experiment-device-configs", ExperimentDeviceConfigViewSet, basename="experiment-device-config")
router.register(r"experiments", ExperimentViewSet, basename="experiment")
router.register(r"partners/3d-geeks", GeeksViewSet, basename='partner-3d-geeks')
router.register(r"releases", ReleaseViewSet, basename='releases')

releases_by_channel = [
    path("releases/<slug:release_channel>/latest", LatestReleaseViewSet.as_view({'get': 'retrieve'})),
]


app_name = "api"

urlpatterns = router.urls + devices_router .urls + devices_by_hostname + releases_by_channel
