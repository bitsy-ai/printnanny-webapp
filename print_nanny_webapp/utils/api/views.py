from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from .service import get_api_config
from .serializers import PrintNannyApiConfigSerializer


class PrintNannyApiConfigViewset(ViewSet):
    def list(self, request, *args, **kwargs):
        data = get_api_config(request)
        serializer = PrintNannyApiConfigSerializer(instance=data)

        return Response(serializer.data)
