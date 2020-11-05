from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ViewSet
from drf_yasg.utils import swagger_auto_schema

from .serializers import UserSerializer


User = get_user_model()


class UserViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = "id"

    def get_queryset(self, *args, **kwargs):
        return self.queryset.filter(id=self.request.user.id)

class MeViewSet(GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    name = "me"

    @swagger_auto_schema(operation_id='get_me', operation_description="GET /me/")
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset()).first()
        serializer = self.get_serializer(queryset)
        return Response(serializer.data)

    def get_queryset(self, *args, **kwargs):
        return self.queryset.filter(id=self.request.user.id)

