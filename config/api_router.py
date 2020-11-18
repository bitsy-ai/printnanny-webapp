from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter
from django.conf.urls import url

from print_nanny_webapp.users.api.views import UserViewSet #, MeViewSet
from print_nanny_webapp.client_events.api.views import (OctoPrintEventViewSet, OctoPrintEventViewSet, 
    PredictEventFileViewSet,
    PredictEventViewSet, GcodeFileViewSet, PrinterProfileViewSet, PrintJobViewSet)


# if settings.DEBUG:
router = DefaultRouter()
# else:
#     router = SimpleRouter()

router.register("users", UserViewSet)
router.register(f"predict_events", PredictEventViewSet, basename='predict-event')
router.register(f"predict_event_files", PredictEventFileViewSet, basename='predict-event-file')

router.register(f"octoprint_events", OctoPrintEventViewSet, basename='octoprint-events')

router.register(f"printer_profiles", PrinterProfileViewSet, basename='printer-profile')
router.register(f"print_jobs", PrintJobViewSet, basename='print-job')
router.register(f"gcode_files", GcodeFileViewSet, basename='gcode-file')

#router.register("me", MeViewSet)


app_name = "api"
urlpatterns = router.urls
# urlpatterns = urlpatterns + [
#   	#url(r'^events/octoprint/$', OctoPrintEventViewSet.as_view({'post': 'post'}), name='octoprint-event'),
#   	url(r'^events/predict/$', PredictEventView.as_view({''}), name='predict-event'),
# ]