# https://drf-spectacular.readthedocs.io/en/latest/blueprints.html

from drfpasswordless.serializers import (
    EmailAuthSerializer,
    MobileAuthSerializer,
    CallbackTokenAuthSerializer,
    EmailVerificationSerializer,
    MobileVerificationSerializer,
    CallbackTokenVerificationSerializer,
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
                tags=[api_settings.PASSWORDLESS_AUTH_PREFIX],
            )
            def post(self, request, *args, **kwargs):
                pass

        return Fixed


# /auth/mobile/
class FixObtainMobileCallbackToken(OpenApiViewExtension):
    target_class = "drfpasswordless.views.ObtainMobileCallbackToken"

    def view_replacement(self):
        class Fixed(self.target_class):
            serializer_class = MobileAuthSerializer

            @extend_schema(
                request=MobileAuthSerializer,
                responses=DetailResponseSerializer,
                tags=[api_settings.PASSWORDLESS_AUTH_PREFIX],
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
                tags=[api_settings.PASSWORDLESS_AUTH_PREFIX],
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
                tags=[api_settings.PASSWORDLESS_AUTH_PREFIX],
            )
            def post(self, request, *args, **kwargs):
                pass

        return Fixed


# /auth/verify/mobile
# automatically sends a token attached to request.user email or mobile if available
# (unused but wrapped for posterity)
class FixObtainMobileVerificationCallbackToken(OpenApiViewExtension):
    target_class = "drfpasswordless.views.ObtainMobileVerificationCallbackToken"

    def view_replacement(self):
        class Fixed(self.target_class):
            serializer_class = MobileVerificationSerializer

            @extend_schema(
                request=MobileVerificationSerializer,
                responses=DetailResponseSerializer,
                tags=[api_settings.PASSWORDLESS_AUTH_PREFIX],
            )
            def post(self, request, *args, **kwargs):
                pass

        return Fixed


# /auth/verify/
# double-check that the endpoint belongs to the request.user and mark the alias as verified
class FixObtainMobileVerificationCallbackToken(OpenApiViewExtension):
    target_class = "drfpasswordless.views.ObtainMobileVerificationCallbackToken"

    def view_replacement(self):
        class Fixed(self.target_class):
            serializer_class = CallbackTokenVerificationSerializer

            @extend_schema(
                request=CallbackTokenVerificationSerializer,
                responses=DetailResponseSerializer,
                tags=[api_settings.PASSWORDLESS_AUTH_PREFIX],
            )
            def post(self, request, *args, **kwargs):
                pass

        return Fixed
