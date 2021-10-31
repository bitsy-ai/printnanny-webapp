from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.decorators import action
from print_nanny_webapp.utils.api.serializers import ErrorDetailSerializer
from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
)
from rest_framework.viewsets import GenericViewSet

from ..models import Release
from .serializers import ReleaseSerializer

##
# Device (by id)
##
list_releases_schema = extend_schema(
    responses={
        "default": ErrorDetailSerializer,
        200: ReleaseSerializer(many=True),
    },
)
retrieve_release_schema = extend_schema(
    responses={
        "default": ErrorDetailSerializer,
        201: ReleaseSerializer,
        202: ReleaseSerializer,
    },
)


@extend_schema_view(list=list_releases_schema, retreive=retrieve_release_schema)
class ReleaseViewSet(
    GenericViewSet,
    ListModelMixin,
    RetrieveModelMixin,
):
    """
    All-in-one Print Nanny installation
    via print-nanny-main-<platform>-<cpu>.img
    """

    serializer_class = ReleaseSerializer
    queryset = Release.objects.all()
    lookup_field = "id"

    # @action(detail=True, methods=["GET"])
    # def latest(self, request):

    #     release_channel = request.data
