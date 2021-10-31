from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.decorators import action
from print_nanny_webapp.utils.api.serializers import ErrorDetailSerializer
from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
)
from rest_framework.permissions import AllowAny
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

    permission_classes = [AllowAny]
    serializer_class = ReleaseSerializer
    queryset = Release.objects.all()


@extend_schema_view(retreive=retrieve_release_schema)
class LatestReleaseViewSet(GenericViewSet, RetrieveModelMixin):
    """
    All-in-one Print Nanny installation
    via print-nanny-main-<platform>-<cpu>.img
    """

    permission_classes = [AllowAny]
    serializer_class = ReleaseSerializer
    queryset = Release.objects.all()
    lookup_field = "release_channel"

    @extend_schema(
        tags=["releases"],
        operation_id="releases_latest_retreive",
        responses={
            "default": ErrorDetailSerializer,
            201: ReleaseSerializer,
        },
    )
    @action(detail=True, methods=["GET"])
    def retreive(self):
        release_channel = self.kwargs["release_channel"]
        return Release.objects.all(release_channel=release_channel).first()
