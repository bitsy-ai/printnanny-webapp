import logging
from rest_framework.mixins import (
    CreateModelMixin,
)
from rest_framework.viewsets import GenericViewSet
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from drf_spectacular.utils import extend_schema_view, extend_schema
from django_nats_nkeys.models import NatsOrganizationUser
from print_nanny_webapp.nkeys.services import get_or_create_nats_organization_user

from print_nanny_webapp.utils.permissions import IsObjectOwner

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
    permission_classes = (IsObjectOwner, IsAuthenticated)
    lookup_field = "id"
    queryset = NatsOrganizationUser.objects.all()
    serializer_class = NatsOrganizationUserSerializer

    def get(self, request):
        org_user = get_or_create_nats_organization_user(self.request.user)
        serializer = NatsOrganizationUserSerializer(instance=org_user)
        return Response(serializer.data, status.HTTP_200_OK)
