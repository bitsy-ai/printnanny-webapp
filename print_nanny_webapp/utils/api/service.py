from typing import TypedDict, Optional
import logging
import urllib.parse

from django.contrib.auth import get_user_model
from django.conf import settings
from django.urls import reverse

from rest_framework.authtoken.models import Token

User = get_user_model()

logger = logging.getLogger(__name__)


class PrintNannyApiConfig(TypedDict):
    bearer_access_token: Optional[str]
    base_path: str


def get_api_config(request, user=None) -> PrintNannyApiConfig:
    if user is None:
        if request.user.is_anonymous:
            token = None
        else:
            tokenobj, _ = Token.objects.get_or_create(user=request.user)
            token = str(tokenobj)
    else:
        tokenobj, _ = Token.objects.get_or_create(user=user)
        token = str(tokenobj)
    base_path = request.build_absolute_uri("/")[
        :-1
    ]  # remove trailing slash for use in API client base_url
    config = PrintNannyApiConfig(
        bearer_access_token=token,
        base_path=base_path,
    )
    logger.debug(
        "Created request.user.is_anonymous=%s config=%s",
        request.user.is_anonymous,
        config,
    )
    return config
