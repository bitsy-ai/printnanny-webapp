from rest_framework.mixins import (
    ListModelMixin,
)
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response

from drf_spectacular.utils import extend_schema_view, extend_schema

from print_nanny_webapp.achievements.services import check_achievements
from print_nanny_webapp.achievements.models import Achievement
from print_nanny_webapp.achievements.api.serializers import AchievementSerializer


@extend_schema_view(
    list=extend_schema(
        tags=["achievements"],
        responses={
            200: AchievementSerializer(many=True),
        },
    ),
)
class AchievementViewSet(
    GenericViewSet,
    ListModelMixin,
):

    serializer_class = AchievementSerializer
    queryset = Achievement.objects.all()
    lookup_field = "id"

    def list(self, request, *args, **kwargs):
        check_achievements(request.user)

        queryset = Achievement.objects.filter(user=request.user)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
