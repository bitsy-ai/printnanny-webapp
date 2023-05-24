from django.db.models.query import QuerySet
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    CreateModelMixin,
)
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import GenericViewSet
from rest_framework import status, parsers

from drf_spectacular.utils import extend_schema_view, extend_schema

from print_nanny_webapp.workspaces.api.serializers import (
    WorkspaceSerializer,
    WorkspaceInviteSerializer,
    WorkspaceInviteCreateSerializer,
)
from print_nanny_webapp.workspaces.models import Workspace
from print_nanny_webapp.workspaces.services import get_workspaces_by_auth_user

from print_nanny_webapp.utils.api.views import (
    generic_create_errors,
    generic_list_errors,
    generic_get_errors,
    generic_update_errors,
)


@extend_schema_view(
    update=extend_schema(tags=["workspaces"]),
    create=extend_schema(
        tags=["workspaces"],
        responses={201: WorkspaceSerializer} | generic_create_errors,
    ),
    list=extend_schema(
        tags=["workspaces"],
        responses={200: WorkspaceSerializer(many=True)} | generic_list_errors,
    ),
    partial_update=extend_schema(
        tags=["workspaces"],
        responses={200: WorkspaceSerializer(many=True)} | generic_update_errors,
    ),
    retrieve=extend_schema(
        tags=["workspaces"],
        responses={200: WorkspaceSerializer} | generic_get_errors,
    ),
)
class WorkspaceViewSet(
    GenericViewSet,
    UpdateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    CreateModelMixin,
):
    serializer_class = WorkspaceSerializer
    lookup_field = "id"
    # omit OwnerOrUserFilterBackend, which is a DEFAULT_FILTER_BACKENDS
    filter_backends = [DjangoFilterBackend]

    def get_queryset(self) -> QuerySet:
        if self.request.user.is_authenticated:
            return get_workspaces_by_auth_user(self.request.user)
        return None

    @extend_schema(
        tags=["workspaces"],
        operation_id="workspaces_invite",
        request=WorkspaceInviteCreateSerializer,
        responses={201: WorkspaceInviteSerializer},
    )
    @action(methods=["post"], detail=False, url_path="invite")
    def invite(self, request):
        req_serializer = WorkspaceInviteCreateSerializer(data=request.data)
        if req_serializer.is_valid():
            invitation = req_serializer.create(
                req_serializer.validated_data, request.user
            )
            res_serializer = WorkspaceInviteSerializer(invitation)

            return Response(res_serializer.data, status=status.HTTP_201_CREATED)
        return Response(req_serializer.errors, status=status.HTTP_201_CREATED)
