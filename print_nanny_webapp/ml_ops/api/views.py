from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from drf_spectacular.utils import extend_schema
from rest_framework.decorators import action
from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiParameter
from rest_framework.response import Response

from print_nanny_webapp.ml_ops.models import (
    ModelArtifact,
    ExperimentDeviceConfig,
    DeviceCalibration,
)
from .serializers import (
    ModelArtifactSerializer,
    ExperimentDeviceConfigSerializer,
    DeviceCalibrationSerializer,
)


@extend_schema(tags=["ml-ops"])
class DeviceCalibrationViewSet(
    UpdateModelMixin, ListModelMixin, RetrieveModelMixin, GenericViewSet
):
    serializer_class = DeviceCalibrationSerializer
    queryset = DeviceCalibration.objects.all()
    lookup_field = "id"

    def get_queryset(self):
        user = self.request.user
        return ExperimentDeviceConfig.objects.filter(device__user=user).all()

    @extend_schema(
        operation_id="device_calibration_update_or_create",
        responses={
            400: DeviceCalibrationSerializer,
            200: DeviceCalibrationSerializer,
            201: DeviceCalibrationSerializer,
        },
    )
    @action(methods=["post"], detail=False, url_path="update-or-create")
    def update_or_create(self, request):

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            instance, created = serializer.update_or_create(serializer.validated_data)
            response_serializer = self.get_serializer(instance)
            if not created:
                return Response(response_serializer.data, status=status.HTTP_200_OK)
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


@extend_schema(tags=["ml-ops"])
class ModelArtifactViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    serializer_class = ModelArtifactSerializer
    queryset = ModelArtifact.objects.all()
    lookup_field = "id"


@extend_schema(tags=["ml-ops"])
class ExperimentDeviceConfigViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    serializer_class = ExperimentDeviceConfigSerializer
    queryset = ExperimentDeviceConfig.objects.all()
    lookup_field = "id"

    def get_queryset(self):
        user = self.request.user
        return ExperimentDeviceConfig.objects.filter(device__user=user).all()
