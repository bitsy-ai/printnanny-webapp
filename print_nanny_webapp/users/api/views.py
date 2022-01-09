from django.contrib.auth import get_user_model
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from drf_spectacular.utils import extend_schema, extend_schema_view

from print_nanny_webapp.utils.api.views import (
    generic_update_errors,
    generic_get_errors,
)
from .serializers import UserSerializer


User = get_user_model()


@extend_schema_view(
    update=extend_schema(
        request=UserSerializer,
        responses=generic_update_errors.merge(
            {
                201: UserSerializer,
            }
        ),
    ),
    retreive=extend_schema(
        request=UserSerializer,
        responses=generic_get_errors.merge(
            {
                200: UserSerializer,
            }
        ),
    ),
    me=extend_schema(
        request=UserSerializer,
        responses=generic_get_errors.merge(
            {
                200: UserSerializer,
            }
        ),
    ),
)
class UserViewSet(RetrieveModelMixin, UpdateModelMixin, GenericViewSet):

    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = "id"

    def get_queryset(self, *args, **kwargs):
        return self.queryset.filter(id=self.request.user.id)

    @action(detail=False, methods=["GET"])
    def me(self, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset()).first()
        serializer = self.get_serializer(queryset)
        return Response(serializer.data)
