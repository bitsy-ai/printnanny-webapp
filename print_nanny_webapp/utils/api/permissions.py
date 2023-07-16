from rest_framework import permissions
from django.conf import settings


class IsAdminOrIsSelf(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user or request.user.is_superuser


class IsObjectOwnerOrSharedWorkspace(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # requets.user is an admin of shared workspace
        if getattr(obj, "workspace", None):
            if obj.workspace is not None:
                return obj.workspace.is_admin(request.user)
        # is object owner
        if getattr(obj, "user", None):
            return obj.user == request.user
        if getattr(obj, "owner", None):
            return obj.owner == request.user
        return False


class HasActiveSubscription(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_beta_tester
            or request.user.groups.filter(name=settings.DEMO_GROUP).exists()
        )

    def has_object_permission(self, request, view, obj):
        return (
            request.user.is_beta_tester
            or request.user.groups.filter(name=settings.DEMO_GROUP).exists()
        )
