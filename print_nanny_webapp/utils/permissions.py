from rest_framework import permissions


class IsAdminOrIsSelf(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user or request.user.is_superuser


class IsObjectOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class IsPrivateAllowed(permissions.BasePermission):
    """
    Allow access to request owner
    """

    def has_permission(self, request, view):
        return view.kwargs.get("id", "") == request.user.id
