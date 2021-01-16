import logging
from drf_spectacular.utils import extend_schema, extend_schema_view

from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ViewSet
from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    CreateModelMixin,
)
from rest_framework.decorators import action

from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import PolymorphicProxySerializer, OpenApiParameter

from .serializers import (ManualVideoUploadAlertSerializer, AlertPolymorphicSerializer, AlertSerializer,
    AlertBulkRequestSerializer,
    AlertBulkResponseSerializer,
    RemoteControlCommandAlertSerializer
)
from ..models import ManualVideoUploadAlert, Alert

logger = logging.getLogger(__name__)

class AlertViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin, UpdateModelMixin):
    serializer_class = AlertPolymorphicSerializer
    queryset = Alert.objects.all()
    lookup_field = "id"

    @extend_schema(tags=["alerts"],
    request= AlertBulkRequestSerializer,
    operation_id='alerts_dismiss',
    responses={
        200: AlertBulkResponseSerializer,
        202: AlertBulkResponseSerializer,
    })
    @action(detail=False, methods=["PATCH"])
    def dismiss(self, request):
        ids = request.data.get('ids', [])

        updated_alerts = Alert.objects.filter(
            user=request.user,
            id__in=ids
        ).update(dismissed=True, seen=True)

        data = dict(updated=updated_alerts, received=len(ids))

        serializer = AlertBulkResponseSerializer(data=data)
        serializer.is_valid()
        return Response(serializer.data)

    @extend_schema(tags=["alerts"],
    request=AlertBulkRequestSerializer,
    operation_id='alerts_seen',
    responses={
        200: AlertBulkResponseSerializer,
        202: AlertBulkResponseSerializer
    })
    @action(detail=False, methods=["PATCH"])
    def seen(self, request):
        
        ids = request.data.get('ids', [])

        updated_alerts = Alert.objects.filter(
            user=request.user,
            id__in=ids
        ).update(seen=True)

        data = dict(updated=updated_alerts, received=len(ids))

        serializer = AlertBulkResponseSerializer(data=data)
        serializer.is_valid()
        return Response(serializer.data)


    @action(detail=False)
    def recent(self, request):
        recent_alerts = Alert.objects.filter(
            user=request.user,
            dismissed=False
        ).order_by('-updated_dt')

        page = self.paginate_queryset(recent_alerts)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(recent_alerts, many=True)
        
        return Response(serializer.data)

    @action(detail=False)
    def unread(self, request):
        recent_alerts = Alert.objects.filter(
            user=request.user,
            dismissed=False,
            seen=False
        ).order_by('-updated_dt')

        page = self.paginate_queryset(recent_alerts)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(recent_alerts, many=True)
        
        return Response(serializer.data)

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

