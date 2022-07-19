# drfpasswordless exports all views by default
# this shim will only export views for auth methods in PASSWORDLESS_AUTH_TYPES
from drfpasswordless.settings import api_settings
from django.urls import path
from drfpasswordless.views import (
    ObtainEmailCallbackToken,
    ObtainMobileCallbackToken,
    ObtainAuthTokenFromCallbackToken,
    VerifyAliasFromCallbackToken,
    ObtainEmailVerificationCallbackToken,
    ObtainMobileVerificationCallbackToken,
)

app_name = "drfpasswordless"

# universal endpoints
urlpatterns = [
    path(
        api_settings.PASSWORDLESS_AUTH_PREFIX + "token/",
        ObtainAuthTokenFromCallbackToken.as_view(),
        name="auth_token",
    ),
    path(
        api_settings.PASSWORDLESS_VERIFY_PREFIX,
        VerifyAliasFromCallbackToken.as_view(),
        name="verify_token",
    ),
]

# PASSWORDLESS_AUTH_TYPES contains EMAIL
if "EMAIL" in api_settings.PASSWORDLESS_AUTH_TYPES:
    urlpatterns += [
        path(
            api_settings.PASSWORDLESS_AUTH_PREFIX + "email/",
            ObtainEmailCallbackToken.as_view(),
            name="auth_email",
        ),
        path(
            api_settings.PASSWORDLESS_VERIFY_PREFIX + "email/",
            ObtainEmailVerificationCallbackToken.as_view(),
            name="verify_email",
        ),
    ]

if "MOBILE" in api_settings.PASSWORDLESS_AUTH_TYPES:
    urlpatterns += [
        path(
            api_settings.PASSWORDLESS_AUTH_PREFIX + "mobile/",
            ObtainMobileCallbackToken.as_view(),
            name="auth_mobile",
        ),
        path(
            api_settings.PASSWORDLESS_VERIFY_PREFIX + "mobile/",
            ObtainMobileVerificationCallbackToken.as_view(),
            name="verify_mobile",
        ),
    ]
# PASSWORDLESS_AUTH_TYPES contains MOBILE
