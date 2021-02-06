from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (ListModelMixin, RetrieveModelMixin)
from drf_spectacular.utils import extend_schema

from print_nanny_webapp.ml_ops.models import TFLiteModel
from .serializers import TFLiteModelSerializer


@extend_schema(tags=["ml-ops"])
class TFLiteModelViewSet(
    ListModelMixin,
    RetrieveModelMixin,
    GenericViewSet
):
    serializer_class = TFLiteModelSerializer
    queryset = TFLiteModel.objects.all()
    lookup_field = "id"

