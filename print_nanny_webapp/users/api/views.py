from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet 

from .serializers import UserSerializer

User = get_user_model()


class UserViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = "id"

    def get_queryset(self, *args, **kwargs):
        return self.queryset.filter(id=self.request.user.id)

    @action(detail=False, methods=["GET"])
    def me(self, request):
        serializer = UserSerializer(request.user, context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)


# class UserViewSet(viewsets.ModelViewSet):
#     """
#     A viewset for viewing and editing user instances.
#     """
#     serializer_class = UserSerializer
#     User = get_user_model()
#     queryset = User.objects.all()
#     filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter)
#     filter_fields = ('email',)
#     search_fields = ('email',)

#     @list_route(permission_classes=[IsAuthenticated])
#     def me(self, request, *args, **kwargs):
#         User = get_user_model()
#         self.object = get_object_or_404(User, pk=request.user.id)
#         serializer = self.get_serializer(self.object)
#         return Response(serializer.data)