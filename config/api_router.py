from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedSimpleRouter


from print_nanny_webapp.achievements.api.views import AchievementViewSet
from print_nanny_webapp.crash_reports.api.views import CrashReportViewSet
from print_nanny_webapp.devices.api.views import (
    SystemInfoViewSet,
    PiViewSet,
    WebrtcStreamViewSet,
    PiLicenseZipViewset,
    NetworkSettingsViewSet,
)
from print_nanny_webapp.events.api.views import (
    EmailAlertSettingsViewSet,
    PrintJobAlertViewSet,
)
from print_nanny_webapp.shop.api.views import (
    ProductsViewSet,
    OrderCheckoutView,
    OrderByStripeCheckoutSessionIdView,
    ProductsSkuView,
)

from print_nanny_webapp.octoprint.api.views import (
    GcodeFileViewSet,
    OctoPrintBackupViewset,
    OctoPrintServerViewSet,
    OctoPrintSettingsViewSet,
    OctoPrinterProfileViewSet,
    OctoPrintServerByDeviceViewSet,
)
from print_nanny_webapp.users.api.views import (
    EmailWaitlistViewSet,
    UserNkeyView,
)
from print_nanny_webapp.videos.api.views import (
    CameraSnapshotViewSet,
    VideoRecordingViewSet,
    VideoRecordingPartViewSet,
    DemoSubmissionViewSet,
    DemoSubmissionFeedbackViewSet,
)
from print_nanny_webapp.moonraker.api.views import (
    MoonrakerServerViewSet,
    MoonrakerServerByDeviceViewSet,
)
from print_nanny_webapp.workspaces.api.views import (
    WorkspaceViewSet,
    workspace_invite_verify_view,
)

router = DefaultRouter()

router.register("accounts/email-waitlist", EmailWaitlistViewSet, "email-waitlist")
router.register("pis", PiViewSet)

router.register("crash-reports", CrashReportViewSet, "crash-reports")
router.register("demos", DemoSubmissionViewSet, "demos-submission")
router.register("demos/feedback", DemoSubmissionFeedbackViewSet, "demos-feedback")

router.register("videos", VideoRecordingViewSet, "videos")
router.register("video-parts", VideoRecordingPartViewSet, "video-parts")

router.register("moonraker", MoonrakerServerViewSet, "moonraker")


# octoprint endpoints (PrintNanny os data model)
other_urls = [
    path("shop/orders", OrderCheckoutView.as_view()),
    path(
        "shop/products/<str:sku>", ProductsSkuView.as_view(), name="shop-product-by-sku"
    ),
    path(
        "shop/checkout/success/<str:stripe_checkout_session_id>",
        OrderByStripeCheckoutSessionIdView.as_view(),
        name="shop-checkout-success",
    ),
    path("accounts/user/nkey", UserNkeyView.as_view()),
    # network settings is a singualar GET, so manually provide viewsets
    path(
        "network-settings/",
        NetworkSettingsViewSet.as_view(
            {
                "get": "retrieve",
                "post": "create",
            }
        ),
    ),
    path(
        "network-settings/<int:id>",
        NetworkSettingsViewSet.as_view(
            {
                "put": "update",
                "patch": "partial_update",
            }
        ),
    ),
    # email alert settings is a singular GET, so manually provide viewsets here
    path(
        "email-alert-settings/",
        EmailAlertSettingsViewSet.as_view(
            {
                "get": "retrieve",
                "post": "create",
            }
        ),
    ),
    path(
        "email-alert-settings/<int:id>",
        EmailAlertSettingsViewSet.as_view(
            {
                "put": "update",
                "patch": "partial_update",
            }
        ),
    ),
    path("workspace-invites/verify/", workspace_invite_verify_view),
]

pi_router = NestedSimpleRouter(router, r"pis", lookup="pi")

pi_router.register(
    "camera-snapshots", CameraSnapshotViewSet, basename="camera-snapshots"
)


pi_router.register("license", PiLicenseZipViewset, basename="license-zip")
pi_router.register(r"webrtc-streams", WebrtcStreamViewSet, basename="janus-streams")

pi_router.register(r"system-info", SystemInfoViewSet, basename="system-info")
pi_router.register(
    r"octoprint-server",
    OctoPrintServerByDeviceViewSet,
    basename="pi-octoprint-server",
)
pi_router.register(
    r"moonraker-server",
    MoonrakerServerByDeviceViewSet,
    basename="pi-moonraer-server",
)


router.register("achievements", AchievementViewSet)

router.register(
    r"shop/products",
    ProductsViewSet,
    basename="products",
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
    r"alerts/print-job",
    PrintJobAlertViewSet,
    basename="print-job-alerts",
)

router.register("workspaces", WorkspaceViewSet, basename="workspaces")

app_name = "api"

urlpatterns = router.urls + pi_router.urls + other_urls
