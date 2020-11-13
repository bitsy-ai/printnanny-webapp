from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter
from django.conf.urls import url

from print_nanny_webapp.users.api.views import UserViewSet #, MeViewSet
from print_nanny_webapp.client_events.api.views import OctoPrintEventViewSet, PredictEventViewSet
if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register(f"events/predict", PredictEventViewSet)

#router.register("me", MeViewSet)


app_name = "api"
urlpatterns = router.urls
# urlpatterns = urlpatterns + [
#   	#url(r'^events/octoprint/$', OctoPrintEventViewSet.as_view({'post': 'post'}), name='octoprint-event'),
#   	url(r'^events/predict/$', PredictEventView.as_view({''}), name='predict-event'),
# ]