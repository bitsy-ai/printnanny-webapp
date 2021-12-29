from drf_spectacular.utils import extend_schema, extend_schema_view
from print_nanny_webapp.utils.api.serializers import ErrorDetailSerializer
from rest_framework.mixins import (
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
)
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet

from ..models import Release
from .serializers import ReleaseSerializer

##
# Releases (by id)
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
        200: ReleaseSerializer,
    },
)
create_release_schema = extend_schema(
    responses={
        "default": ErrorDetailSerializer,
        201: ReleaseSerializer,
    },
)


@extend_schema_view(
    list=list_releases_schema,
    retreive=retrieve_release_schema,
    create=create_release_schema,
)
class ReleaseViewSet(
    GenericViewSet, ListModelMixin, RetrieveModelMixin, CreateModelMixin
):
    """
    All-in-one Print Nanny installation
    via print-nanny-main-<platform>-<cpu>.img
    """

    permission_classes = [AllowAny]
    serializer_class = ReleaseSerializer
    queryset = Release.objects.all()
