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
from drf_spectacular.utils import PolymorphicProxySerializer, OpenApiParameter
from django.apps import apps
from .serializers import (
    # ManualVideoUploadAlertSerializer,
    AlertPolymorphicSerializer,
    AlertSerializer,
    AlertBulkRequestSerializer,
    AlertBulkResponseSerializer,
    AlertMethodSerializer,
    CreatePrintSessionAlertSerializer,
    PrintSessionAlertSerializer,
)
from print_nanny_webapp.utils.permissions import (
    IsAdminOrIsSelf,
    IsAdminOrIsPrintSessionOwner,
)
from ..models import (
    ManualVideoUploadAlert,
    Alert,
    PrintSessionAlert,
)

logger = logging.getLogger(__name__)

PrintSession = apps.get_model("remote_control", "PrintSession")


class AlreadyExists(APIException):
    status_code = 409
    default_detail = "A resource of this type already exists, ignoring request"
    default_code = "already_exists"


# @extend_schema_view(
#     tags=["alerts"],
#     responses={
#         200: PrintSessionAlertSerializer,
#         201: PrintSessionAlertSerializer,
#         202: PrintSessionAlertSerializer,
#     },
#     list=extend_schema(operation_id="print_session_alerts_list"),
# )
# class PrintSessionAlertViewSet(
#     GenericViewSet,
#     ListModelMixin,
#     RetrieveModelMixin,
#     CreateModelMixin,
# ):
#     lookup_fields = ("print_session", "id")
#     serializer_class = PrintSessionAlertSerializer

#     def get_queryset(self):
#         user = self.request.user
#         return PrintSessionAlert.objects.filter(user=user).all()

#     @extend_schema(
#         tags=["alerts"],
#         request=CreatePrintSessionAlertSerializer,
#         operation_id="print_session_alert_create",
#         responses={
#             201: PrintSessionAlertSerializer,
#             400: PrintSessionAlertSerializer,
#             403: PrintSessionAlertSerializer,
#             409: PrintSessionAlertSerializer,
#         },
#     )
#     def create(self, request, permissions=[IsAdminOrIsPrintSessionOwner]):
#         session = request.data.get("print_session")
#         session = PrintSession.objects.get(session=session)

#         request_serializer = CreatePrintSessionAlertSerializer(
#             data=request.data,
#             context={"request": request},
#         )
#         if request_serializer.is_valid():
#             try:
#                 instance = request_serializer.save()
#             except IntegrityError:
#                 raise AlreadyExists()

#             response_serializer = PrintSessionAlertSerializer(instance)
#             instance.trigger_alerts_task(response_serializer.data)

#             return Response(response_serializer.data, status.HTTP_201_CREATED)
#         return Response(request_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema_view(
    tags=["alerts"],
    responses={
        200: AlertPolymorphicSerializer,
        201: AlertPolymorphicSerializer,
        202: AlertPolymorphicSerializer,
    },
)
class AlertViewSet(
    GenericViewSet,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
):
    serializer_class = AlertPolymorphicSerializer
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
