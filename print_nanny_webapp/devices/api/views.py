from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    CreateModelMixin,
)
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .serializers import DeviceSerializer, DeviceIdentitySerializer
from ..models import Device


@extend_schema(tags=["devices"])
class DeviceViewSet(
    GenericViewSet,
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
):

    serializer_class = DeviceSerializer
    queryset = Device.objects.all()
    lookup_field = "id"

    @extend_schema(
        operation_id="devices_update_or_create",
        request=DeviceSerializer,
        responses={
            400: DeviceIdentitySerializer,
            200: DeviceIdentitySerializer,
            201: DeviceIdentitySerializer,
            202: DeviceIdentitySerializer,
        },
    )
    @action(methods=["post"], detail=False, url_path="update-or-create")
    def update_or_create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            validated_data = serializer.validated_data.copy()
            del validated_data["serial"]
            instance, created = serializer.update_or_create(
                request.user, serializer.validated_data.get("serial"), validated_data
            )

            context = {"request": self.request}
            context.update(self.get_serializer_context())

            response_serializer = DeviceIdentitySerializer(
                instance=instance, context=context
            )
            if not created:
                return Response(
                    response_serializer.data, status=status.HTTP_202_ACCEPTED
                )
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(
        operation_id="devices_update",
        parameters=[],
        responses={
            200: DeviceSerializer,
            202: DeviceSerializer,
        },
    )
    def update(self, *args, **kwargs):
        return super().update(*args, **kwargs)

    @extend_schema(
        operation_id="devices_partial_update",
        responses={
            200: DeviceSerializer,
            202: DeviceSerializer,
        },
    )
    def partial_update(self, *args, **kwargs):
        return super().partial_update(*args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
