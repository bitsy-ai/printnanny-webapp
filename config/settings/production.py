import posthog
from config.settings.base import *  # noqa
from django_ghost.settings import GhostLabel, DEFAULT_GHOST_LABEL


# GENERAL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
DEBUG = False
DJANGO_VITE_DEV_MODE = DEBUG

SECRET_KEY = env("DJANGO_SECRET_KEY")
# https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = env.list(
    "DJANGO_ALLOWED_HOSTS",
    default=[
        ".printnanny.ai",
    ],
)

# Anymail
EMAIL_BACKEND = "anymail.backends.mailgun.EmailBackend"
ANYMAIL = {
    "MAILGUN_API_KEY": env("MAILGUN_API_KEY"),
    "MAILGUN_SENDER_DOMAIN": env("MAILGUN_DOMAIN"),
    "MAILGUN_API_URL": env("MAILGUN_API_URL", default="https://api.mailgun.net/v3"),
    "MAILGUN_WEBHOOK_SIGNING_KEY": env("MAILGUN_WEBHOOK_SIGNING_KEY"),
    # TODO: Basic auth headers used with PSK are getting stripped at L7 or L4 LB
    # since webhook requests are already signed, we can disable basic auth - but it'd be good to figure out what's stripping this header
    # "WEBHOOK_SECRET": env("ANYMAIL_WEBHOOK_SECRET", default="debug:debug"),
}


# posthog
# ------------------------------------------------------------------------------
# https://posthog.com/docs/libraries/python
POSTHOG_API_KEY = env("POSTHOG_API_KEY", default=None)
posthog.project_api_key = POSTHOG_API_KEY
posthog.debug = False
posthog.disabled = False
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
SECURE_REFERRER_POLICY = "no-referrer-when-downgrade"

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
    "disable_existing_loggers": True,
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
        },
        "mail_admins": {
            "level": "ERROR",
            "class": "print_nanny_webapp.utils.logging.ThrottledAdminEmailHandler",
        },
    },
    "filters": {
        "exclude_health_endpoint": {
            "()": "print_nanny_webapp.utils.logging.ExcludeHealthEndpoint",
        },
    },
    "root": {"level": LOGLEVEL, "handlers": ["console"]},
    "loggers": {
        "django": {
            "handlers": ["mail_admins", "console"],
            "level": LOGLEVEL,
            "propagate": True,
        },
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
STRIPE_STARTER_PRODUCT_ID = env(
    "STRIPE_STARTER_PRODUCT_ID", default="prod_NJKFEljTzEuDff"
)
STRIPE_SCALER_PRODUCT_ID = env(
    "STRIPE_SCALER_PRODUCT_ID", default="prod_NJKFYsIwRIZwDb"
)
STRIPE_PORTAL_URL = env(
    "STRIPE_PORTAL_URL",
    default="https://billing.stripe.com/p/login/00g4gC9wu9fu9O07ss",
)


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

# django-nats-nkeys
NATS_SERVER_URI = env("NATS_SERVER_URI", default="nats://nats.live.printnanny.ai:4222")
NATS_WS_URI = env("NATS_WS_URI", default="wss://nats.live.printnanny.ai:8443")
NATS_MQTT_BROKER_HOST = env("NATS_MQTT_BROKER_HOST", default="mqtt.live.printnanny.ai")
NATS_MQTT_BROKER_PORT = env("NATS_MQTT_BROKER_PORT", default=1883)


# django-ghost
# sync EmailWaitlist with Ghost newsletter list
INSTALLED_APPS += ["django_ghost"]
GHOST_API_URL = env("GHOST_API_URL", default="https://printnanny.ai/blog")
GHOST_NEWSLETTER_IDS = env.list("GHOST_NEWSLETTER_IDS", default=[])
GHOST_ADMIN_API_APP_ID = env("GHOST_ADMIN_API_APP_ID")
GHOST_ADMIN_API_APP_SECRET = env("GHOST_ADMIN_API_APP_SECRET")
GHOST_SYNC_MODEL = "users.EmailWaitlist"
GHOST_MEMBER_LABELS = [
    DEFAULT_GHOST_LABEL,
    GhostLabel(name="PrintNanny Waitlist", slug="printnanny_waitlist"),
]

# firehose NATS app
# ------------------------------------------------------------------------------
NATS_FIREHOSE_NKEY = env(
    "NATS_FIREHOSE_NKEY", default="/app/.production/.firehose/nkey"
)
