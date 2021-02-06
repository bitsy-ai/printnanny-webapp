from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from drf_spectacular.utils import extend_schema

from print_nanny_webapp.ml_ops.models import ModelArtifact
from .serializers import ModelArtifactSerializer


@extend_schema(tags=["ml-ops"])
class ModelArtifactViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    serializer_class = ModelArtifactSerializer
    queryset = ModelArtifact.objects.all()
    lookup_field = "id"
