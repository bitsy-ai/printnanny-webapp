from django.apps import apps
from rest_framework.viewsets import ViewSet
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema, extend_schema_serializer
from print_nanny_webapp.partners.authentication import GeeksTokenAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action

from .serializers import Partner3DGeeksMetadataSerializer, Partner3DGeeksAlertSerializer

GeeksToken = apps.get_model("partners", "GeeksToken")
OctoPrintDevice = apps.get_model("remote_control", "OctoPrintDevice")
AlertsMessage = apps.get_model("alerts", "AlertMessage")


class GeeksViewSet(ViewSet):
    """
    3D Geeks calls this endpoint to validate token & fetch printer metadata
    """

    authentication_classes = [GeeksTokenAuthentication]

    @extend_schema(
        tags=["partners.geeks3d"],
        operation_id="metadata_retrieve",
        responses={
            200: Partner3DGeeksMetadataSerializer,
        },
    )
    def retrieve(self, request, pk=None):
        queryset = GeeksToken.objects.all()
        token = get_object_or_404(queryset, pk=pk)
        token.verified = True
        token.save()
        serializer = Partner3DGeeksMetadataSerializer(token.octoprint_device)
        return Response(serializer.data)

    @extend_schema(
        tags=["partners.geeks3"],
        operation_id="alerts_list",
        responses={200: Partner3DGeeksAlertSerializer},
    )
    @action(detail=True, methods=["GET"])
    def alerts(self, request, pk=None):
        queryset = GeeksToken.objects.all()
        token = get_object_or_404(queryset, pk=pk)
        alerts = AlertsMessage.objects.filter(
            octoprint_device_id=token.octoprint_device_id
        )
        serializer = Partner3DGeeksAlertSerializer(alerts, many=True)
        return Response(serializer.data)
