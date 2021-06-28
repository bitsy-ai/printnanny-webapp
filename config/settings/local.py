from .base import *  # noqa
from .base import env
# GENERAL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = True
# https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="dsgQKRAGB8mqGmMfYYq6wkqJtvulQz0PnqkRXfuIXZL7THCK5zGlp1xC5gyxksvj",
)
# https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1", "9c99269ffb46.ngrok.io", "desktop.lan", "django", "aurora.local", "aurora"]
# CACHES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "",
    }
}

# WhiteNoise
# ------------------------------------------------------------------------------
# http://whitenoise.evans.io/en/latest/django.html#using-whitenoise-in-development
INSTALLED_APPS = ["whitenoise.runserver_nostatic"] + INSTALLED_APPS  # noqa F405
WHITENOISE_AUTOREFRESH = True

# django-debug-toolbar
# ------------------------------------------------------------------------------
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#prerequisites
INSTALLED_APPS += ["debug_toolbar"]  # noqa F405
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#middleware
MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]  # noqa F405
# https://django-debug-toolbar.readthedocs.io/en/latest/configuration.html#debug-toolbar-config
DEBUG_TOOLBAR_CONFIG = {
    "DISABLE_PANELS": ["debug_toolbar.panels.redirects.RedirectsPanel"],
    "SHOW_TEMPLATE_CONTEXT": True,
}
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#internal-ips
INTERNAL_IPS = ["127.0.0.1", "10.0.2.2"]
if env("USE_DOCKER", default=False) == "yes":
    import socket

    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS += [".".join(ip.split(".")[:-1] + ["1"]) for ip in ips]

# django-extensions
# ------------------------------------------------------------------------------
# https://django-extensions.readthedocs.io/en/latest/installation_instructions.html#configuration
INSTALLED_APPS += ["django_extensions"]  # noqa F405
# Celery
# ------------------------------------------------------------------------------

# Your stuff...
# ------------------------------------------------------------------------------

GOOGLE_ANALYTICS=""

# django-prometheus middleware must be last in middleware stack
MIDDLEWARE += ['django_prometheus.middleware.PrometheusAfterMiddleware']
# django channels
WS_BASE_URL = env('PRINT_NANNY_WS_URL', default='ws://localhost:8000/ws')
BASE_URL = env('PRINT_NANNY_BASE_URL', default='http://localhost:8000/')
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [env("CELERY_BROKER_URL")],
            "group_expiry": 1800,
            # "channel_capacity": {
            #     "http.request": 100,
            #     "http.response!*": 100,
            #     re.compile(r"^websocket.send\!.+"): 10,
            # }
        },
    },
}

BETA_NOTIFY_EMAIL = ["leigh+testing@bitsy.ai"]

# CORS
# ------------------------------------------------------------------------------
CORS_ORIGIN_WHITELIST = [
    'http://localhost:8000'
]

# LOGGING
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#logging
# See https://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s "
            "%(process)d %(thread)d %(message)s"
        }
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        }
    },
    "root": {"level": "INFO", "handlers": ["console"]},
    "loggers": {
        "django.channels.worker": {"level": "DEBUG", "handlers": ["console"]},
        "django.channels.server": {"level": "DEBUG", "handlers": ["console"]},
        "uvicorn": {"handlers": ["console"], "level": "DEBUG"},
    }

}
