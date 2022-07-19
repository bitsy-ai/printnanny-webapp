# https://drf-spectacular.readthedocs.io/en/latest/blueprints.html

from drfpasswordless.serializers import (
    EmailAuthSerializer,
    CallbackTokenAuthSerializer,
    EmailVerificationSerializer,
)
from django.utils.module_loading import import_string
from rest_framework import serializers
from drf_spectacular.extensions import OpenApiViewExtension
from drf_spectacular.utils import extend_schema
from drfpasswordless.settings import api_settings


class DetailResponseSerializer(serializers.Serializer):
    """
    Generic auth response serializer
    """

    detail = serializers.CharField()


# /auth/email/
class FixObtainEmailCallbackToken(OpenApiViewExtension):
    target_class = "drfpasswordless.views.ObtainEmailCallbackToken"

    def view_replacement(self):
        class Fixed(self.target_class):
            serializer_class = EmailAuthSerializer

            @extend_schema(
                request=EmailAuthSerializer,
                responses=DetailResponseSerializer,
                tags=["accounts"],
            )
            def post(self, request, *args, **kwargs):
                pass

        return Fixed


TokenResponseSerializer = import_string(api_settings.PASSWORDLESS_AUTH_TOKEN_SERIALIZER)
# /auth/token/
class FixObtainAuthTokenFromCallbackToken(OpenApiViewExtension):
    target_class = "drfpasswordless.views.ObtainAuthTokenFromCallbackToken"

    def view_replacement(self):
        class Fixed(self.target_class):
            serializer_class = CallbackTokenAuthSerializer

            @extend_schema(
                request=CallbackTokenAuthSerializer,
                responses=TokenResponseSerializer,
                tags=["accounts"],
            )
            def post(self, request, *args, **kwargs):
                pass

        return Fixed


# /auth/verify/email
# automatically sends a token attached to request.user email or mobile if available
# (unused but wrapped for posterity)
class FixObtainEmailVerificationCallbackToken(OpenApiViewExtension):
    target_class = "drfpasswordless.views.ObtainEmailVerificationCallbackToken"

    def view_replacement(self):
        class Fixed(self.target_class):
            serializer_class = EmailVerificationSerializer

            @extend_schema(
                request=EmailVerificationSerializer,
                responses=DetailResponseSerializer,
                tags=["accounts"],
            )
            def post(self, request, *args, **kwargs):
                pass

        return Fixed
