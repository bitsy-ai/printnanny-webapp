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
from print_nanny_webapp.utils.api.views import (
    generic_create_errors,
    generic_list_errors,
    generic_get_errors,
    generic_update_errors,
)
from print_nanny_webapp.utils.permissions import IsObjectOwner
from .serializers import PolymorphicPiEventSerializer, EmailAlertSettingsSerializer

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
    permission_classes = [IsObjectOwner, IsAuthenticated]
    serializer_class = EmailAlertSettingsSerializer
    queryset = EmailAlertSettings.objects.all()
    lookup_field = "id"

    # get email alert settings for user
    def get_queryset(self, *args, **kwargs):
        result = self.queryset.filter(user_id=self.request.user.id).first()
        # if result is empty, initialize model
        if result is None:
            EmailAlertSettings.objects.create(user=self.request.user)
        return self.queryset.filter(user_id=self.request.user.id)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


@extend_schema_view(
    list=extend_schema(
        tags=["pis", "events"],
        responses={
            200: PolymorphicPiEventSerializer(many=True),
        }
        | generic_list_errors,
    ),
    create=extend_schema(
        tags=["pis", "events"],
        request=PolymorphicPiEventSerializer,
        responses={
            201: PolymorphicPiEventSerializer,
        }
        | generic_create_errors,
    ),
    retrieve=extend_schema(
        tags=["pis", "events"],
        request=PolymorphicPiEventSerializer,
        responses={
            200: PolymorphicPiEventSerializer,
        }
        | generic_get_errors,
    ),
)
class AllPiEventsViewSet(
    GenericViewSet,
    ListModelMixin,
    RetrieveModelMixin,
    CreateModelMixin,
):
    """
    Interact with all events inheriting from BasePiEvent
    """

    permission_classes = [IsObjectOwner, IsAuthenticated]
    serializer_class = PolymorphicPiEventSerializer
    queryset = BasePiEvent.objects.all()
    lookup_field = "id"

    # get events related to all pis owned by authenticated user
    def get_queryset(self, *args, **kwargs):
        return self.queryset.filter(user_id=self.request.user.id)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


@extend_schema_view(
    list=extend_schema(
        tags=["pis", "events"],
        parameters=[
            OpenApiParameter(name="pi_id", type=int, location=OpenApiParameter.PATH)
        ],
        responses={
            200: PolymorphicPiEventSerializer(many=True),
        }
        | generic_list_errors,
    ),
)
class SinglePiEventsViewSet(
    GenericViewSet,
    ListModelMixin,
):
    """
    Interact with all events inheriting from BasePiEvent
    """

    permission_classes = [IsObjectOwner, IsAuthenticated]
    serializer_class = PolymorphicPiEventSerializer
    queryset = BasePiEvent.objects.all()
    lookup_field = "id"

    # get events related to path parameter: pi_id
    def get_queryset(self, pi_id=None, *args, **kwargs):
        if pi_id is None:
            raise ValueError("pi_id is required")
        return self.queryset.filter(user_id=self.request.user.id, pi_id=pi_id)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
