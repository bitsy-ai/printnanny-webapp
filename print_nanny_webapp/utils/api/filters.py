from functools import reduce
from django.db.models import Q
from django_filters import rest_framework as filters
from drf_spectacular.contrib.django_filters import DjangoFilterExtension


class WorkspaceFilterBackend(filters.DjangoFilterBackend):
    def filter_queryset(self, request, queryset, view):
        if request.user.is_authenticated:
            # if there's a workspace field, filter by workspace membership
            if getattr(queryset.model, "workspace", None):
                return queryset.filter(workspace__users=request.user)
        return queryset


class OwnerOrUserFilterBackend(filters.DjangoFilterBackend):
    def filter_queryset(self, request, queryset, view):
        result = queryset
        if request.user.is_authenticated:
            queries = []

            # if there's a user field, filter by user
            if getattr(queryset.model, "user", None):
                queries.append(Q(user=request.user))

            # if there's an owner field, filter by owner
            if getattr(queryset.model, "owner", None):
                queries.append(Q(owner=request.user))

            filterset = reduce(lambda a, b: b if a is None else a | b, queries, None)

            return queryset.filter(filterset)
        return result


class PrintNannyFilterExtension(DjangoFilterExtension):
    """
    Because drf-spectacular does extension registration by exact classpath matches, since we use a custom subclass
    of django_filters.rest_framework.DjangoFilterBackend, we have to point drf-spectacular to our subclass since the
    parent class isn't directly in use and therefore doesn't get extended??
    """

    target_class = "print_nanny_webapp.utils.api.filters.OwnerOrUserFilterBackend"
