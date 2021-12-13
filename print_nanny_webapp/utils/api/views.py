from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from .service import get_api_config
from .serializers import PrintNannyApiConfigSerializer, ErrorDetailSerializer


list_desired_config_schema = extend_schema(
    responses={
        "default": ErrorDetailSerializer,
        200: PrintNannyApiConfigSerializer,
    },
)


@extend_schema_view(
    list=list_desired_config_schema,
)
class PrintNannyApiConfigViewset(ViewSet):
    def list(self, request, *args, **kwargs):
        data = get_api_config(request)
        serializer = PrintNannyApiConfigSerializer(instance=data)

        return Response(serializer.data)
