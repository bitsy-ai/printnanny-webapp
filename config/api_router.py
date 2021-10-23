from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedSimpleRouter
from print_nanny_webapp.devices.api.serializers import PrinterControllerSerializer

from print_nanny_webapp.devices.api.views import (
    AnsibleFactsViewSet,
    ApplianceViewSet,
    ApplianceHostnameViewSet,
    AppliancePublicKeyViewSet,
    CameraViewSet,
    CloudIoTDeviceViewSet,
    PrinterControllerViewSet,
)
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

router = DefaultRouter()

router.register("alerts", AlertViewSet)
router.register("appliances", ApplianceViewSet)
# enables /api/appliances/:hostname lookup (no nested routing)
appliances_by_hostname = [
    path("appliances/<slug:hostname>", ApplianceHostnameViewSet.as_view({'get': 'retrieve'})),
]

appliances_router = NestedSimpleRouter(router, r'appliances', lookup='appliance')
appliances_router.register(r'ansible-facts', AnsibleFactsViewSet, basename='ansible-facts')
appliances_router.register(r'keypairs', AppliancePublicKeyViewSet, basename='keypairs')
appliances_router.register(r'cameras', CameraViewSet, basename='cameras')
appliances_router.register(r'cloud-iot-devices', CloudIoTDeviceViewSet, basename='cloud-iot-devices')
appliances_router.register(r'printer-controllers', PrinterControllerViewSet, basename='printer-controllers')

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

app_name = "api"

urlpatterns = router.urls + appliances_router.urls + appliances_by_hostname
