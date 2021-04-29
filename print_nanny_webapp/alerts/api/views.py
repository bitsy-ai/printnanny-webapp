import logging
from drf_spectacular.utils import extend_schema, extend_schema_view
from django.db.models import Q
from rest_framework.exceptions import APIException

from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ViewSet
from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    CreateModelMixin,
)
from rest_framework.decorators import action
from rest_framework import status
from django.db.utils import IntegrityError
from drf_spectacular.types import OpenApiTypes
from django.apps import apps
from .serializers import (
    # ManualVideoUploadAlertSerializer,
    AlertSerializer,
    AlertBulkRequestSerializer,
    AlertBulkResponseSerializer,
)
from print_nanny_webapp.utils.permissions import (
    IsAdminOrIsSelf,
    IsAdminOrIsPrintSessionOwner,
)
from ..models import (
    Alert,
)

logger = logging.getLogger(__name__)

PrintSession = apps.get_model("remote_control", "PrintSession")


class AlreadyExists(APIException):
    status_code = 409
    default_detail = "A resource of this type already exists, ignoring request"
    default_code = "already_exists"


@extend_schema_view(
    tags=["alerts"],
    responses={
        200: AlertSerializer,
        201: AlertSerializer,
        202: AlertSerializer,
    },
)
class AlertViewSet(
    GenericViewSet,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
):
    serializer_class = AlertSerializer
    queryset = Alert.objects.all()
    lookup_field = "id"

    def get_queryset(self):
        user = self.request.user
        return Alert.objects.filter(user=user).all()

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

    @extend_schema(
        tags=["alerts"],
        request=AlertBulkRequestSerializer,
        operation_id="alerts_recent",
        responses={200: AlertBulkResponseSerializer, 202: AlertBulkResponseSerializer},
    )
    @action(detail=False)
    def recent(self, request):
        recent_alerts = Alert.objects.filter(user=request.user).order_by("-updated_dt")

        page = self.paginate_queryset(recent_alerts)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(recent_alerts, many=True)

        return Response(serializer.data)

    @extend_schema(
        tags=["alerts"],
        request=AlertBulkRequestSerializer,
        operation_id="alerts_unread",
        responses={200: AlertBulkResponseSerializer, 202: AlertBulkResponseSerializer},
    )
    @action(detail=False)
    def unread(self, request):
        recent_alerts = Alert.objects.filter(user=request.user, seen=False).order_by(
            "-updated_dt"
        )

        page = self.paginate_queryset(recent_alerts)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(recent_alerts, many=True)

        logger.info(serializer)
        logger.info(f"serializer data {serializer.data}")

        return Response(serializer.data)
