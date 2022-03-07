import logging
from drf_spectacular.utils import (
    extend_schema,
    extend_schema_view,
)
from django.apps import apps

from rest_framework.exceptions import PermissionDenied
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
    CreateModelMixin,
)
from rest_framework.permissions import IsAuthenticated
from print_nanny_webapp.utils.api.views import (
    generic_create_errors,
    generic_list_errors,
    generic_get_errors,
)
from print_nanny_webapp.utils.permissions import IsObjectOwner
from print_nanny_webapp.events.models import Event
from print_nanny_webapp.devices.services import janus_cloud_setup
from .serializers import PolymorphicEventSerializer

Device = apps.get_model("devices", "Device")

logger = logging.getLogger(__name__)


@extend_schema_view(
    list=extend_schema(
        tags=["events"],
        responses={
            200: PolymorphicEventSerializer(many=True),
        }
        | generic_list_errors,
    ),
    create=extend_schema(
        tags=["events"],
        request=PolymorphicEventSerializer,
        responses={
            201: PolymorphicEventSerializer,
        }
        | generic_create_errors,
    ),
    retrieve=extend_schema(
        tags=["events"],
        request=PolymorphicEventSerializer,
        responses={
            200: PolymorphicEventSerializer,
        }
        | generic_get_errors,
    ),
)
class EventViewSet(
    GenericViewSet,
    ListModelMixin,
    RetrieveModelMixin,
    CreateModelMixin,
):
    """
    Generic events viewset
    """

    permission_classes = [IsObjectOwner, IsAuthenticated]
    serializer_class = PolymorphicEventSerializer
    queryset = Event.objects.all()
    lookup_field = "id"
    device = None
    stream = None

    def get_queryset(self, *args, **kwargs):
        return self.queryset.filter(user_id=self.request.user.id)

    def create(self, request, *args, **kwargs):
        logger.info("EventViewSet.create handling request.data %s", request.data)
        serializer = self.get_serializer(data=request.data)
        logger.info("EventViewSet.create got serializer %s", serializer)
        serializer.is_valid(raise_exception=True)
        logger.info("EventViewSet.create serializer is_valid=True")

        # assert user owns device
        if serializer.validated_data.get("device"):
            device = serializer.validated_data.get("device")
            if device.user != request.user:
                raise PermissionDenied(
                    {
                        "message": "You don't have permission to access",
                        "object_id": device.id,
                        "user_id": request.user.id,
                        "serializer_data": serializer.validated_data,
                    }
                )

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.validated_data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    def perform_create(self, serializer):
        device = serializer.validated_data.get("device")
        stream = janus_cloud_setup(device)
        return serializer.save(user=self.request.user, stream=stream)
