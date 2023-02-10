import logging

from drfpasswordless.views import (
    ObtainAuthTokenFromCallbackToken,
)
from django.contrib.auth import login
from django.utils.module_loading import import_string
from drfpasswordless.settings import api_settings
from rest_framework.response import Response
from rest_framework import status

logger = logging.getLogger(__name__)


class ObtainAuthTokenAndSessionCookieFromCallbackToken(
    ObtainAuthTokenFromCallbackToken
):
    """
    Persist a user id and a backend in the request. This way a user doesn't
    have to reauthenticate on every request. Note that data set during
    the anonymous session is retained when the user logs in.
    """

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data["user"]
            token_creator = import_string(api_settings.PASSWORDLESS_AUTH_TOKEN_CREATOR)
            (token, _) = token_creator(user)

            if token:
                TokenSerializer = import_string(
                    api_settings.PASSWORDLESS_AUTH_TOKEN_SERIALIZER
                )
                token_serializer = TokenSerializer(data=token.__dict__, partial=True)
                if token_serializer.is_valid():
                    login(
                        request,
                        user,
                        backend="print_nanny_webapp.drfpasswordless.backends.PasswordlessBackend",
                    )
                    return Response(token_serializer.data, status=status.HTTP_200_OK)
        else:
            logger.error(
                "Couldn't log in unknown user. Errors on serializer: {}".format(
                    serializer.error_messages
                )
            )
        return Response(
            {"detail": "Couldn't log you in. Try again later."},
            status=status.HTTP_400_BAD_REQUEST,
        )
