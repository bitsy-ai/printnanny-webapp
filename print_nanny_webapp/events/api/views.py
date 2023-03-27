import logging
from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiParameter
from django.apps import apps


from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
    CreateModelMixin,
    UpdateModelMixin,
)
from rest_framework.permissions import IsAuthenticated
from print_nanny_webapp.events.models import BasePiEvent
from print_nanny_webapp.events.models.alerts import EmailAlertSettings
from print_nanny_webapp.events.models.pi import (
    PiBootCommand,
    PiBootStatus,
    PiCamCommand,
    PiCamStatus,
    PiSoftwareUpdateCommand,
    PiSoftwareUpdateStatus,
)
from print_nanny_webapp.events.services import nats_publish
from print_nanny_webapp.utils.api.views import (
    generic_get_errors,
    generic_create_errors,
    generic_list_errors,
    generic_update_errors,
)
from print_nanny_webapp.events.api.serializers import (
    PolymorphicPiEventSerializer,
    PolymorphicPiCommandSerializer,
    PolymorphicPiStatusSerializer,
    EmailAlertSettingsSerializer,
)

Pi = apps.get_model("devices", "Pi")

logger = logging.getLogger(__name__)


@extend_schema_view(
    retrieve=extend_schema(
        tags=["settings", "alerts"],
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

    # get email alert settings for user
    def get_queryset(self, *args, **kwargs):
        result = self.queryset.filter(user_id=self.request.user.id).first()
        # if result is empty, initialize model
        if result is None and self.request.user.is_authenticated:
            EmailAlertSettings.objects.create(user=self.request.user)
        return self.queryset.filter(user_id=self.request.user.id)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
