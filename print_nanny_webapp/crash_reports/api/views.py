import logging

from drf_spectacular.utils import extend_schema_view, extend_schema

from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (
    CreateModelMixin,
)
from rest_framework import parsers

from print_nanny_webapp.crash_reports.models import CrashReport
from print_nanny_webapp.crash_reports.api.serializers import CrashReportSerializer
from print_nanny_webapp.utils.api.views import (
    generic_create_errors,
)

logger = logging.getLogger(__name__)


@extend_schema_view(
    create=extend_schema(
        tags=["crash-reports"],
        request=CrashReportSerializer,
        responses={201: CrashReportSerializer} | generic_create_errors,
    )
)
class CrashReportViewSet(
    GenericViewSet,
    CreateModelMixin,
):
    serializer_class = CrashReportSerializer
    queryset = CrashReport.objects.all()
    lookup_field = "id"

    parser_classes = [
        parsers.FormParser,
        parsers.MultiPartParser,
    ]
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        logger.info(
            "CrashReport.create called with request=%s asgi.request=%s",
            request.__dict__,
            request._request.__dict__,
        )
        return super().create(request, *args, **kwargs)
