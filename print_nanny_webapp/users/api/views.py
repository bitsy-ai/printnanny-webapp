import logging
from django.db.models.query import QuerySet

from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    CreateModelMixin,
)

from drf_spectacular.utils import extend_schema_view, extend_schema
from django_nats_nkeys.models import NatsOrganizationUser, _default_name
from django_nats_nkeys.services import create_organization

from print_nanny_webapp.utils.views import AuthenticatedHttpRequest
from print_nanny_webapp.users.api.serializers import (
    EmailWaitlistSerializer,
    NatsOrganizationUserSerializer,
    WorkspaceSerializer,
)
from print_nanny_webapp.utils.api.views import (
    generic_create_errors,
    generic_list_errors,
    generic_get_errors,
    generic_update_errors,
)
from print_nanny_webapp.users.models import EmailWaitlist, Workspace, WorkspaceUser

logger = logging.getLogger(__name__)


@extend_schema_view(create=extend_schema(tags=["accounts"]))
class EmailWaitlistViewSet(GenericViewSet, CreateModelMixin):
    """
    A device (Raspberry Pi) running Print Nanny OS
    """

    serializer_class = EmailWaitlistSerializer
    queryset = EmailWaitlist.objects.all()
    lookup_field = "id"
    permission_classes = (AllowAny,)


class UserNkeyView(APIView):
    """
    Providers user nkey credentials
    """

    lookup_field = "id"
    queryset = NatsOrganizationUser.objects.all()
    serializer_class = NatsOrganizationUserSerializer

    def get(self, request: AuthenticatedHttpRequest):
        try:
            org_user = NatsOrganizationUser.objects.get(user=request.user)
        except NatsOrganizationUser.DoesNotExist:
            create_organization(
                request.user,
                _default_name(),
                org_user_defaults={"is_admin": True},
            )
            org_user = NatsOrganizationUser.objects.get(user=request.user)
        serializer = NatsOrganizationUserSerializer(instance=org_user)
        return Response(serializer.data, status.HTTP_200_OK)


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
class WorkspaceViewset(
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
