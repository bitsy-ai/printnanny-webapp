from django_filters import rest_framework as filters


class OwnerOrUserFilterBackend(filters.DjangoFilterBackend):
    def filter_queryset(self, request, queryset, view):
        # TODO: set owner field on models
        # return queryset.filter(Q(owner=request.user) | Q(user=request.user))
        return queryset.filter(user=request.user)
