import logging

from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiParameter
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from rest_framework import parsers
from rest_framework.decorators import action
from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    CreateModelMixin,
)
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from print_nanny_webapp.moonraker.models import MoonrakerServer
from print_nanny_webapp.moonraker.api.serializers import MoonrakerServerSerializer
from print_nanny_webapp.utils.api.views import (
    generic_create_errors,
    generic_list_errors,
    generic_update_errors,
    generic_get_errors,
)

##
# MoonrakerServer (no device filter)
##
@extend_schema_view(
    list=extend_schema(
        tags=["Mmonraker"],
        responses={
            200: MoonrakerServerSerializer(many=True),
        }
        | generic_list_errors,
    ),
    retrieve=extend_schema(
        tags=["moonraker"],
        responses={
            200: MoonrakerServerSerializer(),
        }
        | generic_get_errors,
    ),
    create=extend_schema(
        tags=["moonraker"],
        request=MoonrakerServerSerializer,
        responses={
            201: MoonrakerServerSerializer,
        }
        | generic_create_errors,
    ),
    update=extend_schema(
        tags=["moonraker"],
        request=MoonrakerServerSerializer,
        responses={
            202: MoonrakerServerSerializer,
        }
        | generic_update_errors,
    ),
)
class MoonrakerServerViewSet(
    GenericViewSet,
    CreateModelMixin,
    ListModelMixin,
    UpdateModelMixin,
):
    serializer_class = MoonrakerServerSerializer
    queryset = MoonrakerServer.objects.all()
    lookup_field = "id"

    @extend_schema(
        operation_id="moonraker_server_update_or_create",
        responses={
            # 400: PrinterProfileSerializer,
            200: MoonrakerServerSerializer,
            201: MoonrakerServerSerializer,
        },
        tags=["moonraker"],
    )
    @action(methods=["post"], detail=False, url_path="update-or-create")
    def update_or_create(self, request, device_id=None):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            device_id = request.data.get("device")
            instance, created = serializer.update_or_create(  # type: ignore[attr-defined]
                serializer.validated_data, device_id, self.request.user
            )
            response_serializer = self.get_serializer(instance)
            if not created:
                return Response(response_serializer.data, status=status.HTTP_200_OK)
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
