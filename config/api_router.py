from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedSimpleRouter
from print_nanny_webapp.devices.api.views import (
    CloudiotDeviceViewSet,
    DeviceHostnameViewSet,
    PublicKeyViewSet,
    SystemInfoViewSet,
    DeviceViewSet,
    JanusStreamViewSet,
    ConfigDownloadViewSet,
    DeviceSettingsViewSet,
)
from print_nanny_webapp.events.api.views import CommandViewSet, EventViewSet

from print_nanny_webapp.alerts.api.views import (
    AlertSettingsViewSet,
    AlertViewSet,  # , PrintSessionAlertViewSet
)

from print_nanny_webapp.partners.api.views import GeeksViewSet
from print_nanny_webapp.subscriptions.api.views import (
    BillingCancelView,
    BillingReactivateView,
    BillingSummaryView,
)
from print_nanny_webapp.utils.api.views import PrintNannyApiConfigViewset
from print_nanny_webapp.octoprint.api.views import (
    GcodeFileViewSet,
    OctoPrintBackupViewset,
    OctoPrintServerViewSet,
    OctoPrintSettingsViewSet,
    OctoPrinterProfileViewSet,
    OctoPrintServerByDeviceViewSet,
)


router = DefaultRouter()
router.register("alerts", AlertViewSet)
router.register("alert-settings", AlertSettingsViewSet)
router.register("devices", DeviceViewSet)

# octoprint endpoints (PrintNanny os data model)

# enables /api/devices/:hostname lookup (no nested routing)
other_urls = [
    path("devices/<slug:hostname>", DeviceHostnameViewSet.as_view({"get": "retrieve"})),
    path("client", PrintNannyApiConfigViewset.as_view(), name="client"),
    path("billing/summary", BillingSummaryView.as_view(), name="billing-summary"),
    path(
        "billing/<slug:subscription_id>/cancel/",
        BillingCancelView.as_view(),
        name="billing-cancel",
    ),
    path(
        "billing/<slug:subscription_id>/reactivate/",
        BillingReactivateView.as_view(),
        name="billing-reactivate",
    ),
]

devices_router = NestedSimpleRouter(router, r"devices", lookup="device")
devices_router.register("config", ConfigDownloadViewSet, basename="config")
devices_router.register("settings", DeviceSettingsViewSet, basename="settings")
devices_router.register(r"public-keys", PublicKeyViewSet, basename="public-keys")
devices_router.register(r"janus-streams", JanusStreamViewSet, basename="janus-streams")

devices_router.register(r"system-info", SystemInfoViewSet, basename="system-info")
devices_router.register(r"cloudiot", CloudiotDeviceViewSet, basename="cloudiot")
devices_router.register(
    r"octoprint-servers",
    OctoPrintServerByDeviceViewSet,
    basename="octoprint-servers",
)

router.register(
    r"octoprint-servers",
    OctoPrintServerViewSet,
    basename="octoprint-servers",
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
router.register(r"partners/3d-geeks", GeeksViewSet, basename="partner-3d-geeks")

app_name = "api"

urlpatterns = router.urls + devices_router.urls + other_urls
