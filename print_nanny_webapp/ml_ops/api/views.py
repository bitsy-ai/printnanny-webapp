from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from drf_spectacular.utils import extend_schema

from print_nanny_webapp.ml_ops.models import ModelArtifact, ExperimentDeviceConfig
from .serializers import ModelArtifactSerializer, ExperimentDeviceConfigSerializer


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
