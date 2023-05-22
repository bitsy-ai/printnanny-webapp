from django.db.models.query import QuerySet
from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    CreateModelMixin,
)
from rest_framework.viewsets import GenericViewSet
from drf_spectacular.utils import extend_schema_view, extend_schema

from print_nanny_webapp.workspaces.api.serializers import WorkspaceSerializer
from print_nanny_webapp.workspaces.models import Workspace

from print_nanny_webapp.utils.api.views import (
    generic_create_errors,
    generic_list_errors,
    generic_get_errors,
    generic_update_errors,
)


@extend_schema_view(
    create=extend_schema(
        tags=["workspaces"],
        responses={201: WorkspaceSerializer} | generic_create_errors,
    ),
    update=extend_schema(tags=["workspaces"]),
    list=extend_schema(
        tags=["workspaces"],
        responses={200: WorkspaceSerializer(many=True)} | generic_list_errors,
    ),
    partial_update=extend_schema(tags=["workspaces"]),
    retrieve=extend_schema(
        tags=["workspaces"],
        responses={200: WorkspaceSerializer} | generic_get_errors,
    ),
)
class WorkspaceViewSet(
    GenericViewSet,
    CreateModelMixin,
    UpdateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
):
    serializer_class = WorkspaceSerializer
    lookup_field = "id"

    def get_queryset(self) -> QuerySet:
        if self.request.user.is_authenticated:
            return Workspace.objects.filter(owner__email=self.request.user.email)
        return None
