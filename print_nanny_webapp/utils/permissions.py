from rest_framework import permissions


class IsPrivateAllowed(permissions.BasePermission):
    """
    Allow access to request owner
    """
    def has_permission(self, request, view):
        return view.kwargs.get('id', '') == request.user.id