"""
With these settings, tests run faster.
"""
import django_stubs_ext

django_stubs_ext.monkeypatch()
from .base import *  # noqa
from .base import env


# GENERAL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="nF2tDTEGAdjzk2DNx9pfikPNgyiPILVSRJ7Ek9tRoYhvTapZUlq8d4f03sxLg5pP",
)
# https://docs.djangoproject.com/en/dev/ref/settings/#test-runner
TEST_RUNNER = "django.test.runner.DiscoverRunner"

# CACHES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "",
    }
}

# PASSWORDS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#password-hashers
PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]

# TEMPLATES
# ------------------------------------------------------------------------------
TEMPLATES[-1]["OPTIONS"]["loaders"] = [  # type: ignore[index] # noqa F405
    (
        "django.template.loaders.cached.Loader",
        [
            "django.template.loaders.filesystem.Loader",
            "django.template.loaders.app_directories.Loader",
        ],
    )
]

# EMAIL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"

# Your stuff...
# ------------------------------------------------------------------------------
BETA_NOTIFY_EMAIL = "test@print-nanny.com"
GHOST_ADMIN_API_KEY = ""
WS_BASE_URL = env("PRINT_NANNY_WS_URL", default="ws://localhost:8000/ws")
BASE_URL = env("DJANGO_BASE_URL", default="http://localhost:8000/")


WHITENOISE_MANIFEST_STRICT = False
GOOGLE_ANALYTICS = ""
