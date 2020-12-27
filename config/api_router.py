from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter
from django.urls import include, path, re_path

from print_nanny_webapp.users.api.views import UserViewSet #, MeViewSet
from print_nanny_webapp.client_events.api.views import (
    OctoPrintEventViewSet, 
    # ObjectDetectEventFileViewSet,
    # ObjectDetectEventViewSet, 
)

from print_nanny_webapp.remote_control.api.views import (
    GcodeFileViewSet, 
    PrinterProfileViewSet, 
    PrintJobViewSet,
)

# from print_nanny_webapp.alerts.api.views import (
#     AlertVideoMessageViewSet,
#     AlertEventViewSet
# )


router = DefaultRouter()
# router.register('alert-messages', AlertVideoMessageViewSet, basename='alert-message', namespace='alerts')
# router.register('alert-events', AlertEventViewSet, basename='alert-event', namespace='alerts')

router.register("users", UserViewSet)

# router.register(f"predict-events", ObjectDetectEventViewSet, basename='predict-event')
# router.register(f"predict-event-files", ObjectDetectEventFileViewSet, basename='predict-event-file')
router.register(f"octoprint-events", OctoPrintEventViewSet, basename='octoprint-event')

router.register(r"printer-profiles", PrinterProfileViewSet, basename='printer-profile')
router.register(r"print-jobs", PrintJobViewSet, basename='print-job')
router.register(r"gcode-files", GcodeFileViewSet, basename='gcode-file')

app_name = "api"
urlpatterns = router.urls
