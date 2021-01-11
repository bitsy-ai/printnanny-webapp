from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.viewsets import GenericViewSet, ViewSet
from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    CreateModelMixin,
)
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import PolymorphicProxySerializer, OpenApiParameter

from .serializers import ManualVideoUploadAlertSerializer, AlertPolymorphicSerializer, AlertSerializer, RemoteControlCommandAlertSerializer
from ..models import ManualVideoUploadAlert, Alert


        
# @extend_schema(tags=["alerts"], responses={
#     200: PolymorphicProxySerializer(
#         component_name='Alert',
#         serializers=[AlertSerializer, RemoteControlCommandAlertSerializer, ManualVideoUploadAlertSerializer],
#         resource_type_field_name='type',
#     ),
# })
class AlertViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    serializer_class = AlertPolymorphicSerializer
    queryset = Alert.objects.all()
    lookup_field = "id"

# @extend_schema(tags=["alerts"])
# class ManualVideoUploadAlertViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):
#     serializer_class = AlertPolymorphicSerializer
#     queryset = ManualVideoUploadAlert.objects.all()
#     lookup_field = "id"

#     def get_queryset(self, *args, **kwargs):
#         return self.queryset.filter(user_id=self.request.user.id)

#     def perform_create(self, serializer):
#         instance = serializer.save(user=self.request.user)

#     @extend_schema(
#         operation_id="alert_message_cancel_print",
#         responses={
#             400: AlertPolymorphicSerializer,
#             200: AlertPolymorphicSerializer,
#         },
#         parameters=[
#             OpenApiParameter(
#                 "action", enum=ManualVideoUploadAlert.ActionChoices, required=True
#             )
#         ],
#     )
#     @action(methods=["GET"], detail=True)
#     def feedback(self, request, *args, **kwargs):
#         action = self.request.query_params.get("action", None)
#         if action is None:
#             return Response(
#                 f"Please specify action={list(ManualVideoUploadAlert.ActionChoices)}",
#                 status=status.HTTP_400_BAD_REQUEST,
#             )
#         action = action.upper()
#         if action not in ManualVideoUploadAlert.ActionChoices:
#             return Response(
#                 f"Please specify action={list(ManualVideoUploadAlert.ActionChoices)}",
#                 status=status.HTTP_400_BAD_REQUEST,
#             )

#         data = {"last_action": ManualVideoUploadAlert.ActionChoices[action]}
#         instance = self.get_object()
#         serializer = self.get_serializer(instance, data=data, partial=True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)

