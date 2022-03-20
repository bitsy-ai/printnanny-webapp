from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedSimpleRouter

from print_nanny_webapp.devices.api.views import (
    CloudiotDeviceViewSet,
    DeviceHostnameViewSet,
    JanusAuthViewSet,
    JanusStreamViewSet,
    PublicKeyViewSet,
    SystemInfoViewSet,
    DeviceViewSet,
)
from print_nanny_webapp.events.api.views import EventViewSet
from print_nanny_webapp.ml_ops.api.views import (
    ModelArtifactViewSet,
    ExperimentDeviceConfigViewSet,
    DeviceCalibrationViewSet,
    ExperimentViewSet,
)
from print_nanny_webapp.users.api.views import UserViewSet

from print_nanny_webapp.remote_control.api.views import (
    GcodeFileViewSet,
    PrinterProfileViewSet as AlphaPrinterProfileViewSet,
    PrintSessionViewSet,
    OctoPrintDeviceViewSet,
    CommandViewSet,
)

from print_nanny_webapp.telemetry.api.views import (
    OctoPrintEventViewSet,
    PrintNannyPluginEventViewSet,
    PrintJobEventViewSet,
    RemoteCommandEventViewSet,
    TelemetryEventViewSet,
)

from print_nanny_webapp.alerts.api.views import (
    AlertViewSet,  # , PrintSessionAlertViewSet
)

from print_nanny_webapp.partners.api.views import GeeksViewSet
from print_nanny_webapp.utils.api.views import PrintNannyApiConfigViewset
from print_nanny_webapp.octoprint.api.views import (
    OctoPrintBackupViewset,
    OctoPrintSettingsViewSet,
)

router = DefaultRouter()

router.register("client-config", PrintNannyApiConfigViewset, basename="client-config")

router.register("alerts", AlertViewSet)
router.register("devices", DeviceViewSet)

# octoprint endpoints (print nanny os data model)
router.register("octoprint-backups", OctoPrintBackupViewset)

# enables /api/devices/:hostname lookup (no nested routing)
devices_by_hostname = [
    path("devices/<slug:hostname>", DeviceHostnameViewSet.as_view({"get": "retrieve"})),
]

devices_router = NestedSimpleRouter(router, r"devices", lookup="device")
devices_router.register(r"public-keys", PublicKeyViewSet, basename="public-keys")
devices_router.register(r"janus-streams", JanusStreamViewSet, basename="janus-streams")

devices_router.register(r"system-info", SystemInfoViewSet, basename="system-info")
devices_router.register(r"cloudiot", CloudiotDeviceViewSet, basename="cloudiot")

router.register(
    r"octoprint/backups", OctoPrintBackupViewset, basename="octoprint-backups"
)
router.register(
    r"octoprint/settings",
    OctoPrintSettingsViewSet,
    basename="octoprint-settings",
)


router.register("events", EventViewSet, basename="events")


router.register("telemetry-events", TelemetryEventViewSet, basename="telemetry-events")
router.register(
    "remote-command-events", RemoteCommandEventViewSet, basename="remote-command-events"
)
router.register("octoprint-events", OctoPrintEventViewSet, basename="octoprint-events")
router.register(
    "print-nanny-plugin-events",
    PrintNannyPluginEventViewSet,
    basename="print-nanny-plugin-events",
)
router.register("print-job-events", PrintJobEventViewSet, basename="print-job-events")

router.register("users", UserViewSet)
user_router = NestedSimpleRouter(router, r"users", lookup="user")
user_router.register(r"janus-auth", JanusAuthViewSet, basename="janus-auth")


router.register(
    "device-calibrations", DeviceCalibrationViewSet, basename="device-calibration"
)
router.register(
    "octoprint-devices", OctoPrintDeviceViewSet, basename="octoprint-device"
)

router.register(
    r"printer-profiles", AlphaPrinterProfileViewSet, basename="printer-profile"
)
router.register(r"print-sessions", PrintSessionViewSet, basename="print-session")
router.register(r"gcode-files", GcodeFileViewSet, basename="gcode-file")
router.register(r"commands", CommandViewSet, basename="command")
router.register(r"model-artifacts", ModelArtifactViewSet, basename="model-artifact")
router.register(
    r"experiment-device-configs",
    ExperimentDeviceConfigViewSet,
    basename="experiment-device-config",
)
router.register(r"experiments", ExperimentViewSet, basename="experiment")
router.register(r"partners/3d-geeks", GeeksViewSet, basename="partner-3d-geeks")

app_name = "api"

urlpatterns = router.urls + devices_router.urls + user_router.urls + devices_by_hostname
