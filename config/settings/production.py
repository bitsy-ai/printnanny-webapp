import posthog
from config.settings.base import *  # noqa


# GENERAL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = env("DJANGO_SECRET_KEY")
# https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = env.list(
    "DJANGO_ALLOWED_HOSTS",
    default=[
        ".printnanny.ai",
    ],
)

# posthog
# ------------------------------------------------------------------------------
# https://posthog.com/docs/libraries/python
POSTHOG_API_KEY = env("POSTHOG_API_KEY", default=None)
POSTHOG_ENABLED = True
posthog.project_api_key = POSTHOG_API_KEY
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
SECURE_SSL_REDIRECT = env.bool("DJANGO_SECURE_SSL_REDIRECT", default=False)
# https://docs.djangoproject.com/en/dev/ref/settings/#session-cookie-secure
SESSION_COOKIE_SECURE = True
# https://docs.djangoproject.com/en/dev/ref/settings/#csrf-cookie-secure
CSRF_COOKIE_SECURE = True
# https://docs.djangoproject.com/en/3.2/ref/settings/#csrf-cookie-domain
CSRF_COOKIE_DOMAIN = env("DJANGO_CSRF_COOKIE_DOMAIN", default=".printnanny.ai")
CSRF_TRUSTED_ORIGINS = [
    "api.printnanny.ai",
    ".printnanny.ai",
    "printnanny.ai",
    "www.printnanny.ai",
]
SESSION_COOKIE_DOMAIN = env("DJANGO_SESSION_COOKIE_DOMAIN", default=".printnanny.ai")

# https://docs.djangoproject.com/en/3.2/ref/middleware/#referrer-policy
# SECURE_REFERRER_POLICY = "no-referrer-when-downgrade"

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
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s "
            "%(process)d %(thread)d %(message)s"
        }
    },
    "handlers": {
        "console": {
            "level": LOGLEVEL,
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        }
    },
    "filters": {
        "exclude_health_endpoint": {
            "()": "print_nanny_webapp.utils.logging.ExcludeHealthEndpoint",
        },
    },
    "root": {"level": LOGLEVEL, "handlers": ["console"]},
    "loggers": {
        "django.db.backends": {
            "level": "INFO",
            "handlers": ["console"],
            "propagate": False,
        },
        # Errors logged by the SDK itself
        "django.security.DisallowedHost": {
            "level": "INFO",
            "handlers": ["console"],
            "propagate": False,
        },
        "health-check": {
            "handlers": ["console"],
            "level": "WARNING",
            "propagate": True,
        },
        "uvicorn": {
            "handlers": ["console"],
            "level": LOGLEVEL,
            "filters": ["exclude_health_endpoint"],
        },
    },
}

# Your stuff...
# ------------------------------------------------------------------------------


GOOGLE_ANALYTICS = "G-QKHED5DPGV"

MIDDLEWARE += [
    "allow_cidr.middleware.AllowCIDRMiddleware",
    "print_nanny_webapp.middleware.honeycomb.HoneyMiddlewareIgnoreHealthCheck",
]

ALLOWED_CIDR_NETS = [
    # Cluster pod address range (www-beta)
    "10.12.0.0/14",
    # Service address range (www-beta)
    "10.16.0.0/20",
    # Cluster pod address range (www-spot)
    "10.40.0.0/14",
    # Service address range (www-beta)
    "10.44.0.0/20",
]


# django-prometheus middleware must be last in middleware stack
MIDDLEWARE += ["django_prometheus.middleware.PrometheusAfterMiddleware"]


# Django channels
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [env("REDIS_URL")],
        },
    },
}

BETA_NOTIFY_EMAIL = ["beta@print-nanny.com"]

GCP_PROJECT_ID = env("GCP_PROJECT_ID", default="print-nanny")

DEBUG = False

# dj-stripe
# ------------------------------------------------------------------------------
STRIPE_LIVE_MODE = True

# ghost member sync
# async task print_nanny_webapp/users/tasks.py
# ------------------------------------------------------------------------------
GHOST_ADMIN_API_KEY = env("GHOST_ADMIN_API_KEY")
GHOST_CONTENT_API_KEY = env("GHOST_CONTENT_API_KEY")

# CORS
# see also: corsheaders.middleware.CorsMiddleware
# https://pypi.org/project/django-cors-headers/
# ------------------------------------------------------------------------------
CORS_ALLOWED_ORIGINS = [
    "https://print-nanny.com",
    "https://www.print-nanny.com",
    "https://printnanny.ai",
    "https://www.printnanny.ai",
    "https://live.printnanny.ai",
    "https://www.live.printnanny.ai",
    "https://beta.printnanny.ai",
    "https://www.beta.printnanny.ai",
    "https://cdn.printnanny.ai",
    "https://api.printnanny.ai",
    "https://api.live.printnanny.ai",
]

# posthog
# ------------------------------------------------------------------------------
# https://posthog.com/docs/libraries/python
posthog.project_api_key = env("POSTHOG_API_KEY")
posthog.debug = False

# cloudiot registry
# ------------------------------------------------------------------------------
GCP_CLOUDIOT_STANDALONE_DEVICE_REGISTRY = env(
    "GCP_CLOUDIOT_DEVICE_REGISTRY", default="printnanny-os--live"
)
