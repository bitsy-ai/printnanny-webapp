import logging

from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (
    CreateModelMixin,
)

from drf_spectacular.utils import extend_schema_view, extend_schema
from django_nats_nkeys.models import NatsOrganizationUser, _default_name
from django_nats_nkeys.services import create_organization

from print_nanny_webapp.utils.views import AuthenticatedHttpRequest
from print_nanny_webapp.users.api.serializers import (
    EmailWaitlistSerializer,
    NatsOrganizationUserSerializer,
)

from print_nanny_webapp.users.models import EmailWaitlist

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
