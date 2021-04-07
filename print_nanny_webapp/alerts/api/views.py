import logging
from drf_spectacular.utils import extend_schema, extend_schema_view
from django.db.models import Q

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

from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import PolymorphicProxySerializer, OpenApiParameter
from django.apps import apps
from .serializers import (
    ManualVideoUploadAlertSerializer,
    AlertSettingsPolymorphicSerializer,
    AlertPolymorphicSerializer,
    AlertSerializer,
    AlertBulkRequestSerializer,
    AlertBulkResponseSerializer,
    RemoteControlCommandAlertSerializer,
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
    AlertSettings,
    PrintSessionAlert,
    PrintSessionAlertSettings
)

logger = logging.getLogger(__name__)

PrintSession = apps.get_model("remote_control", "PrintSession")


@extend_schema(
    tags=["alerts"],
    responses={
        200: PrintSessionAlertSerializer,
        201: PrintSessionAlertSerializer,
        202: PrintSessionAlertSerializer,
    },
)
class PrintSessionAlertViewSet(
    GenericViewSet,
    ListModelMixin,
    RetrieveModelMixin,
    CreateModelMixin,
):
    lookup_fields = ("print_session", "id")
    serializer_class = PrintSessionAlertSerializer

    def get_queryset(self):
        user = self.request.user
        return PrintSessionAlert.objects.filter(user=user).all()

    @extend_schema(
        tags=["alerts"],
        request=CreatePrintSessionAlertSerializer,
        operation_id="print_session_alert_create",
        responses={
            201: PrintSessionAlertSerializer,
            400: PrintSessionAlertSerializer,
            403: PrintSessionAlertSerializer,
            409: PrintSessionAlertSerializer,
        },
    )
    def create(self, request, permissions=[IsAdminOrIsPrintSessionOwner]):
        session = request.data.get("print_session")
        session = PrintSession.objects.get(session=session)

        request_serializer = CreatePrintSessionAlertSerializer(
            data=request.data,
            context={"request": request},
        )
        if request_serializer.is_valid():
            instance = serializer.save()
            instance.trigger_alerts_task(serializer.data)
            response_serializer = PrintSessionAlertSerializer(instance)

            return Response(response_serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# TODO combine defect, end, progress events into PrintSessionAlert subtypes
# @extend_schema(
#     tags=["alerts"],
#     responses={
#         200: DefectAlertSerializer,
#         201: DefectAlertSerializer,
#         202: DefectAlertSerializer,
#     },
# )
# class DefectAlertViewSet(
#     GenericViewSet,
#     ListModelMixin,
#     RetrieveModelMixin,
#     CreateModelMixin,
#     UpdateModelMixin,
# ):
#     serializer_class = DefectAlertSerializer
#     queryset = DefectAlert.objects.all()

#     def get_queryset(self):
#         user = self.request.user
#         return DefectAlert.objects.filter(user=user).all()

#     @extend_schema(
#         tags=["alerts"],
#         request=CreateDefectAlertSerializer,
#         operation_id="defect_alert_create",
#         responses={
#             201: DefectAlertSerializer,
#             400: DefectAlertSerializer,
#             403: DefectAlertSerializer,
#         },
#     )
#     def create(self, request, permissions=[IsAdminOrIsPrintSessionOwner]):
#         session = request.data.get("print_session")
#         session = PrintSession.objects.get(session=session)
#         serializer = DefectAlertSerializer(
#             data={
#                 "print_session": session.id,
#                 "user": session.user.id,
#                 "octoprint_device": session.octoprint_device.id,
#             },
#             context={"request": request},
#         )
#         if serializer.is_valid() and session.should_alert is True:
#             alert_settings, created = DefectAlertSettings.objects.get_or_create(
#                 user=session.user,
#             )
#             instance = serializer.save(
#                 user=session.user,
#                 octoprint_device=session.octoprint_device,
#                 print_session=session,
#                 alert_methods=alert_settings.alert_methods,
#             )
#             instance.trigger_alerts_task(serializer.data)

#             return Response(serializer.data, status.HTTP_201_CREATED)
#         elif session.should_alert is False:
#             return Response(
#                 {"error": "Alerts are supressed"}, status=status.HTTP_409_CONFLICT
#             )
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     # @extend_schema(
#     #     tags=["alerts"],
#     #     request=AlertBulkRequestSerializer,
#     #     operation_id="defect_alert_supress",
#     #     responses={
#     #         200: DefectAlertSerializer,
#     #         400: DefectAlertSerializer,
#     #         403: DefectAlertSerializer,
#     #     },
#     # )
#     # @action(
#     #     detail=True, methods=["GET", "POST"]
#     # )  # GET method is required to render as a href / raw link in emails
#     # def supress(self, request, permission_classes=[IsAdminOrIsSelf]):
#     #     defect_alert = self.get_object()

#     #     defect_alert.print_session.supress_alerts = True
#     #     defect_alert.save()
#     #     serializer = self.get_serializer(defect_alert)
#     #     return Response(serializer.data, status.HTTP_202_ACCEPTED)

#     @extend_schema(
#         tags=["alerts"],
#         request=AlertBulkRequestSerializer,
#         operation_id="defect_alert_stop_print",
#         responses={
#             200: DefectAlertSerializer,
#             400: DefectAlertSerializer,
#             403: DefectAlertSerializer,
#         },
#     )
#     @action(
#         detail=True, methods=["GET", "POST"]
#     )  # GET method is required to render as a href / raw link in emails
#     def stop_print(self, request, permission_classes=[IsAdminOrIsSelf]):
#         defect_alert = self.get_object()
#         remote_control_command = RemoteControlCommand.objects.create(
#             command=RemoteControlCommand.PRINT_STOP,
#             user=defect_alert.user,
#             device=defect_alert.octoprint_device,
#         )
#         serializer = self.get_serializer(defect_alert)
#         return Response(serializer.data, status.HTTP_202_ACCEPTED)


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
        return Alert.objects.filter(user=user).order_by("-seen", "-updated_dt").all()

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
        logger.info(f"serializer data {serializer.data}")

        return Response(serializer.data)


@extend_schema(tags=["alert-settings"])
class AlertSettingsViewSet(
    GenericViewSet,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
):

    serializer_class = AlertSettingsPolymorphicSerializer
    queryset = AlertSettings.objects.all()
    lookup_field = "id"

    @extend_schema(tags=["alert_settings"], responses={200: AlertMethodSerializer})
    @action(detail=False)
    def methods(self, request):
        data = [
            {"label": label, "value": value}
            for label, value in Alert.AlertMethodChoices.choices
        ]
        serializer = AlertMethodSerializer(data=data, many=True)
        serializer.is_valid()
        return Response(serializer.data)
