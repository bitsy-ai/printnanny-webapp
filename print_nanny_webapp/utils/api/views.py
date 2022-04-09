from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.viewsets import ViewSet, GenericViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.views import APIView


from .service import get_api_config
from .serializers import PrintNannyApiConfigSerializer, ErrorDetailSerializer


generic_list_errors = {
    400: ErrorDetailSerializer,
    401: ErrorDetailSerializer,
    403: ErrorDetailSerializer,
    500: ErrorDetailSerializer,
}

generic_get_errors = {404: ErrorDetailSerializer} | generic_list_errors


generic_create_errors = {409: ErrorDetailSerializer} | generic_list_errors

generic_update_errors = generic_create_errors


class PrintNannyApiConfigViewset(APIView):
    @extend_schema(
        operation_id="api_config_retreive",
        tags=["client", "config"],
        responses={
            200: PrintNannyApiConfigSerializer(many=False),
        }
        | generic_get_errors,
    )
    def get(self, request, *args, **kwargs):
        data = get_api_config(request)
        serializer = PrintNannyApiConfigSerializer(
            instance=data, context=dict(request=request), many=False
        )
        return Response(serializer.data)
