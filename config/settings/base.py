"""
Base settings to build other settings files upon.
"""
from pathlib import Path
import os
import socket
import environ
import subprocess
from django.contrib.messages import constants as messages

from print_nanny_webapp import __version__ as API_VERSION

ROOT_DIR = Path(__file__).resolve(strict=True).parent.parent.parent
# print_nanny_webapp/
APPS_DIR = ROOT_DIR / "print_nanny_webapp"
env = environ.Env()

READ_DOT_ENV_FILE = env.bool("DJANGO_READ_DOT_ENV_FILE", default=False)
if READ_DOT_ENV_FILE:
    # OS environment variables take precedence over variables from .env
    env.read_env(str(ROOT_DIR / ".env"))

# GENERAL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = env.bool("DJANGO_DEBUG", False)
# Local time zone. Choices are
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# though not all of them may be available with every OS.
# In Windows, this must be set to your system time zone.
TIME_ZONE = "UTC"
# https://docs.djangoproject.com/en/dev/ref/settings/#language-code
LANGUAGE_CODE = "en-us"
# https://docs.djangoproject.com/en/dev/ref/settings/#site-id
SITE_ID = 1
# https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_I18N = True
# https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
USE_L10N = True
# https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
USE_TZ = True
# https://docs.djangoproject.com/en/dev/ref/settings/#locale-paths
LOCALE_PATHS = [str(ROOT_DIR / "locale")]

# externally-managed CDN (Google Storage CDN)
CDN_BASE_URL = "https://cdn.print-nanny.com"

# DATABASES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#databases
DEFAULT_AUTO_FIELD = "django.db.models.AutoField"
db_config = env.db("DATABASE_URL")
db_config["ENGINE"] = "django_prometheus.db.backends.postgresql"
DATABASES = {
    "default": db_config,
}
DATABASES["default"]["ATOMIC_REQUESTS"] = True

# URLS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#root-urlconf
ROOT_URLCONF = "config.urls"
# https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = "config.wsgi.application"

ASGI_APPLICATION = "config.asgi.application"

# APPS
# ------------------------------------------------------------------------------
DJANGO_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",  # Handy template tags
    "django.contrib.admin",
    "django.forms",
]
THIRD_PARTY_APPS = [
    "crispy_forms",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "rest_framework",
    "rest_framework.authtoken",
    "django_coturn",
]

LOCAL_APPS = [
    "print_nanny_webapp.alerts.apps.AlertsConfig",
    "print_nanny_webapp.dashboard.apps.DashboardConfig",
    "print_nanny_webapp.devices.apps.DevicesConfig",
    "print_nanny_webapp.ml_ops.apps.MlOpsConfig",
    "print_nanny_webapp.partners.apps.PartnersConfig",
    "print_nanny_webapp.remote_control.apps.RemoteControlConfig",
    "print_nanny_webapp.telemetry.apps.TelemetryConfig",
    "print_nanny_webapp.users.apps.UsersConfig",
    "print_nanny_webapp.surveys.apps.SurveysConfig",
    "print_nanny_webapp.octoprint.apps.OctoprintConfig",
    "print_nanny_webapp.events.apps.EventsConfig",  # Gated at the bottom
    # Your stuff: custom apps go here
]


# https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# MIGRATIONS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#migration-modules
MIGRATION_MODULES = {"sites": "print_nanny_webapp.contrib.sites.migrations"}

# AUTHENTICATION
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#authentication-backends
AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-user-model
AUTH_USER_MODEL = "users.User"
# https://docs.djangoproject.com/en/dev/ref/settings/#login-redirect-url
LOGIN_REDIRECT_URL = "users:redirect"
# https://docs.djangoproject.com/en/dev/ref/settings/#login-url
LOGIN_URL = "account_login"

# PASSWORDS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#password-hashers
PASSWORD_HASHERS = [
    # https://docs.djangoproject.com/en/dev/topics/auth/passwords/#using-argon2-with-django
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
]
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# MIDDLEWARE
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#middleware
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django_prometheus.middleware.PrometheusBeforeMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.common.BrokenLinkEmailsMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# STATIC
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = str(ROOT_DIR / "staticfiles")
# https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = "/static/"
# https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS


VUE_APP_DIR = os.path.join(ROOT_DIR, "print_nanny_vue")
# @TODO rm these staticfiles dirs
STATICFILES_DIRS = [
    ("css", str(APPS_DIR / "static/css")),
    ("fonts", str(APPS_DIR / "static/fonts")),
    ("images", str(APPS_DIR / "static/images")),
    ("js", str(APPS_DIR / "static/js")),
    ("vue", str(APPS_DIR / "static/vue")),
]
# https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

# Webpack loader
# ------------------------------------------------------------------------------
INSTALLED_APPS += ["webpack_loader"]

WEBPACK_LOADER = {
    "DEFAULT": {
        "CACHE": not DEBUG,
        "BUNDLE_DIR_NAME": "vue/",  # must end with slash
        "STATS_FILE": os.path.join(VUE_APP_DIR, "webpack-stats.json"),
        "POLL_INTERVAL": 0.1,
        "TIMEOUT": None,
        "IGNORE": [r".+\.hot-update.js", r".+\.map"],
        "LOADER_CLASS": "webpack_loader.loader.WebpackLoader",
    }
}


# MEDIA
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = str(APPS_DIR / "media")
# https://docs.djangoproject.com/en/dev/ref/settings/#media-url

# TMP_ROOT = str(ROOT_DIR / ".tmp")
# TEMPLATES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#templates
TEMPLATES = [
    {
        # https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-TEMPLATES-BACKEND
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        # https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
        "DIRS": [str(APPS_DIR / "templates")],
        "OPTIONS": {
            # https://docs.djangoproject.com/en/dev/ref/settings/#template-loaders
            # https://docs.djangoproject.com/en/dev/ref/templates/api/#loader-types
            "loaders": [
                "django.template.loaders.filesystem.Loader",
                "django.template.loaders.app_directories.Loader",
            ],
            # https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
                "print_nanny_webapp.utils.context_processors.settings_context",
                "print_nanny_webapp.utils.context_processors.help_context",
            ],
        },
    }
]

# STORAGES
# ------------------------------------------------------------------------------
# https://django-storages.readthedocs.io/en/latest/#installation
INSTALLED_APPS += ["storages"]  # noqa F405
GS_BUCKET_NAME = env("DJANGO_GCP_STORAGE_BUCKET_NAME", default="printnanny-sandbox")
GS_FILE_OVERWRITE = True
GS_DEFAULT_ACL = "projectPrivate"
# STATIC
# ------------------------
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
WHITENOISE_SKIP_COMPRESS_EXTENSIONS = (
    "ico",
    "jpg",
    "jpeg",
    "png",
    "gif",
    "webp",
    "zip",
    "gz",
    "tgz",
    "bz2",
    "tbz",
    "xz",
    "br",
    "swf",
    "flv",
    "woff",
    "woff2",
)
# MEDIA
# ------------------------------------------------------------------------------
DEFAULT_FILE_STORAGE = "print_nanny_webapp.utils.storages.MediaRootGoogleCloudStorage"
MEDIA_URL = f"https://storage.googleapis.com/{GS_BUCKET_NAME}/"


# https://docs.djangoproject.com/en/dev/ref/settings/#form-renderer
FORM_RENDERER = "django.forms.renderers.TemplatesSetting"

# http://django-crispy-forms.readthedocs.io/en/latest/install.html#template-packs
CRISPY_TEMPLATE_PACK = "bootstrap4"
CRISPY_CLASS_CONVERTERS = {"select": "custom-select", "form-group": "input-group"}


# FIXTURES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#fixture-dirs
FIXTURE_DIRS = (str(APPS_DIR / "fixtures"),)

# SECURITY
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#session-cookie-httponly
SESSION_COOKIE_HTTPONLY = False
# https://docs.djangoproject.com/en/dev/ref/settings/#csrf-cookie-httponly
CSRF_COOKIE_HTTPONLY = False
# https://docs.djangoproject.com/en/dev/ref/settings/#secure-browser-xss-filter
SECURE_BROWSER_XSS_FILTER = True
# https://docs.djangoproject.com/en/dev/ref/settings/#x-frame-options
X_FRAME_OPTIONS = "DENY"

# EMAIL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = env(
    "DJANGO_EMAIL_BACKEND", default="django.core.mail.backends.smtp.EmailBackend"
)
# https://docs.djangoproject.com/en/dev/ref/settings/#email-timeout
EMAIL_TIMEOUT = 5

DEFAULT_FROM_EMAIL = env(
    "DJANGO_DEFAULT_FROM_EMAIL", default="Print Nanny <leigh@printnanny.ai>"
)
# https://docs.djangoproject.com/en/dev/ref/settings/#server-email
SERVER_EMAIL = env("DJANGO_SERVER_EMAIL", default=DEFAULT_FROM_EMAIL)
# https://docs.djangoproject.com/en/dev/ref/settings/#email-subject-prefix
EMAIL_SUBJECT_PREFIX = env("DJANGO_EMAIL_SUBJECT_PREFIX", default="[Print Nanny]")

# Anymail
# ------------------------------------------------------------------------------
# https://anymail.readthedocs.io/en/stable/installation/#installing-anymail
INSTALLED_APPS += ["anymail"]  # noqa F405
# https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
# https://anymail.readthedocs.io/en/stable/installation/#anymail-settings-reference
# https://anymail.readthedocs.io/en/stable/esps/mailgun/
EMAIL_BACKEND = "anymail.backends.mailgun.EmailBackend"
ANYMAIL = {
    "MAILGUN_API_KEY": env("MAILGUN_API_KEY"),
    "MAILGUN_SENDER_DOMAIN": env("MAILGUN_DOMAIN"),
    "MAILGUN_API_URL": env("MAILGUN_API_URL", default="https://api.mailgun.net/v3"),
    # "WEBHOOK_SECRET": env("MAILGUN_WEBHOOK_SECRET")
}

# Discord
# ------------------------------------------------------------------------------
DISCORD_TOKEN = env("DISCORD_TOKEN", default="")


# ADMIN
# ------------------------------------------------------------------------------
# Django Admin URL.
ADMIN_URL = "admin/"
# https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = [("""Leigh Johnson""", "leigh@printnanny.ai")]
# https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS

# LOGGING
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#logging
# See https://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGLEVEL = env("LOGLEVEL", default="INFO").upper()
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
    "root": {"level": LOGLEVEL, "handlers": ["console"]},
}

REDIS_URL = env("REDIS_URL")

# django-allauth
# ------------------------------------------------------------------------------
ACCOUNT_ALLOW_REGISTRATION = env.bool("DJANGO_ACCOUNT_ALLOW_REGISTRATION", True)
# https://django-allauth.readthedocs.io/en/latest/configuration.html
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_FORMS = {"signup": "print_nanny_webapp.users.forms.UserCreationForm"}


# https://django-allauth.readthedocs.io/en/latest/configuration.html
ACCOUNT_EMAIL_REQUIRED = True
# https://django-allauth.readthedocs.io/en/latest/configuration.html
ACCOUNT_EMAIL_VERIFICATION = "optional"
# https://django-allauth.readthedocs.io/en/latest/configuration.html
ACCOUNT_ADAPTER = "print_nanny_webapp.users.adapters.AccountAdapter"
# https://django-allauth.readthedocs.io/en/latest/configuration.html
SOCIALACCOUNT_ADAPTER = "print_nanny_webapp.users.adapters.SocialAccountAdapter"
# django-compressor
# ------------------------------------------------------------------------------
# https://django-compressor.readthedocs.io/en/latest/quickstart/#installation
# INSTALLED_APPS += ["compressor"]
# STATICFILES_FINDERS += ["compressor.finders.CompressorFinder"]
# django-rest-framework
# -------------------------------------------------------------------------------
# django-rest-framework - https://www.django-rest-framework.org/api-guide/settings/
# drf-spectacular
INSTALLED_APPS += ["drf_spectacular"]
PAGE_SIZE = 20
REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.SessionAuthentication",
        "print_nanny_webapp.users.authentication.BearerTokenAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
    "DEFAULT_PAGINATION_CLASS": "print_nanny_webapp.utils.pagination.PageNumberPagination",
    "PAGE_SIZE": PAGE_SIZE,
    # 'ALLOWED_VERSIONS': ('v0','v1', ''),
    # 'DEFAULT_VERSION': 'v0'
}

# Your stuff...
# ------------------------------------------------------------------------------

SPECTACULAR_SETTINGS = {
    "SCHEMA_PATH_PREFIX": "/api",
    # 'COMPONENT_NO_READ_ONLY_REQUIRED': True,
    "COMPONENT_SPLIT_REQUEST": True,
    "ENUM_ADD_EXPLICIT_BLANK_NULL_CHOICE": True,
    "SCHEMA_COERCE_PATH_PK_SUFFIX": True,
    "ENUM_NAME_OVERRIDES": {
        # TODO refactor event apps+namespaces for clarity before adding mainsail
        # begin device app enums
        "CameraType": "print_nanny_webapp.devices.enum.CameraType",
        "JanusConfigType": "print_nanny_webapp.devices.enum.JanusConfigType",
        "DeviceReleaseChannel": "print_nanny_webapp.devices.enum.DeviceReleaseChannel",
        # begin alerts app enums
        "PrintProgressAlertEventType": "print_nanny_webapp.alerts.models.PrintProgressAlert.PrintProgressAlertEventType.choices",
        "AlertMessageType": "print_nanny_webapp.alerts.models.AlertMessage.AlertMessageType.choices",
        "AlertSettingsEventType": "print_nanny_webapp.alerts.models.AlertSettings.AlertSettingsEventType.choices",
        # begin octoprint event types
        "OctoTelemetryEvent": "print_nanny_webapp.telemetry.enum.TelemetryEventType",
        "OctoPrintNannyEvent": "print_nanny_webapp.telemetry.enum.PrintNannyPluginEventType",
        "OctoGenericEvent": "print_nanny_webapp.telemetry.enum.OctoprintEventType",
        "OctoJobEvent": "print_nanny_webapp.telemetry.enum.PrintJobEventType",
        "OctoPrinterEvent": "print_nanny_webapp.telemetry.enum.PrinterEventType",
        "AlphaEventSource": "print_nanny_webapp.telemetry.enum.EventSource",
        # begin webrtc event types
        "TestEventName": "print_nanny_webapp.events.enum.TestEventName",
        "WebRTCEventName": "print_nanny_webapp.events.enum.WebRTCEventName",
        "EventType": "print_nanny_webapp.events.enum.EventType",
        "EventSource": "print_nanny_webapp.events.enum.EventSource",
    },
    "TITLE": "printnanny-api-client",
    "DESCRIPTION": "Official API client library forprintnanny.ai print-nanny.com",
    "LICENSE": {"name": "AGPLv3"},
    "CONTACT": {
        "name": "Leigh Johnson",
        "email": "leigh@printnanny.ai",
        "url": "https://print-nanny.com",
    },
}

# django-filters
# ------------------------------------------------------------------------------
INSTALLED_APPS += ["django_filters"]

# django-prometheus
# ------------------------------------------------------------------------------
INSTALLED_APPS += ["django_prometheus"]

PROMETHEUS_METRICS_EXPORT_PORT_RANGE = range(8001, 8050)
PROMETHEUS_METRICS_EXPORT_ADDRESS = ""  # all addresses
# https://github.com/korfuri/django-prometheus/issues/252
PROMETHEUS_EXPORT_MIGRATIONS = False


# ------------------------------------------------------------------------------
# django-polymorphic

INSTALLED_APPS += [
    "polymorphic",
]

# django-invitations
# ------------------------------------------------------------------------------
INSTALLED_APPS += [
    "invitations",
]
ACCOUNT_ADAPTER = "invitations.models.InvitationsAdapter"
INVITATIONS_ADAPTER = ACCOUNT_ADAPTER
INVITATIONS_INVITATION_ONLY = False
INVITATIONS_INVITATION_EXPIRY = 30
INVITATIONS_EMAIL_SUBJECT_PREFIX = "[Print Nanny]"
INVITATIONS_ACCEPT_INVITE_AFTER_SIGNUP = True

# channels
# ------------------------------------------------------------------------------
INSTALLED_APPS += [
    "channels",
]

APPEND_SLASH = True

# pubsub and cloud iot
# ------------------------------------------------------------------------------
GCP_MQTT_BRIDGE_HOSTNAME = "mqtt.2030.ltsapis.goog"
GCP_MQTT_BRIDGE_PORT = 443
GCP_LTS_CA_PRIMARY = "https://pki.goog/gtsltsr/gtsltsr.crt"
GCP_LTS_CA_BACKUP = "https://pki.goog/gsr4/GSR4.crt"

GCP_PUBSUB_UNDELIVERED_HEALTH_THRESHOLD_MINUTES = 10

GCP_PROJECT_ID = env("GCP_PROJECT_ID", default="printnanny-sandbox")

GCP_CLOUDIOT_DEVICE_REGISTRY_REGION = "us-central1"
GCP_CLOUDIOT_STANDALONE_DEVICE_REGISTRY = env(
    "GCP_CLOUDIOT_DEVICE_REGISTRY", default="printnanny-os--sandbox"
)
GCP_CLOUDIOT_OCTOPRINT_DEVICE_REGISTRY = env(
    "GCP_CLOUDIOT_DEVICE_REGISTRY_DEPRECATED", default="octoprint-devices"
)

GCP_PUBSUB_TELEMETRY_DEFAULT_TOPIC = env(
    "GCP_PUBSUB_TELEMETRY_DEFAULT",
    default=os.path.join("projects", GCP_PROJECT_ID, "topics/default-telemetry"),
)

GCP_PUBSUB_OCTOPRINT_EVENTS_TOPIC = env(
    "GCP_PUBSUB_OCTOPRINT_EVENTS",
    default=os.path.join("projects", GCP_PROJECT_ID, "topics/octoprint-events"),
)

GCP_PUBSUB_OCTOPRINT_EVENTS_SUBSCRIPTION = env(
    "GCP_PUBSUB_OCTOPRINT_EVENTS_SUBSCRIPTION",
    default=os.path.join(
        "projects", GCP_PROJECT_ID, "subscriptions/octoprint-events-pull"
    ),
)

GCP_PUBSUB_OCTOPRINT_ALERTS_SUBSCRIPTION = env(
    "GCP_PUBSUB_OCTOPRINT_ALERTS_SUBSCRIPTION",
    default=os.path.join("projects", GCP_PROJECT_ID, "subscriptions/alerts-pull"),
)

MESSAGE_STORAGE = "django.contrib.messages.storage.cookie.CookieStorage"

# honeycomb
# ------------------------------------------------------------------------------
# https://docs.honeycomb.io/getting-data-in/beelines/
HONEYCOMB_DATASET = env("HONEYCOMB_DATASET", default="print_nanny_sandbox")
HONEYCOMB_SERVICE_NAME = env("HONEYCOMB_SERVICE_NAME", default="django")
HONEYCOMB_API_KEY = env("HONEYCOMB_API_KEY", default="noop")


# django-health-check
# ------------------------------------------------------------------------------
INSTALLED_APPS += [
    "health_check",  # required
    "health_check.db",  # stock Django health checkers
    "health_check.cache",
    "health_check.contrib.migrations",
    "health_check.contrib.redis",  # requires Redis broker
]

# ------------------------------------------------------------------------------
# help guides + other notion wiki links

ROADMAP_URL = (
    "https://bitsy-ai.notion.site/Print-Nanny-Roadmap-7b48a2c8d83248eea2de14edfeaf52ee"
)
HELP_OCTOPRINT_PLUGIN_SETUP = "https://help.print-nanny.com/octoprint-plugin-setup/"
HELP_WIKI = "https://www.notion.so/bitsy-ai/Print-Nanny-Guides-Support-ac1079fafc944d769aa21cf8bffe4692"
HELP_GETTING_STARTED = "https://bitsy-ai.notion.site/Getting-Started-with-Print-Nanny-817bc65297ff44a085120c663dced5f3"
HELP_DEVICE_PKI = "https://www.notion.so/bitsy-ai/Securing-IoT-Devices-with-PKI-f9e728fb1e734e6d95efb930d9f23620"
ERROR_ACTIVATE_LICENSE = "https://www.notion.so/bitsy-ai/License-Activation-Failed-99bb98ebc01546979717da214d2198c8"
HELP_BOOK_30M = "https://calendly.com/bitsy-ai-labs/30min"
HELP_BOOK_60M = "https://calendly.com/bitsy-ai-labs/60min"
# dj-stripe
# ------------------------------------------------------------------------------
INSTALLED_APPS += ["djstripe"]
INSTALLED_APPS += ["print_nanny_webapp.subscriptions.apps.SubscriptionsConfig"]

DJSTRIPE_USE_NATIVE_JSONFIELD = True
STRIPE_LIVE_MODE = env("STRIPE_LIVE_MODE", default=False)
# https://github.com/dj-stripe/dj-stripe/issues/1360
DJSTRIPE_WEBHOOK_SECRET = env("DJSTRIPE_WEBHOOK_SECRET", default="whsec_x")
STRIPE_TEST_PUBLIC_KEY = env("STRIPE_TEST_PUBLIC_KEY", default="pk_test_x")
STRIPE_TEST_SECRET_KEY = env("STRIPE_TEST_SECRET_KEY", default="sk_test_x")
STRIPE_LIVE_PUBLIC_KEY = env("STRIPE_LIVE_PUBLIC_KEY", default="pk_live_x")
STRIPE_LIVE_SECRET_KEY = env("STRIPE_LIVE_SECRET_KEY", default="sk_live_x")
DJSTRIPE_FOREIGN_KEY_TO_FIELD = "id"

FREE_BETA_TESTER_IDS = range(0, 102)
PAID_BETA_LAUNCH_TIMESTAMP = 1628528400  # 10 AM PDT 2021-08-09
PAID_BETA_SUBSCRIPTION_LIMIT = 29

TRIAL_PERIOD_DAYS = 30
REFERRAL_COUPON_DAYS = 30

# django-safedelete
# ------------------------------------------------------------------------------
INSTALLED_APPS += ["safedelete"]

# django-flags
# ------------------------------------------------------------------------------
INSTALLED_APPS += ["flags"]

FLAGS = {
    "PARTNER_3DGEEKS_ENABLED": [{"condition": "parameter", "value": "3dgeeks_enabled="}]
}

# 3D Geeks Integration settings
# ------------------------------------------------------------------------------
PARTNERS_3DGEEKS_SETTINGS = {
    "alerts_push": "https://qx8eve27wk.execute-api.eu-west-2.amazonaws.com/prod/printnanny_push"
}

# messages
# ------------------------------------------------------------------------------
MESSAGE_TAGS = {
    messages.DEBUG: "alert-info",
    messages.INFO: "alert-info",
    messages.SUCCESS: "alert-success",
    messages.WARNING: "alert-warning",
    messages.ERROR: "alert-danger",
}

# messages
# ------------------------------------------------------------------------------
GCP_RENDER_VIDEO_TOPIC = "VideoRenderRequest"


# links
# ------------------------------------------------------------------------------
DISCORD_URL = "https://discord.gg/sf23bk2hPr"
REPORT_ISSUE_URL = (
    "https://help.print-nanny.com/faq/how-to-report-issue-with-octoprint-logs"
)
HELP_SITE_URL = "https://help.print-nanny.com"
BLOG_SITE_URL = "https://blog.print-nanny.com"
ABOUT_URL = "https://blog.print-nanny.com/about"
GITHUB_ISSUE_URL = "https://github.com/bitsy-ai/octoprint-nanny-plugin/issues/new"

# drfpasswordless
# https://github.com/aaronn/django-rest-framework-passwordless
# ------------------------------------------------------------------------------
INSTALLED_APPS += ["drfpasswordless"]
PASSWORDLESS_AUTH = {
    "PASSWORDLESS_AUTH_TYPES": ["EMAIL"],
    "PASSWORDLESS_USER_MARK_EMAIL_VERIFIED": True,
    "PASSWORDLESS_EMAIL_NOREPLY_ADDRESS": "noreply@print-nanny.com",
    "PASSWORDLESS_EMAIL_PLAINTEXT_MESSAGE": "Enter this token to sign in: %s",
}

# django-coturn
# https://github.com/bitsy-ai/django-coturn
# ------------------------------------------------------------------------------
coturn_db = env.db("COTURN_DATABASE_URL")
coturn_db["ENGINE"] = "django_prometheus.db.backends.postgresql"
DATABASES["coturn"] = coturn_db
COTURN_SECRET_KEY = env("COTURN_SECRET_KEY")
COTURN_REALM = env("COTURN_REALM")

# ghost user management keys
GHOST_ADMIN_API_KEY = ""
GHOST_CONTENT_API_KEY = ""

# internal PRINTNANNY_ vars
# ------------------------------------------------------------------------------
PRINTNANNY_ENV = env("PRINTNANNY_ENV", default="sandbox")

# posthog
# ------------------------------------------------------------------------------
POSTHOG_API_KEY = env("POSTHOG_API_KEY", default=None)
POSTHOG_ENABLED = False

# corsheaders
# see also: corsheaders.middleware.CorsMiddleware
# ------------------------------------------------------------------------------
INSTALLED_APPS += ["corsheaders"]
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOWED_ORIGINS = [
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    f"http://{socket.gethostname()}:8000",
]

# Janus cloud
# ------------------------------------------------------------------------------
JANUS_CLOUD_DOMAIN = env("JANUS_CLOUD_DOMAIN", default="localhost")
JANUS_CLOUD_ADMIN_SECRET = env("JANUS_CLOUD_ADMIN_SECRET", default="debug")
JANUS_CLOUD_ADMIN_URL = env(
    "JANUS_CLOUD_ADMIN_URL", default="http://localhost:7088/admin"
)
JANUS_CLOUD_ADMIN_PORT = env("JANUS_CLOUD_ADMIN_PORT", default=7088)
JANUS_CLOUD_API_URL = env(
    "JANUS_CLOUD_ADMIN_HTTP_PORT", default="http://localhost:8088/janus"
)
JANUS_CLOUD_API_PORT = env("JANUS_CLOUD_API_PORT", default=8088)
JANUS_CLOUD_WS_URL = env("JANUS_CLOUD_WS_URL", default="ws://aurora.local:8188")
JANUS_CLOUD_WS_PORT = env("JANUS_CLOUD_WS_PORT", default=8188)
JANUS_CLOUD_RTP_PORT_RANGE = env.tuple(
    "JANUS_CLOUD_RTP_PORT_RANGE", default=(5000, 5050)
)
JANUS_CLOUD_STREAMING_ADMIN_KEY = env(
    "JANUS_CLOUD_STREAMING_ADMIN_KEY", default="debugstreaming"
)
JANUS_CLOUD_RTP_DOMAIN = env("JANUS_CLOUD_RTP_DOMAIN", default="localhost")

# django-qr-code
# https://django-qr-code.readthedocs.io/en/latest/pages/README.html
# ------------------------------------------------------------------------------
INSTALLED_APPS += ["qr_code"]
SERVE_QR_CODE_IMAGE_PATH = "qr/"

# set build version
# ------------------------------------------------------------------------------
GIT_SHA = env("GIT_SHA", default="No GIT_SHA specified")
