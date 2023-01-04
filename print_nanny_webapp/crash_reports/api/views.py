import logging

from drf_spectacular.utils import extend_schema_view, extend_schema

from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    CreateModelMixin,
    DestroyModelMixin,
)
from rest_framework import parsers

from print_nanny_webapp.utils.api.permissions import IsObjectOwner
from print_nanny_webapp.crash_reports.models import CrashReport
from print_nanny_webapp.crash_reports.api.serializers import CrashReportSerializer
from print_nanny_webapp.utils.api.views import (
    generic_create_errors,
    generic_list_errors,
    generic_update_errors,
)

logger = logging.getLogger(__name__)


@extend_schema_view(
    create=extend_schema(
        tags=["crash-reports"],
        request=CrashReportSerializer,
        responses={201: CrashReportSerializer} | generic_create_errors,
    ),
    list=extend_schema(
        tags=["crash-reports"],
        responses={
            200: CrashReportSerializer(many=True),
        }
        | generic_list_errors,
    ),
    update=extend_schema(
        tags=["crash-reports"],
        request=CrashReportSerializer,
        responses={
            202: CrashReportSerializer,
        }
        | generic_update_errors,
    ),
    partial_update=extend_schema(
        tags=["crash-reports"],
        request=CrashReportSerializer,
        responses={
            202: CrashReportSerializer,
        }
        | generic_update_errors,
    ),
)
class CrashReportViewSet(
    GenericViewSet,
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
):
    serializer_class = CrashReportSerializer
    queryset = CrashReport.objects.all()
    lookup_field = "id"

    parser_classes = [
        parsers.FormParser,
        parsers.MultiPartParser,
    ]
    # allow create from un-authenticated requests, but required authentication and object ownership for list/get
    def get_permissions(self):
        if self.action == "create":
            permission_classes = (AllowAny,)
        else:
            permission_classes = (
                IsAuthenticated,
                IsObjectOwner,
            )
        return [permission() for permission in permission_classes]
