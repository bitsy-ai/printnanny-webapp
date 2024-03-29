from config.settings.base import *  # noqa
from config.settings.base import env
import posthog

# GENERAL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = True
DJANGO_VITE_DEV_MODE = DEBUG
FLAGS_STATE_LOGGING = True
DEBUG_TOOLBAR_PANELS = [
    "flags.panels.FlagsPanel",
    "flags.panels.FlagChecksPanel",
    "debug_toolbar.panels.history.HistoryPanel",
    "debug_toolbar.panels.versions.VersionsPanel",
    "debug_toolbar.panels.timer.TimerPanel",
    "debug_toolbar.panels.settings.SettingsPanel",
    "debug_toolbar.panels.headers.HeadersPanel",
    "debug_toolbar.panels.request.RequestPanel",
    "debug_toolbar.panels.sql.SQLPanel",
    "debug_toolbar.panels.staticfiles.StaticFilesPanel",
    "debug_toolbar.panels.templates.TemplatesPanel",
    "debug_toolbar.panels.cache.CachePanel",
    "debug_toolbar.panels.signals.SignalsPanel",
    "debug_toolbar.panels.redirects.RedirectsPanel",
    "debug_toolbar.panels.profiling.ProfilingPanel",
]

# https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="dsgQKRAGB8mqGmMfYYq6wkqJtvulQz0PnqkRXfuIXZL7THCK5zGlp1xC5gyxksvj",
)
# https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = [
    "localhost",
    "0.0.0.0",
    "127.0.0.1",
    "9c99269ffb46.ngrok.io",
    "desktop.lan",
    "django",
    "aurora.local",
    "aurora",
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


def custom_show_toolbar(request):
    return True  # Always show toolbar


DEBUG_TOOLBAR_CONFIG = {
    # "DISABLE_PANELS": ["debug_toolbar.panels.redirects.RedirectsPanel"],
    "SHOW_TEMPLATE_CONTEXT": True,
    "SHOW_TOOLBAR_CALLBACK": custom_show_toolbar,
    "SHOW_COLLAPSED": True,
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

# Your stuff...
# ------------------------------------------------------------------------------

GOOGLE_ANALYTICS = ""

# django-prometheus middleware must be last in middleware stack
MIDDLEWARE += ["django_prometheus.middleware.PrometheusAfterMiddleware"]
# django channels
WS_BASE_URL = env("DJANGO_WS_URL", default="ws")
BASE_URL = env("DJANGO_BASE_URL", default="/")
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [env("REDIS_URL")],
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
    "http://localhost:8080",
    "http://localhost:3000",
    "http://localhost:5173",
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
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        }
    },
    "root": {"level": "INFO", "handlers": ["console"]},
    "loggers": {
        "django.channels.worker": {"level": "INFO", "handlers": ["console"]},
        "django.channels.server": {"level": "INFO", "handlers": ["console"]},
        "uvicorn": {"handlers": ["console"], "level": "INFO"},
    },
}

# CORS
# see also: corsheaders.middleware.CorsMiddleware
# ------------------------------------------------------------------------------
CORS_ALLOW_ALL_ORIGINS = True

DEV_SERVER_HOSTNAME = "aurora"

ANYMAIL_DEBUG_API_REQUESTS = True


# posthog
# ------------------------------------------------------------------------------
posthog.debug = True


# Celery
# ------------------------------------------------------------------------------
CELERY_TASK_ALWAYS_EAGER = True
CELERY_TASK_EAGER_PROPAGATES = True
