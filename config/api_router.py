from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from print_nanny_webapp.users.api.views import UserViewSet #, MeViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
#router.register("me", MeViewSet)


app_name = "api"
urlpatterns = router.urls
