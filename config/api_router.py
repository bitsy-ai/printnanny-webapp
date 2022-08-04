from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedSimpleRouter
from print_nanny_webapp.devices.api.views import (
    CloudiotDeviceViewSet,
    PublicKeyViewSet,
    SystemInfoViewSet,
    PiViewSet,
    WebrtcStreamViewSet,
    PiLicenseZipViewset,
    PiLicenseJsonViewSet,
    PiSettingsViewSet,
)
from print_nanny_webapp.events.api.views import (
    AllPiEventsViewSet,
    SinglePiEventsViewSet,
    EmailAlertSettingsViewSet,
)

# from print_nanny_webapp.alerts.api.views import (
#     AlertSettingsViewSet,
#     AlertViewSet,  # , PrintSessionAlertViewSet
# )

from print_nanny_webapp.subscriptions.api.views import (
    BillingSummaryView,
)
from print_nanny_webapp.octoprint.api.views import (
    GcodeFileViewSet,
    OctoPrintBackupViewset,
    OctoPrintServerViewSet,
    OctoPrintSettingsViewSet,
    OctoPrinterProfileViewSet,
    OctoPrintServerByDeviceViewSet,
)
from print_nanny_webapp.users.api.views import EmailWaitlistViewSet


router = DefaultRouter()

router.register("accounts/email-waitlist", EmailWaitlistViewSet, "email-waitlist")
# router.register("alerts", AlertViewSet, basename="alerts")
# router.register(r"alert-settings", AlertSettingsViewSet, basename="alert-settings")

router.register("pis", PiViewSet)

# octoprint endpoints (PrintNanny os data model)

# enables /api/devices/:hostname lookup (no nested routing)
other_urls = [
    path("billing/summary", BillingSummaryView.as_view(), name="billing-summary"),
]

router.register("pis/events", AllPiEventsViewSet, basename="all-pi-events")
pi_router = NestedSimpleRouter(router, r"pis", lookup="pi")

pi_router.register("events", SinglePiEventsViewSet, basename="events")
pi_router.register("license", PiLicenseZipViewset, basename="license-zip")
pi_router.register("license", PiLicenseJsonViewSet, basename="license-api-json")

pi_router.register("settings", PiSettingsViewSet, basename="settings")
pi_router.register(r"public-keys", PublicKeyViewSet, basename="public-keys")
pi_router.register(r"webrtc-streams", WebrtcStreamViewSet, basename="janus-streams")

pi_router.register(r"system-info", SystemInfoViewSet, basename="system-info")
pi_router.register(r"cloudiot", CloudiotDeviceViewSet, basename="cloudiot")
pi_router.register(
    r"octoprint",
    OctoPrintServerByDeviceViewSet,
    basename="octoprints",
)

router.register(
    r"octoprint",
    OctoPrintServerViewSet,
    basename="octoprint",
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

router.register(
    r"alert-settings/email",
    EmailAlertSettingsViewSet,
    basename="email-alert-settings",
)

# router.register("events", PiEventViewSet, basename="events")
# router.register("commands", CommandViewSet, basename="commands")
app_name = "api"

urlpatterns = router.urls + pi_router.urls + other_urls
