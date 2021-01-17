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

from .serializers import (
    ManualVideoUploadAlertSerializer,
    AlertPolymorphicSerializer,
    AlertSerializer,
    AlertBulkRequestSerializer,
    AlertBulkResponseSerializer,
    RemoteControlCommandAlertSerializer,
)
from ..models import ManualVideoUploadAlert, Alert

logger = logging.getLogger(__name__)


class AlertViewSet(
    GenericViewSet, ListModelMixin, RetrieveModelMixin, UpdateModelMixin,
):
    serializer_class = AlertPolymorphicSerializer
    queryset = Alert.objects.all()
    lookup_field = "id"

    def get_queryset(self):
        user = self.request.user
        return Alert.objects.filter(user=user).order_by('-seen','-updated_dt').all()

    @extend_schema(
        tags=["alerts"],
        request=AlertBulkRequestSerializer,
        operation_id="alerts_dismiss",
        responses={
            200: AlertBulkResponseSerializer,
            202: AlertBulkResponseSerializer,
        },
    )
    @action(detail=False, methods=["PATCH"])
    def dismiss(self, request):
        ids = request.data.get("ids", [])

        updated_alerts = Alert.objects.filter(user=request.user, id__in=ids).update(
            dismissed=True, seen=True
        )

        data = dict(updated=updated_alerts, received=len(ids))

        serializer = AlertBulkResponseSerializer(data=data)
        serializer.is_valid()
        return Response(serializer.data)

    @extend_schema(
        tags=["alerts"],
        request=AlertBulkRequestSerializer,
        operation_id="alerts_seen",
        responses={200: AlertBulkResponseSerializer, 202: AlertBulkResponseSerializer},
    )
    @action(detail=False, methods=["PATCH"])
    def seen(self, request):

        ids = request.data.get("ids", [])

        updated_alerts = Alert.objects.filter(user=request.user, id__in=ids).update(
            seen=True
        )

        data = dict(updated=updated_alerts, received=len(ids))

        serializer = AlertBulkResponseSerializer(data=data)
        serializer.is_valid()
        return Response(serializer.data)

    @action(detail=False)
    def recent(self, request):
        recent_alerts = Alert.objects.filter(
            user=request.user, dismissed=False
        ).order_by("-updated_dt")

        page = self.paginate_queryset(recent_alerts)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(recent_alerts, many=True)

        return Response(serializer.data)

    @action(detail=False)
    def unread(self, request):
        recent_alerts = Alert.objects.filter(
            user=request.user, dismissed=False, seen=False
        ).order_by("-updated_dt")

        page = self.paginate_queryset(recent_alerts)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(recent_alerts, many=True)

        logger.info(serializer)
        logger.info(f'serializer data {serializer.data}')

        return Response(serializer.data)
