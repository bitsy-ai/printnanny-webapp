import logging
from django.shortcuts import get_object_or_404
from django.apps import apps
from drf_spectacular.utils import (
    extend_schema,
    extend_schema_view,
    OpenApiParameter,
)
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
    CreateModelMixin,
)
from print_nanny_webapp.utils.api.views import (
    generic_create_errors,
    generic_list_errors,
    generic_get_errors,
    generic_update_errors,
)
from print_nanny_webapp.tasks.models import Task, TaskStatus
from .serializers import PolymorphicTaskSerializer, TaskStatusSerializer

Device = apps.get_model("devices", "Device")

logger = logging.getLogger(__name__)


@extend_schema_view(
    list=extend_schema(
        tags=["tasks", "devices"],
        parameters=[
            OpenApiParameter(name="device_id", type=int, location=OpenApiParameter.PATH)
        ],
        responses={
            200: PolymorphicTaskSerializer(many=True),
        }
        | generic_list_errors,
    ),
    create=extend_schema(
        tags=["tasks", "devices"],
        parameters=[
            OpenApiParameter(name="device_id", type=int, location=OpenApiParameter.PATH)
        ],
        request=PolymorphicTaskSerializer,
        responses={
            201: PolymorphicTaskSerializer,
        }
        | generic_create_errors,
    ),
    retrieve=extend_schema(
        tags=["tasks", "devices"],
        parameters=[
            OpenApiParameter(
                name="device_id", type=int, location=OpenApiParameter.PATH
            ),
        ],
        request=PolymorphicTaskSerializer,
        responses={
            200: PolymorphicTaskSerializer,
        }
        | generic_get_errors,
    ),
    update=extend_schema(
        tags=["tasks", "devices"],
        parameters=[
            OpenApiParameter(
                name="device_id", type=int, location=OpenApiParameter.PATH
            ),
        ],
        request=PolymorphicTaskSerializer,
        responses={
            202: PolymorphicTaskSerializer,
        }
        | generic_update_errors,
    ),
)
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

    def create(self, request, *args, **kwargs):
        device_id = kwargs.get("device_id")
        if device_id is None:
            raise ValueError("Failed to parse :device_id from url path")
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.device = get_object_or_404(Device, pk=device_id)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    def perform_create(self, serializer):
        logger.info("TaskViewSet.perform_create request=%s", self.request.POST)
        serializer.save(user=self.request.user, device=self.device)


@extend_schema_view(
    list=extend_schema(
        tags=["tasks", "devices"],
        parameters=[
            OpenApiParameter(
                name="device_id", type=int, location=OpenApiParameter.PATH
            ),
            OpenApiParameter(name="task_id", type=int, location=OpenApiParameter.PATH),
        ],
        responses={
            200: TaskStatusSerializer(many=True),
        }
        | generic_list_errors,
    ),
    create=extend_schema(
        tags=["tasks", "devices"],
        parameters=[
            OpenApiParameter(
                name="device_id", type=int, location=OpenApiParameter.PATH
            ),
            OpenApiParameter(name="task_id", type=int, location=OpenApiParameter.PATH),
        ],
        request=TaskStatusSerializer,
        responses={
            201: TaskStatusSerializer,
        }
        | generic_create_errors,
    ),
    retrieve=extend_schema(
        tags=["tasks", "devices"],
        parameters=[
            OpenApiParameter(
                name="device_id", type=int, location=OpenApiParameter.PATH
            ),
            OpenApiParameter(name="task_id", type=int, location=OpenApiParameter.PATH),
        ],
        request=TaskStatusSerializer,
        responses={
            200: TaskStatusSerializer,
        }
        | generic_get_errors,
    ),
)
class TaskStatusViewSet(
    GenericViewSet,
    ListModelMixin,
    RetrieveModelMixin,
    CreateModelMixin,
):
    serializer_class = TaskStatusSerializer
    queryset = TaskStatus.objects.all()
    lookup_field = "id"
