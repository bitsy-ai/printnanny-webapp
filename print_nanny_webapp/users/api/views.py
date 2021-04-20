from print_nanny_webapp.users.authentication import GeeksTokenAuthentication
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import action, api_view, authentication_classes
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ViewSet
from drf_spectacular.utils import extend_schema, extend_schema_view

# from drf_yasg.utils import swagger_auto_schema
# from drf_yasg import openapi

from .serializers import UserSerializer


User = get_user_model()


@extend_schema(
    tags=["users"],
    responses={200: UserSerializer, 201: UserSerializer, 202: UserSerializer},
)
class UserViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
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

@api_view(['GET'])
@authentication_classes([GeeksTokenAuthentication])
def geeks_token_validation_view_set(request):
    return Response({
        "printer_name": request.auth.octoprint_device.name,
        "is_valid": True,
    })
