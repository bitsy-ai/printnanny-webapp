import logging

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration
from sentry_sdk.integrations.logging import LoggingIntegration
from sentry_sdk.integrations.celery import CeleryIntegration


from .base import *  # noqa
from .base import env

# GENERAL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = env("DJANGO_SECRET_KEY")
# https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS", default=["print-nanny.com"])

# DATABASES
# ------------------------------------------------------------------------------
DATABASES["default"] = env.db("DATABASE_URL")  # noqa F405
DATABASES["default"]["ATOMIC_REQUESTS"] = True  # noqa F405
DATABASES["default"]["CONN_MAX_AGE"] = env.int("CONN_MAX_AGE", default=60)  # noqa F405

# CACHES
# ------------------------------------------------------------------------------
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": env("REDIS_URL"),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            # Mimicing memcache behavior.
            # https://github.com/jazzband/django-redis#memcached-exceptions-behavior
            "IGNORE_EXCEPTIONS": True,
        },
    }
}

# SECURITY
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#secure-proxy-ssl-header
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
# https://docs.djangoproject.com/en/dev/ref/settings/#secure-ssl-redirect
SECURE_SSL_REDIRECT = env.bool("DJANGO_SECURE_SSL_REDIRECT", default=True)
# https://docs.djangoproject.com/en/dev/ref/settings/#session-cookie-secure
SESSION_COOKIE_SECURE = True
# https://docs.djangoproject.com/en/dev/ref/settings/#csrf-cookie-secure
CSRF_COOKIE_SECURE = True
# https://docs.djangoproject.com/en/dev/topics/security/#ssl-https
# https://docs.djangoproject.com/en/dev/ref/settings/#secure-hsts-seconds
# TODO: set this to 60 seconds first and then to 518400 once you prove the former works
SECURE_HSTS_SECONDS = 60
# https://docs.djangoproject.com/en/dev/ref/settings/#secure-hsts-include-subdomains
SECURE_HSTS_INCLUDE_SUBDOMAINS = env.bool(
    "DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS", default=True
)
# https://docs.djangoproject.com/en/dev/ref/settings/#secure-hsts-preload
SECURE_HSTS_PRELOAD = env.bool("DJANGO_SECURE_HSTS_PRELOAD", default=True)
# https://docs.djangoproject.com/en/dev/ref/middleware/#x-content-type-options-nosniff
SECURE_CONTENT_TYPE_NOSNIFF = env.bool(
    "DJANGO_SECURE_CONTENT_TYPE_NOSNIFF", default=True
)

# STATIC
# ------------------------
# MEDIA
# ------------------------------------------------------------------------------
DEFAULT_FILE_STORAGE = "print_nanny_webapp.utils.storages.MediaRootGoogleCloudStorage"
MEDIA_URL = f"https://storage.googleapis.com/{GS_BUCKET_NAME}/webapp/media/"

# TEMPLATES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#templates
TEMPLATES[-1]["OPTIONS"]["loaders"] = [  # type: ignore[index] # noqa F405
    (
        "django.template.loaders.cached.Loader",
        [
            "django.template.loaders.filesystem.Loader",
            "django.template.loaders.app_directories.Loader",
        ],
    )
]

# ADMIN
# ------------------------------------------------------------------------------
# Django Admin URL regex.
ADMIN_URL = env("DJANGO_ADMIN_URL")

# django-compressor
# ------------------------------------------------------------------------------
# https://django-compressor.readthedocs.io/en/latest/settings/#django.conf.settings.COMPRESS_ENABLED
# COMPRESS_ENABLED = env.bool("COMPRESS_ENABLED", default=True)
# # https://django-compressor.readthedocs.io/en/latest/settings/#django.conf.settings.COMPRESS_URL
# COMPRESS_URL = STATIC_URL  # noqa F405
# # https://django-compressor.readthedocs.io/en/latest/settings/#django.conf.settings.COMPRESS_OFFLINE
# COMPRESS_OFFLINE = True  # Offline compression is required when using Whitenoise
# # https://django-compressor.readthedocs.io/en/latest/settings/#django.conf.settings.COMPRESS_FILTERS
# COMPRESS_FILTERS = {
#     "css": [
#         "compressor.filters.css_default.CssAbsoluteFilter",
#         "compressor.filters.cssmin.rCSSMinFilter",
#     ],
#     "js": ["compressor.filters.jsmin.JSMinFilter"],
# }

# LOGGING
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#logging
# See https://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.

LOGGING = {
    "version": 1,
    "disable_existing_loggers": True,
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
        "django.db.backends": {
            "level": "ERROR",
            "handlers": ["console"],
            "propagate": False,
        },
        # Errors logged by the SDK itself
        "sentry_sdk": {"level": "ERROR", "handlers": ["console"], "propagate": False},
        "django.security.DisallowedHost": {
            "level": "ERROR",
            "handlers": ["console"],
            "propagate": False,
        },
    },
}

# Sentry
# ------------------------------------------------------------------------------
SENTRY_DSN = env("SENTRY_DSN")
SENTRY_LOG_LEVEL = env.int("DJANGO_SENTRY_LOG_LEVEL", logging.INFO)

sentry_logging = LoggingIntegration(
    level=SENTRY_LOG_LEVEL,  # Capture info and above as breadcrumbs
    event_level=logging.ERROR,  # Send errors as events
)
integrations = [sentry_logging, DjangoIntegration(), CeleryIntegration()]
sentry_sdk.init(
    dsn=SENTRY_DSN,
    integrations=integrations,
    environment=env("SENTRY_ENVIRONMENT", default="production"),
    send_default_pii=True,
    #traces_sample_rate=env.float("SENTRY_TRACES_SAMPLE_RATE", default=0.0),
)

# Your stuff...
# ------------------------------------------------------------------------------


GOOGLE_ANALYTICS =  'G-QKHED5DPGV'

MIDDLEWARE += [ 'allow_cidr.middleware.AllowCIDRMiddleware']

ALLOWED_CIDR_NETS = [
    '10.12.0.0/14',
    '10.16.0.0/20'
]


# django-prometheus middleware must be last in middleware stack
MIDDLEWARE += ['django_prometheus.middleware.PrometheusAfterMiddleware']


# Django channels
WS_BASE_URL = 'wss://print-nanny.com:8080/ws'
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [env("CELERY_BROKER_URL")],
        },
    },
}

BETA_NOTIFY_EMAIL = ["beta@print-nanny.com"]


PROMETHEUS_METRICS_EXPORT_PORT_RANGE = range(8001, 8050)

GCP_CLOUD_IOT_DEVICE_REGISTRY = env('GCP_CLOUD_IOT_DEVICE_REGISTRY', default='devices-us-central1-prod')

GCP_MQTT_BRIDGE_HOSTNAME = env('GCP_MQTT_BRIDGE_HOSTNAME', default='mqtt.googleapis.com')
GCP_MQTT_BRIDGE_PORT = env('GCP_MQTT_BRIDGE_PORT', default=443)
GCP_ROOT_CA = env('GCP_ROOT_CA', default='/app/data/google-ca-root-certas.pem')
JWT_EXPIRES_MINUTES = env('JWT_EXPIRES_MINUTES', default=60)

GCP_PUBSUB_TELEMETRY_DEFAULT_TOPIC = env('GCP_PUBSUB_TELEMETRY_DEFAULT', default='projects/print-nanny/topics/telemetry-prod')
GCP_PUBSUB_BOUNDING_BOXES_SUBFOLDER = env('GCP_PUBSUB_BOUNDING_BOXES', default='projects/print-nanny/topics/bounding-boxes-prod')
GCP_PUBSUB_OCTOPRINT_EVENTS_TOPIC = env('GCP_PUBSUB_OCTOPRINT_EVENTS', default='projects/print-nanny/topics/octoprint-events-prod')

GCP_PUBSUB_OCTOPRINT_EVENTS_SUBSCRIPTION = env('GCP_PUBSUB_OCTOPRINT_EVENTS_SUBSCRIPTION', default='projects/print-nanny/subscriptions/octoprint-events-webapp-prod')

STATIC_URL = "https://print-nanny.com/static/"

DEBUG=False