import logging
from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiParameter
from django.apps import apps


from rest_framework import status, parsers
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
    CreateModelMixin,
    UpdateModelMixin,
)
from print_nanny_webapp.events.models.alerts import EmailAlertSettings, PrintJobAlert
from print_nanny_webapp.utils.api.views import (
    generic_get_errors,
    generic_create_errors,
    generic_list_errors,
    generic_update_errors,
)
from print_nanny_webapp.events.api.serializers import (
    EmailAlertSettingsSerializer,
    PrintJobAlertSerializer,
)

Pi = apps.get_model("devices", "Pi")

logger = logging.getLogger(__name__)


@extend_schema_view(
    retrieve=extend_schema(
        tags=["settings", "alerts"],
        responses={200: EmailAlertSettingsSerializer(many=False)} | generic_get_errors,
    ),
    list=extend_schema(
        tags=["settings", "alerts"],
        responses={
            200: EmailAlertSettingsSerializer(many=True),
        }
        | generic_list_errors,
    ),
    update=extend_schema(
        tags=["settings", "alerts"],
        request=EmailAlertSettingsSerializer,
        responses={
            202: EmailAlertSettingsSerializer,
        }
        | generic_update_errors,
    ),
    partial_update=extend_schema(
        tags=["settings", "alerts"],
        request=EmailAlertSettingsSerializer,
        responses={
            202: EmailAlertSettingsSerializer,
        }
        | generic_update_errors,
    ),
    create=extend_schema(
        tags=["settings", "alerts"],
        request=EmailAlertSettingsSerializer,
        responses={201: EmailAlertSettingsSerializer} | generic_create_errors,
    ),
)
class EmailAlertSettingsViewSet(
    GenericViewSet,
    ListModelMixin,
    RetrieveModelMixin,
    CreateModelMixin,
    UpdateModelMixin,
):
    serializer_class = EmailAlertSettingsSerializer
    queryset = EmailAlertSettings.objects.all()
    lookup_field = "id"

    def get_object(self):
        return self.get_queryset()

    # get email alert settings for user
    def get_queryset(self, *args, **kwargs):
        result = self.queryset.filter(user_id=self.request.user.id).first()
        # if result is empty, initialize model
        if result is None and self.request.user.is_authenticated:
            EmailAlertSettings.objects.create(user=self.request.user)
        return self.queryset.filter(user_id=self.request.user.id)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


@extend_schema_view(
    retrieve=extend_schema(
        tags=["alerts"],
        responses={200: PrintJobAlertSerializer(many=False)} | generic_get_errors,
    ),
    list=extend_schema(
        tags=["alerts"],
        responses={
            200: PrintJobAlertSerializer(many=True),
        }
        | generic_list_errors,
    ),
    update=extend_schema(
        tags=["alerts"],
        request=PrintJobAlertSerializer,
        responses={
            202: PrintJobAlertSerializer,
        }
        | generic_update_errors,
    ),
    partial_update=extend_schema(
        tags=["alerts"],
        request=PrintJobAlertSerializer,
        responses={
            202: PrintJobAlertSerializer,
        }
        | generic_update_errors,
    ),
    create=extend_schema(
        tags=["alerts"],
        request=PrintJobAlertSerializer,
        responses={201: PrintJobAlertSerializer} | generic_create_errors,
    ),
)
class PrintJobAlertViewSet(
    GenericViewSet,
    ListModelMixin,
    RetrieveModelMixin,
    CreateModelMixin,
    UpdateModelMixin,
):
    serializer_class = PrintJobAlertSerializer
    queryset = PrintJobAlert.objects.all()
    lookup_field = "id"

    def get_queryset(self, *args, **kwargs):
        result = self.queryset.filter(user_id=self.request.user.id)
        return result

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
