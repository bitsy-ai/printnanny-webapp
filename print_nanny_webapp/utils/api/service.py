from typing import TypedDict, Optional

from django.contrib.auth.models import AnonymousUser
from django.contrib.auth import get_user_model

from rest_framework.authtoken.models import Token

User = get_user_model()


class PrintNannyApiConfig(TypedDict):
    bearer_access_token: str
    base_path: str
    device_id: Optional[int]
    user_id: int
    user_email: str


def get_api_config(request, device=None) -> PrintNannyApiConfig:
    if type(request.user) == AnonymousUser:
        raise Exception("APIConfig requires authenticated user to retreive")

    token, _ = Token.objects.get_or_create(user=request.user)
    user_email = str(request.user.email)

    device_id = int(device.id) if device else None
    user_id = int(request.user.id)
    base_path = request.build_absolute_uri("/")[
        :-1
    ]  # remove trailing slash for use in API client base_url
    return PrintNannyApiConfig(
        bearer_access_token=str(token),
        base_path=base_path,
        device_id=device_id,
        user_id=user_id,
        user_email=request.user.email,
    )
