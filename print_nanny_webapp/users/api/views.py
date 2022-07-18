from rest_framework.mixins import (
    CreateModelMixin,
)
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import AllowAny
from drf_spectacular.utils import extend_schema_view, extend_schema

from .serializers import EmailWaitlistSerializer
from ..models import EmailWaitlist


@extend_schema_view(create=extend_schema(tags=["accounts"]))
class EmailWaitlistViewSet(GenericViewSet, CreateModelMixin):
    """
    A device (Raspberry Pi) running Print Nanny OS
    """

    serializer_class = EmailWaitlistSerializer
    queryset = EmailWaitlist.objects.all()
    lookup_field = "id"
    permission_classes = (AllowAny,)
