"""
With these settings, tests run faster.
"""
import django_stubs_ext

django_stubs_ext.monkeypatch()
from config.settings.base import *  # noqa
from config.settings.base import env


# GENERAL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
DEBUG = True
DJANGO_VITE_DEV_MODE = DEBUG
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="nF2tDTEGAdjzk2DNx9pfikPNgyiPILVSRJ7Ek9tRoYhvTapZUlq8d4f03sxLg5pP",
)
# https://docs.djangoproject.com/en/dev/ref/settings/#test-runner
TEST_RUNNER = "django.test.runner.DiscoverRunner"

# https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    "0.0.0.0",
]

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

# WhiteNoise
# ------------------------------------------------------------------------------
# http://whitenoise.evans.io/en/latest/django.html#using-whitenoise-in-development
INSTALLED_APPS = ["whitenoise.runserver_nostatic"] + INSTALLED_APPS  # noqa F405
WHITENOISE_AUTOREFRESH = True

# CORS
# ------------------------------------------------------------------------------
CORS_ALLOW_ALL_ORIGINS = True

# EMAIL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"

# Your stuff...
# ------------------------------------------------------------------------------
ADMINS = []

BETA_NOTIFY_EMAIL = "test@print-nanny.com"
WS_BASE_URL = env("DJANGO_WS_URL", default="ws://localhost:8080/ws")
BASE_URL = env("DJANGO_BASE_URL", default="http://localhost:8080/")


WHITENOISE_MANIFEST_STRICT = False
GOOGLE_ANALYTICS = ""

# Django Channels
# ------------------------------------------------------------------------------
WS_BASE_URL = env("DJANGO_WS_URL", default="ws")
BASE_URL = env("DJANGO_BASE_URL", default="/")
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [env("REDIS_URL")],
            "group_expiry": 1800,
        },
    },
}
DISCORD_NEW_SIGNUP_WEBHOOK = None


# posthog
# ------------------------------------------------------------------------------
posthog.disabled = True
