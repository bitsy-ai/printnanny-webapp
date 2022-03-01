import logging
import json
from typing import TYPE_CHECKING
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema
from django.core.files.base import ContentFile


from print_nanny_webapp.ml_ops.models import (
    ModelArtifact,
    ExperimentDeviceConfig,
    DeviceCalibration,
    Experiment,
)
from .serializers import (
    ModelArtifactSerializer,
    ExperimentDeviceConfigSerializer,
    DeviceCalibrationSerializer,
    ExperimentSerializer,
)

logger = logging.getLogger(__name__)

# https://github.com/typeddjango/django-stubs/issues/599
if TYPE_CHECKING:
    from print_nanny_webapp.users.models import User as UserType


@extend_schema(
    tags=["ml-ops"],
    responses={
        400: DeviceCalibrationSerializer,
        200: DeviceCalibrationSerializer,
        201: DeviceCalibrationSerializer,
    },
)
class DeviceCalibrationViewSet(
    UpdateModelMixin, ListModelMixin, RetrieveModelMixin, GenericViewSet
):
    serializer_class = DeviceCalibrationSerializer
    queryset = DeviceCalibration.objects.all()
    lookup_field = "id"

    def get_queryset(self):
        user = self.request.user  # type: ignore
        return DeviceCalibration.objects.filter(octoprint_device__user=user).all()

    @extend_schema(operation_id="device_calibration_update_or_create")
    @action(methods=["post"], detail=False, url_path="update-or-create")
    def update_or_create(self, request):

        octoprint_device_id = request.data.get("octoprint_device")

        instance = DeviceCalibration.objects.filter(
            octoprint_device=octoprint_device_id
        ).first()
        serializer = self.get_serializer(data=request.data, instance=instance)

        if serializer.is_valid():
            config_file_content = json.dumps(
                dict(
                    fps=serializer.validated_data["fps"],
                    mask=serializer.validated_data["mask"],
                    coordinates=serializer.validated_data["coordinates"],
                )
            ).encode("utf-8")
            # config_file_content = ContentFile(config_file_content)
            instance, created = serializer.update_or_create(serializer.validated_data)  # type: ignore[attr-defined]
            # instance.config_file.save("calibration.json", config_file_content)
            response_serializer = self.get_serializer(instance)
            if not created:
                return Response(
                    response_serializer.data, status=status.HTTP_202_ACCEPTED
                )
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(tags=["ml-ops"])
class ModelArtifactViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    serializer_class = ModelArtifactSerializer
    queryset = ModelArtifact.objects.all()
    lookup_field = "id"


@extend_schema(tags=["ml-ops"])
class ExperimentViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    serializer_class = ExperimentSerializer
    queryset = Experiment.objects.all()
    lookup_field = "id"


@extend_schema(tags=["ml-ops"])
class ExperimentDeviceConfigViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    serializer_class = ExperimentDeviceConfigSerializer
    queryset = ExperimentDeviceConfig.objects.all()
    lookup_field = "id"

    def get_queryset(self):
        user = self.request.user
        return ExperimentDeviceConfig.objects.filter(device__user=user).all()
