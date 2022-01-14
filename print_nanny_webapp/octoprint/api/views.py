import logging
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
    CreateModelMixin,
)

from print_nanny_webapp.octoprint.api.serializers import OctoPrintBackupSerializer
from print_nanny_webapp.octoprint.models import OctoPrintBackup
from print_nanny_webapp.utils.api.views import (
    generic_create_errors,
    generic_list_errors,
    generic_get_errors,
)

logger = logging.getLogger(__name__)


@extend_schema_view(
    list=extend_schema(
        responses={200: OctoPrintBackupSerializer(many=True)} | generic_list_errors
    ),
    create=extend_schema(
        request=OctoPrintBackupSerializer,
        responses={201: OctoPrintBackupSerializer} | generic_create_errors,
    ),
    retreive=extend_schema(
        request=OctoPrintBackupSerializer,
        responses={200: OctoPrintBackupSerializer} | generic_get_errors,
    ),
    tags=["octoprint"],
)
class OctoPrintBackupViewset(
    GenericViewSet,
    ListModelMixin,
    RetrieveModelMixin,
    CreateModelMixin,
):
    serializer_class = OctoPrintBackupSerializer
    queryset = OctoPrintBackup.objects.all()
    lookup_field = "id"
