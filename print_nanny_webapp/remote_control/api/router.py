
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# router.register('alert-messages', AlertMessageViewSet, basename='alert-message', namespace='alerts')
# router.register('alert-events', AlertEventViewSet, basename='alert-event', namespace='alerts')

# router.register("users", UserViewSet)
# router.register(f"predict-events", PredictEventViewSet, basename='predict-event', namespace='events')
# router.register(f"predict-event-files", PredictEventFileViewSet, basename='predict-event-file', 'events')

# router.register(f"octoprint-events", OctoPrintEventViewSet, basename='octoprint-event', 'events')

router.register(f"printer-profiles", PrinterProfileViewSet, basename='printer-profile')
router.register(f"print-jobs", PrintJobViewSet, basename='print-job')
router.register(f"gcode-files", GcodeFileViewSet)



app_name = "remote-control"
urlpatterns = router.urls
