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
from drfpasswordless.views import (
    ObtainEmailCallbackToken,
    ObtainMobileCallbackToken,
    ObtainMobileCallbackToken,
    ObtainAuthTokenFromCallbackToken,
    ObtainEmailVerificationCallbackToken,
    ObtainMobileVerificationCallbackToken,
    ObtainMobileVerificationCallbackToken,
)


class DetailResponseSerializer(serializers.Serializer):
    """
    Generic auth response serializer
    """

    detail = serializers.CharField()

    def create(self):
        pass


# /auth/email/
class FixObtainEmailCallbackToken(OpenApiViewExtension):
    def view_replacement(self):
        class Fixed(ObtainEmailCallbackToken):
            serializer_class = EmailAuthSerializer

            @extend_schema(
                request=EmailAuthSerializer,
                responses=DetailResponseSerializer,
                tags=[api_settings.PASSWORDLESS_AUTH_PREFIX.replace("/", "")],
            )
            def post(self, request, *args, **kwargs):
                pass

        return Fixed


# /auth/mobile/
class FixObtainMobileCallbackToken(OpenApiViewExtension):
    def view_replacement(self):
        class Fixed(ObtainMobileCallbackToken):
            serializer_class = MobileAuthSerializer

            @extend_schema(
                request=MobileAuthSerializer,
                responses=DetailResponseSerializer,
                tags=[api_settings.PASSWORDLESS_AUTH_PREFIX.replace("/", "")],
            )
            def post(self, request, *args, **kwargs):
                pass

        return Fixed


TokenResponseSerializer = import_string(api_settings.PASSWORDLESS_AUTH_TOKEN_SERIALIZER)
# /auth/token/


class FixObtainAuthTokenFromCallbackToken(OpenApiViewExtension):
    def view_replacement(self):
        class Fixed(ObtainAuthTokenFromCallbackToken):
            serializer_class = CallbackTokenAuthSerializer

            @extend_schema(
                request=CallbackTokenAuthSerializer,
                responses=TokenResponseSerializer,
                tags=[api_settings.PASSWORDLESS_AUTH_PREFIX.replace("/", "")],
            )
            def post(self, request, *args, **kwargs):
                pass

        return Fixed


# /auth/verify/email
# automatically sends a token attached to request.user email or mobile if available
# (unused but wrapped for posterity)
class FixObtainEmailVerificationCallbackToken(OpenApiViewExtension):
    def view_replacement(self):
        class Fixed(ObtainEmailVerificationCallbackToken):
            serializer_class = EmailVerificationSerializer

            @extend_schema(
                request=EmailVerificationSerializer,
                responses=DetailResponseSerializer,
                tags=[api_settings.PASSWORDLESS_AUTH_PREFIX.replace("/", "")],
            )
            def post(self, request, *args, **kwargs):
                pass

        return Fixed


# /auth/verify/mobile
# automatically sends a token attached to request.user email or mobile if available
# (unused but wrapped for posterity)
class FixObtainMobileVerificationCallbackToken(OpenApiViewExtension):
    def view_replacement(self):
        class Fixed(ObtainMobileVerificationCallbackToken):
            serializer_class = MobileVerificationSerializer

            @extend_schema(
                request=MobileVerificationSerializer,
                responses=DetailResponseSerializer,
                tags=[api_settings.PASSWORDLESS_AUTH_PREFIX.replace("/", "")],
            )
            def post(self, request, *args, **kwargs):
                pass

        return Fixed


# /auth/verify/
# double-check that the endpoint belongs to the request.user and mark the alias as verified
class FixCallbackTokenVerificationToken(OpenApiViewExtension):
    def view_replacement(self):
        class Fixed(ObtainMobileVerificationCallbackToken):
            serializer_class = CallbackTokenVerificationSerializer

            @extend_schema(
                request=CallbackTokenVerificationSerializer,
                responses=DetailResponseSerializer,
                tags=[api_settings.PASSWORDLESS_AUTH_PREFIX.replace("/", "")],
            )
            def post(self, request, *args, **kwargs):
                pass

        return Fixed
