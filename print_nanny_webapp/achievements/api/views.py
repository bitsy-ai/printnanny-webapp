from rest_framework.mixins import (
    ListModelMixin,
    CreateModelMixin,
)
from rest_framework.viewsets import GenericViewSet
from drf_spectacular.utils import extend_schema_view, extend_schema

from print_nanny_webapp.achievements.models import Achievement
from print_nanny_webapp.achievements.api.serializers import AchievementSerializer


@extend_schema_view(
    list=extend_schema(
        tags=["achievements"],
        responses={
            200: AchievementSerializer(many=True),
        },
    ),
    create=extend_schema(
        tags=["achievements"],
        request=AchievementSerializer,
        responses={
            201: AchievementSerializer,
        },
    ),
)
class AchievementViewSet(
    GenericViewSet,
    CreateModelMixin,
    ListModelMixin,
):

    serializer_class = AchievementSerializer
    queryset = Achievement.objects.all()
    lookup_field = "id"
