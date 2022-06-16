from email.mime import base
from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedSimpleRouter

from print_nanny_webapp.devices.api.views import (
    CloudiotDeviceViewSet,
    DeviceHostnameViewSet,
    JanusAuthViewSet,
    JanusCloudStreamViewSet,
    JanusEdgeStreamViewSet,
    LicenseViewSet,
    PublicKeyViewSet,
    SystemInfoViewSet,
    DeviceViewSet,
    JanusStreamViewSet,
)
from print_nanny_webapp.events.api.views import CommandViewSet, EventViewSet
from print_nanny_webapp.users.api.views import UserViewSet

from print_nanny_webapp.alerts.api.views import (
    AlertViewSet,  # , PrintSessionAlertViewSet
)

from print_nanny_webapp.partners.api.views import GeeksViewSet
from print_nanny_webapp.utils.api.views import PrintNannyApiConfigViewset
from print_nanny_webapp.octoprint.api.views import (
    GcodeFileViewSet,
    OctoPrintBackupViewset,
    OctoPrintInstallViewSet,
    OctoPrintSettingsViewSet,
    OctoPrinterProfileViewSet,
    OctoPrintInstallByDeviceViewSet,
)

router = DefaultRouter()
router.register("alerts", AlertViewSet)
router.register("devices", DeviceViewSet)

# octoprint endpoints (PrintNanny os data model)

# enables /api/devices/:hostname lookup (no nested routing)
other_urls = [
    path("devices/<slug:hostname>", DeviceHostnameViewSet.as_view({"get": "retrieve"})),
    path("client", PrintNannyApiConfigViewset.as_view(), name="client"),
    path("licenses", LicenseViewSet, name="licenses"),
]

devices_router = NestedSimpleRouter(router, r"devices", lookup="device")
devices_router.register(r"public-keys", PublicKeyViewSet, basename="public-keys")
devices_router.register(
    r"janus-cloud-streams", JanusCloudStreamViewSet, basename="janus-cloud-streams"
)
devices_router.register(
    r"janus-edge-streams", JanusEdgeStreamViewSet, basename="janus-edge-streams"
)
devices_router.register(r"janus-streams", JanusStreamViewSet, basename="janus-streams")

devices_router.register(r"system-info", SystemInfoViewSet, basename="system-info")
devices_router.register(r"cloudiot", CloudiotDeviceViewSet, basename="cloudiot")
devices_router.register(
    r"octoprint-installs",
    OctoPrintInstallByDeviceViewSet,
    basename="octoprint-installs",
)

router.register(
    r"octoprint/installs",
    OctoPrintInstallViewSet,
    basename="octoprint-installs",
)
router.register(
    r"octoprint/backups", OctoPrintBackupViewset, basename="octoprint-backups"
)
router.register(
    r"octoprint/gcode-files",
    GcodeFileViewSet,
    basename="gcode-files",
)
router.register(
    r"octoprint/printer-profiles",
    OctoPrinterProfileViewSet,
    basename="octoprint-printer-profiles",
)
router.register(
    r"octoprint/settings",
    OctoPrintSettingsViewSet,
    basename="octoprint-settings",
)


router.register("events", EventViewSet, basename="events")
router.register("commands", CommandViewSet, basename="commands")
router.register("users", UserViewSet)
user_router = NestedSimpleRouter(router, r"users", lookup="user")
user_router.register(r"janus-auth", JanusAuthViewSet, basename="janus-auth")
router.register(r"partners/3d-geeks", GeeksViewSet, basename="partner-3d-geeks")

app_name = "api"

urlpatterns = router.urls + devices_router.urls + user_router.urls + other_urls
