from typing import TypedDict, Optional

from django.http import HttpRequest
from rest_framework.authtoken.models import Token


class PrintNannyApiConfig(TypedDict):
    bearer_access_token: str
    base_path: str
    device_id: Optional[int]
    user_id: int
    user_email: str


def get_api_config(request: HttpRequest, device=None) -> PrintNannyApiConfig:
    if not request.user:
        raise Exception("APIConfig requires authenticated user to retreive")
    if not request.user.email:
        raise Exception("User.email is required")

    token, _ = Token.objects.get_or_create(user=request.user)

    device_id = device.id if device else None
    base_path = request.build_absolute_uri("/")[
        :-1
    ]  # remove trailing slash for use in API client base_url
    return PrintNannyApiConfig(
        bearer_access_token=str(token),
        base_path=base_path,
        device_id=device_id,
        user_id=request.user.id,
        user_email=request.user.email,
    )
