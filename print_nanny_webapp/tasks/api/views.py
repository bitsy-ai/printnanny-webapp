import logging
from django.shortcuts import get_object_or_404
from django.apps import apps
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
    CreateModelMixin,
)
from print_nanny_webapp.tasks.models import Task
from .serializers import PolymorphicTaskSerializer

Device = apps.get_model("devices", "Device")

logger = logging.getLogger(__name__)


@extend_schema(tags=["tasks"])
class TaskViewSet(
    GenericViewSet,
    ListModelMixin,
    RetrieveModelMixin,
    CreateModelMixin,
):
    serializer_class = PolymorphicTaskSerializer
    queryset = Task.objects.all()
    lookup_field = "id"
    device = None

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
