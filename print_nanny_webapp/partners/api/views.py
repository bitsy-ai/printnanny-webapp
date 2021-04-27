from django.apps import apps
from rest_framework.viewsets import ViewSet
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema, extend_schema_serializer
from print_nanny_webapp.partners.authentication import GeeksTokenAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response

from .serializers import GeeksMetadataSerializer

GeeksToken = apps.get_model("partners", "GeeksToken")
OctoPrintDevice = apps.get_model("remote_control", "OctoPrintDevice")


class GeeksViewSet(ViewSet):
    """
    3D Geeks calls this endpoint to validate token & fetch printer metadata
    """

    authentication_classes = [GeeksTokenAuthentication]
    @extend_schema(
        tags=["3dgeeks", "partners"],
        operation_id="geeks_3d_metadata_retrieve",
        responses={
            200: GeeksMetadataSerializer,
        },
    )
    def retrieve(self, request, pk=None):
        queryset = GeeksToken.objects.all()
        token = get_object_or_404(queryset, pk=pk)
        serializer = GeeksMetadataSerializer(token.octoprint_device)
        return Response(serializer.data)