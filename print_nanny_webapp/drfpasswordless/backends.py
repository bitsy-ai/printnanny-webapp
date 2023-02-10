from django.utils.module_loading import import_string
from drfpasswordless.settings import api_settings
from django.contrib.auth import get_user_model
from django.core.exceptions import SuspiciousOperation

UserModel = get_user_model()


class PasswordlessBackend:
    """
    Authentication backend used with passwordless 2fa
    """

    def authenticate(self, request=None, user=None, **credentials):
        if user is None:
            return
        return user

    def get_user(self, user_id):
        try:
            return UserModel.objects.get(id=user_id)
        except UserModel.DoesNotExist:
            return None
