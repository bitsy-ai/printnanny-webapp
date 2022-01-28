import logging
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.response import Response
from django.apps import apps
from drf_spectacular.utils import PolymorphicProxySerializer
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin
from print_nanny_webapp.events.models import Event, TestEvent, DeviceEvent
from .serializers import PolymorphicEventSerializer, TestEventSerializer
from print_nanny_webapp.utils.api.views import (
    generic_create_errors,
    generic_list_errors,
    generic_get_errors,
    generic_update_errors,
)

Device = apps.get_model("devices", "Device")

logger = logging.getLogger(__name__)

# @extend_schema_view(
#     create=extend_schema(
#         request=PolymorphicEventSerializer,
#         responses={
#             201: PolymorphicEventSerializer,
#         } | generic_create_errors
#     )
# )


@extend_schema(tags=["events", "devices"])
class DeviceEventViewSet(
    GenericViewSet, ListModelMixin, RetrieveModelMixin, CreateModelMixin
):
    serializer_class = PolymorphicEventSerializer
    queryset = DeviceEvent.objects.all()
    lookup_field = "id"

    def get_queryset(self, *args, **kwargs):
        device_id = self.kwargs.get("device_id")
        self.device = get_object_or_404(Device, pk=device_id)
        return self.queryset.filter(user_id=self.request.user.id, device=self.device)

    def create(self, request, device_id=None, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.device = get_object_or_404(Device, pk=device_id)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    def perform_create(self, serializer):
        logger.info(f"DeviceEventViewSet.perform_create request={self.request.POST}")
        serializer.save(user=self.request.user, device=self.device)
