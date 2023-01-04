from rest_framework import permissions
from django.conf import settings


class IsAdminOrIsSelf(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user or request.user.is_superuser


class IsObjectOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


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
