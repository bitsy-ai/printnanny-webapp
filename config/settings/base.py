"""
Base settings to build other settings files upon.
"""
from pathlib import Path
from typing import List, Tuple
import re

import socket
import environ
import os
import posthog

from django.contrib.messages import constants as messages


ROOT_DIR = Path(__file__).resolve(strict=True).parent.parent.parent
# print_nanny_webapp/
APPS_DIR = ROOT_DIR / "print_nanny_webapp"
UI_DIR = ROOT_DIR / "ui"
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
]

LOCAL_APPS = [
    "print_nanny_webapp.achievements.apps.AchievementsConfig",
    "print_nanny_webapp.crash_reports.apps.CrashReportsConfig",
    "print_nanny_webapp.devices.apps.DevicesConfig",
    "print_nanny_webapp.email_campaigns.apps.EmailCampaignsConfig",
    "print_nanny_webapp.users.apps.UsersConfig",
    "print_nanny_webapp.surveys.apps.SurveysConfig",
    "print_nanny_webapp.octoprint.apps.OctoprintConfig",
    "print_nanny_webapp.moonraker.apps.MoonrakerConfig",
    "print_nanny_webapp.shop.apps.ShopConfig",
    "print_nanny_webapp.videos.apps.VideosConfig",
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
    "oauth2_provider.backends.OAuth2Backend",
    "print_nanny_webapp.drfpasswordless.backends.PasswordlessBackend",
    "django.contrib.auth.backends.ModelBackend",
]
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-user-model
AUTH_USER_MODEL = "users.User"
# https://docs.djangoproject.com/en/dev/ref/settings/#login-redirect-url
LOGIN_REDIRECT_URL = "/devices/"
# https://docs.djangoproject.com/en/dev/ref/settings/#login-url
LOGIN_URL = "/login/"

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
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django_prometheus.middleware.PrometheusBeforeMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "print_nanny_webapp.utils.middleware.DomainRedirectMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "oauth2_provider.middleware.OAuth2TokenMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]
# ------------------------------------------------------------------------------
# STATIC
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = env("DJANGO_STATIC_URL", default="/ui/")
# https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
BASE_URL = env("DJANGO_BASE_URL", default="/")
WS_BASE_URL = env("DJANGO_WS_URL", default="/ws")

STATICFILES_DIRS = [str(ROOT_DIR / "ui/dist/")]
STATIC_ROOT = str(ROOT_DIR / "staticfiles")
# https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

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
        "DIRS": [str(APPS_DIR / "templates"), str(ROOT_DIR / "ui/dist")],
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
    "DJANGO_DEFAULT_FROM_EMAIL", default="PrintNanny <noreply@printnanny.ai>"
)
# https://docs.djangoproject.com/en/dev/ref/settings/#server-email
SERVER_EMAIL = env("DJANGO_SERVER_EMAIL", default=DEFAULT_FROM_EMAIL)
# https://docs.djangoproject.com/en/dev/ref/settings/#email-subject-prefix
EMAIL_SUBJECT_PREFIX = env("DJANGO_EMAIL_SUBJECT_PREFIX", default="[PrintNanny]")

# Anymail
# ------------------------------------------------------------------------------
# https://anymail.readthedocs.io/en/stable/installation/#installing-anymail
INSTALLED_APPS += ["anymail"]  # noqa F405
# https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
# https://anymail.readthedocs.io/en/stable/installation/#anymail-settings-reference
# https://anymail.readthedocs.io/en/stable/esps/mailgun/
EMAIL_HOST = env("EMAIL_HOST", default="mailhog")
EMAIL_PORT = 1025

# Discord
# ------------------------------------------------------------------------------
DISCORD_TOKEN = env("DISCORD_TOKEN", default="")
DISCORD_NEW_SIGNUP_WEBHOOK = env("DISCORD_NEW_SIGNUP_WEBHOOK", default=None)


# ADMIN
# ------------------------------------------------------------------------------
# Django Admin URL.
ADMIN_URL = "admin/"
# https://docs.djangoproject.com/en/dev/ref/settings/#admins
# ADMINS = [("""Leigh Johnson""", "leigh+alerts@printnanny.ai")]
ADMINS: List[Tuple[str, str]] = []
# https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS: List[Tuple[str, str]] = ADMINS
DEMO_GROUP = "demo"

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
        "oauth2_provider.contrib.rest_framework.OAuth2Authentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": (
        "rest_framework.permissions.IsAuthenticated",
        "print_nanny_webapp.utils.api.permissions.IsObjectOwner",
    ),
    "DEFAULT_FILTER_BACKENDS": [
        "django_filters.rest_framework.DjangoFilterBackend",
        "print_nanny_webapp.utils.api.filters.OwnerOrUserFilterBackend",
    ],
    "DEFAULT_PAGINATION_CLASS": "print_nanny_webapp.utils.pagination.PageNumberPagination",
    "PAGE_SIZE": PAGE_SIZE,
    "EXCEPTION_HANDLER": "print_nanny_webapp.utils.api.exceptions.custom_exception_handler"
    # 'ALLOWED_VERSIONS': ('v0','v1', ''),
    # 'DEFAULT_VERSION': 'v0'
}

# Your stuff...
# ------------------------------------------------------------------------------
with open("version.txt", "r", encoding="utf-8") as f:
    API_VERSION = f.read()

# from djstripe.enums import SessionMode
# import djstripe.fields

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
        "PreferredDnsType": "print_nanny_webapp.devices.enum.PreferredDnsType",
        # end device app enums
        # begin alerts app enums
        # end alerts app enums
        # begin Pi polymorphic event types
        "PiEventModel": "print_nanny_webapp.events.models.enum.PiEventModel",
        "PiCamStatusType": "print_nanny_webapp.events.models.enum.PiCamStatusType",
        "PiCamCommandType": "print_nanny_webapp.events.models.enum.PiCamCommandType",
        "PiSoftwareUpdateStatusType": "print_nanny_webapp.events.models.enum.PiSoftwareUpdateStatusType",
        "PiSoftwareUpdateCommandType": "print_nanny_webapp.events.models.enum.PiSoftwareUpdateCommandType",
        "PiBootStatusType": "print_nanny_webapp.events.models.enum.PiBootStatusType",
        "PiBootCommandType": "print_nanny_webapp.events.models.enum.PiBootCommandType",
        # end Pi polymorphic event types
        "GcodeEventType": "print_nanny_webapp.events.models.enum.GcodeEventType",
        # begin OctoPrint polymorphic event types
        "OctoPrintPrintJobStatusType": "print_nanny_webapp.octoprint.enum.OctoPrintPrintJobStatusType",
        "OctoPrintServerStatusType": "print_nanny_webapp.octoprint.enum.OctoPrintServerStatusType",
        "OctoPrintPrinterStatusType": "print_nanny_webapp.octoprint.enum.OctoPrintPrinterStatusType",
        # end OctoPrint polymorphic event types
        # begin shop types
        "OrderStatusType": "print_nanny_webapp.shop.enum.OrderStatusType",
        # end shop types
        # begin djstipe enum types
        "StripeApiKeyType": "djstripe.enums.APIKeyType.choices",
        "StripeApiErrorCode": "djstripe.enums.ApiErrorCode.choices",
        "StripeAccountTypeCode": "djstripe.enums.AccountType.choices",
        "StripeBalanceTransactionStatus": "djstripe.enums.BalanceTransactionStatus.choices",
        "StripeBalanceTransactionType": "djstripe.enums.BalanceTransactionReportingCategory.choices",
        "StripeBankAccountHolderType": "djstripe.enums.BankAccountHolderType.choices",
        "StripeBankAccountStatus": "djstripe.enums.BankAccountStatus.choices",
        "StripeBillingScheme": "djstripe.enums.BillingScheme.choices",
        "StripeBalanceTransactionReportingCategory": "djstripe.enums.BalanceTransactionReportingCategory.choices",
        "StripeBusinessType": "djstripe.enums.BusinessType.choices",
        "StripeCaptureMethod": "djstripe.enums.BalanceTransactionReportingCategory.choices",
        "StripeCardCheckResult": "djstripe.enums.CardCheckResult.choices",
        "StripeCardBrand": "djstripe.enums.BalanceTransactionReportingCategory.choices",
        "StripeCardFundingType": "djstripe.enums.CardFundingType.choices",
        "StripeCardTokenizationMethod": "djstripe.enums.CardTokenizationMethod.choices",
        "StripeChargeStatus": "djstripe.enums.ChargeStatus.choices",
        "StripeConfirmationMethod": "djstripe.enums.ConfirmationMethod.choices",
        "StripeCouponDuration": "djstripe.enums.CouponDuration.choices",
        "StripeCustomerTaxExempt": "djstripe.enums.CustomerTaxExempt.choices",
        "StripeDisputeReason": "djstripe.enums.DisputeReason.choices",
        "StripeDisputeStatus": "djstripe.enums.DisputeStatus.choices",
        "StripeFilePurpose": "djstripe.enums.FilePurpose.choices",
        "StripeFileType": "djstripe.enums.FileType.choices",
        "StripeInvoiceBillingReason": "djstripe.enums.InvoiceBillingReason.choices",
        "StripeInvoiceCollectionMethod": "djstripe.enums.InvoiceCollectionMethod.choices",
        "StripeIntentUsage": "djstripe.enums.IntentUsage.choices",
        "StripeIntentStatus": "djstripe.enums.IntentStatus.choices",
        "StripeMandateStatus": "djstripe.enums.MandateStatus.choices",
        "StripePaymentIntentStatus": "djstripe.enums.PaymentIntentStatus.choices",
        "StripeMandateType": "djstripe.enums.MandateType.choices",
        "StripeSetupIntentStatus": "djstripe.enums.SetupIntentStatus.choices",
        "StripePaymentMethodType": "djstripe.enums.PaymentMethodType.choices",
        "StripePayoutFailureCode": "djstripe.enums.PayoutFailureCode.choices",
        "StripePayoutMethod": "djstripe.enums.PayoutMethod.choices",
        "StripePayoutSourceType": "djstripe.enums.PayoutSourceType.choices",
        "StripePaymentIntentCancellationReason": "djstripe.enums.PaymentIntentCancellationReason.choices",
        "StripePlanAggregateUsage": "djstripe.enums.PlanAggregateUsage.choices",
        "StripePlanInterval": "djstripe.enums.PlanInterval.choices",
        "StripePriceTiersMode": "djstripe.enums.PriceTiersMode.choices",
        "StripePriceType": "djstripe.enums.PriceType.choices",
        "StripePriceUsageType": "djstripe.enums.PriceUsageType.choices",
        "StripeProductType": "djstripe.enums.ProductType.choices",
        "StripeSetupIntentCancellationReason": "djstripe.enums.SetupIntentCancellationReason.choices",
        "StripeScheduledQueryRunStatus": "djstripe.enums.ScheduledQueryRunStatus.choices",
        "StripeSourceFlow": "djstripe.enums.SourceFlow.choices",
        "StripeSourceStatus": "djstripe.enums.SourceStatus.choices",
        "StripeSourceType": "djstripe.enums.SourceType.choices",
        "StripeLegacySourceType": "djstripe.enums.LegacySourceType.choices",
        "StripeRefundFailureReason": "djstripe.enums.RefundFailureReason.choices",
        "StripeRefundReason": "djstripe.enums.RefundReason.choices",
        "StripeRefundStatus": "djstripe.enums.RefundStatus.choices",
        "StripeSessionBillingAddressCollection": "djstripe.enums.SessionBillingAddressCollection.choices",
        "StripeSessionMode": "djstripe.enums.SessionMode.choices",
        "StripeSourceUsage": "djstripe.enums.SourceUsage.choices",
        "StripeSourceCodeVerificationStatus": "djstripe.enums.SourceCodeVerificationStatus.choices",
        "StripeSourceRedirectFailureReason": "djstripe.enums.SourceRedirectFailureReason.choices",
        "StripeSourceRedirectStatus": "djstripe.enums.SourceRedirectStatus.choices",
        "StripeSubmitTypeStatus": "djstripe.enums.SubmitTypeStatus.choices",
        "StripeSubscriptionScheduleEndBehavior": "djstripe.enums.SubscriptionScheduleEndBehavior.choices",
        "StripeSubscriptionScheduleStatus": "djstripe.enums.SubscriptionScheduleStatus.choices",
        "StripeSubscriptionStatus": "djstripe.enums.SubscriptionStatus.choices",
        "StripeTaxIdType": "djstripe.enums.TaxIdType.choices",
        "StripeUsageAction": "djstripe.enums.UsageAction.choices",
        "StripeWebhookEndpointStatus": "djstripe.enums.WebhookEndpointStatus.choices",
        "DjstripePaymentMethodType": "djstripe.enums.DjstripePaymentMethodType.choices",
        # end djstripe types
    },
    "TITLE": "printnanny-api-client",
    "DESCRIPTION": "Official API client library for printnanny.ai",
    "LICENSE": {"name": "AGPLv3"},
    "CONTACT": {
        "name": "Leigh Johnson",
        "email": "leigh@printnanny.ai",
        "url": "https://printnanny.ai",
    },
    "VERSION": API_VERSION,
    "PREPROCESSING_HOOKS": [
        "drf_spectacular.hooks.preprocess_exclude_path_format",
    ],
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

# channels
# ------------------------------------------------------------------------------
INSTALLED_APPS += [
    "channels",
]

APPEND_SLASH = True

# gcp
# ------------------------------------------------------------------------------
GCP_PROJECT_ID = env("GCP_PROJECT_ID", default="printnanny-sandbox")


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
# docs site
DOCS_SITE_URL = "https://printnanny.ai/docs/category/quick-start/"
DOCS_SITE__QUICKSTART = DOCS_SITE_URL

# dj-stripe
# ------------------------------------------------------------------------------
INSTALLED_APPS += ["djstripe"]
DJSTRIPE_USE_NATIVE_JSONFIELD = True
STRIPE_LIVE_MODE = env("STRIPE_LIVE_MODE", default=False)
# https://github.com/dj-stripe/dj-stripe/issues/1360
DJSTRIPE_WEBHOOK_SECRET = env("DJSTRIPE_WEBHOOK_SECRET", default="whsec_x")
STRIPE_TEST_PUBLIC_KEY = env("STRIPE_TEST_PUBLIC_KEY", default="pk_test_x")
STRIPE_TEST_SECRET_KEY = env("STRIPE_TEST_SECRET_KEY", default="sk_test_x")
STRIPE_LIVE_PUBLIC_KEY = env("STRIPE_LIVE_PUBLIC_KEY", default="pk_live_x")
STRIPE_LIVE_SECRET_KEY = env("STRIPE_LIVE_SECRET_KEY", default="sk_live_x")
DJSTRIPE_FOREIGN_KEY_TO_FIELD = "id"

STRIPE_PORTAL_URL = env(
    "STRIPE_PORTAL_URL",
    default="https://billing.stripe.com/p/login/test_aEU02ufgd2l26TSbII",
)

STRIPE_STARTER_PRODUCT_ID = env(
    "STRIPE_STARTER_PRODUCT_ID", default="prod_NITqAttqXx5JjJ"
)
STRIPE_SCALER_PRODUCT_ID = env(
    "STRIPE_SCALER_PRODUCT_ID", default="prod_NIXYlyaLbcpYxB"
)

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
    "PARTNER_3DGEEKS_ENABLED": [
        {"condition": "parameter", "value": "3dgeeks_enabled="}
    ],
    "MONTHLY_SUB": [{"condition": "parameter", "value": "monthly_sub=true"}],
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
MESSAGE_STORAGE = "django.contrib.messages.storage.cookie.CookieStorage"

# links
# ------------------------------------------------------------------------------
DISCORD_URL = "https://discord.gg/sf23bk2hPr"
ABOUT_URL = "https://blog.print-nanny.com/about"
GITHUB_ISSUE_URL = "https://github.com/bitsy-ai/octoprint-nanny-plugin/issues/new"

# drfpasswordless
# https://github.com/aaronn/django-rest-framework-passwordless
# ------------------------------------------------------------------------------
INSTALLED_APPS += ["drfpasswordless"]
PASSWORDLESS_AUTH = {
    "PASSWORDLESS_AUTH_TYPES": ["EMAIL"],
    "PASSWORDLESS_USER_MARK_EMAIL_VERIFIED": True,
    "PASSWORDLESS_EMAIL_NOREPLY_ADDRESS": "noreply@printnanny.ai",
    "PASSWORDLESS_EMAIL_PLAINTEXT_MESSAGE": "Enter this token to sign in: %s",
    "PASSWORDLESS_AUTH_PREFIX": "accounts/2fa-auth/",
    "PASSWORDLESS_VERIFY_PREFIX": "accounts/2fa-auth/verify/",
    "PASSWORDLESS_EMAIL_TOKEN_HTML_TEMPLATE_NAME": "drfpasswordless/passwordless_custom_token_email.html",
    "PASSWORDLESS_EMAIL_CALLBACK": "print_nanny_webapp.drfpasswordless.utils.send_email_with_callback_token",
    "PASSWORDLESS_EMAIL_SUBJECT": "[PrintNanny] Your temporary login code",
}

# internal PRINTNANNY_ vars
# ------------------------------------------------------------------------------
PRINTNANNY_ENV = env("PRINTNANNY_ENV", default="sandbox")

# posthog
# ------------------------------------------------------------------------------
POSTHOG_API_KEY = env("POSTHOG_API_KEY", default=None)
if POSTHOG_API_KEY:
    posthog.project_api_key = POSTHOG_API_KEY

# corsheaders
# see also: corsheaders.middleware.CorsMiddleware
# ------------------------------------------------------------------------------
INSTALLED_APPS += ["corsheaders"]
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://localhost:3001",
    "http://localhost:8080",
    "http://django:8080",
    "http://127.0.0.1:8000",
    f"http://{socket.gethostname()}:8080",
    f"http://{socket.gethostname()}:3000",
]

# Janus Cloud defaults
# in production, Janus Gateway is deployed to Cloud as an SFU and adressible over internet
# ------------------------------------------------------------------------------
JANUS_CLOUD_DOMAIN = env("JANUS_CLOUD_DOMAIN", default="janus")
JANUS_CLOUD_ADMIN_SECRET = env("JANUS_CLOUD_ADMIN_SECRET", default="debug")
JANUS_CLOUD_ADMIN_URL = env(
    "JANUS_CLOUD_ADMIN_URL", default=f"http://{JANUS_CLOUD_DOMAIN}:7088/admin"
)
JANUS_CLOUD_API_URL = env(
    "JANUS_CLOUD_API_URL", default=f"http://{JANUS_CLOUD_DOMAIN}:8088/janus"
)
JANUS_CLOUD_API_PORT: int = int(env("JANUS_CLOUD_API_PORT", default=8088))
JANUS_CLOUD_WS_URL = env(
    "JANUS_CLOUD_WS_URL", default=f"ws://{JANUS_CLOUD_DOMAIN}:8188"
)
JANUS_CLOUD_ADMIN_PORT: int = int(env("JANUS_CLOUD_ADMIN_PORT", default=7088))
JANUS_CLOUD_WS_PORT: int = int(env("JANUS_CLOUD_WS_PORT", default=8188))
JANUS_CLOUD_VIDEO_RTP_PORT_RANGE: List[int] = list(
    map(int, env.tuple("JANUS_CLOUD_VIDEO_RTP_PORT_RANGE", default=(20000, 20999)))
)
JANUS_CLOUD_DATA_RTP_PORT_RANGE: List[int] = list(
    map(int, env.tuple("JANUS_CLOUD_DATA_RTP_PORT_RANGE", default=(21000, 21999)))
)
JANUS_CLOUD_RTP_DOMAIN = env("JANUS_CLOUD_RTP_DOMAIN", default="aurora")

# general { admin_key: "..." } in janus.plugin.streaming.jcfg
# key must be provided in requests to create new mountpoints
JANUS_CLOUD_STREAMING_PLUGIN_ADMIN_KEY = env(
    "JANUS_CLOUD_STREAMING_PLUGIN_ADMIN_KEY", default="debugstreaming"
)

# Janus Edge defaults
# in production, Janus Gateway is deployed to edge device and addressible to LAN peers
# ------------------------------------------------------------------------------
JANUS_EDGE_ADMIN_PORT: int = int(env("JANUS_EDGE_ADMIN_PORT", default=7088))
JANUS_EDGE_VIDEO_RTP_PORT: int = int(env("JANUS_EDGE_VIDEO_RTP_PORT", default=5105))
JANUS_EDGE_DATA_RTP_PORT: int = int(env("JANUS_EDGE_DATA_RTP_PORT", default=6105))
JANUS_EDGE_API_PORT: int = int(env("JANUS_EDGE_API_PORT", default=8088))
JANUS_EDGE_WS_PORT: int = int(env("JANUS_EDGE_WS_PORT", default=8188))


# django-qr-code
# https://django-qr-code.readthedocs.io/en/latest/pages/README.html
# ------------------------------------------------------------------------------
INSTALLED_APPS += ["qr_code"]
SERVE_QR_CODE_IMAGE_PATH = "qr/"

# set build version
# ------------------------------------------------------------------------------
GIT_SHA = env("GIT_SHA", default="No GIT_SHA specified")

# OctoPrint
# ------------------------------------------------------------------------------

# base url for serving OctoPrint in PrintNanny OS
# see Nginx locations for ref:
# https://github.com/bitsy-ai/ansible-collection-printnanny/blob/main/roles/octoprint/templates/nginx.locations.j2
# Trailing slash should match Nginx location
OCTOPRINT_URL = "/octoprint/"
PRINTNANNY_OS_RELEASE_URL = "https://github.com/bitsy-ai/printnanny-os/releases"
PRINTNANNY_OS_UPGRADE_URL = (
    "https://github.com/bitsy-ai/printnanny-os/blob/main/docs/UPGRADE.MD"
)
# legacy octoprint plugin device registry
GCP_CLOUDIOT_OCTOPRINT_DEVICE_REGISTRY = env(
    "GCP_CLOUDIOT_DEVICE_REGISTRY_DEPRECATED", default="octoprint-devices"
)
# octoprint events topics/subscriptions
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

# default backup schedule for PrintNanny OS
PRINTNANNY_OS_DEFAULT_BACKUP_SCHEDULE = "0 0 * * 2"

# django-loginas
# https://github.com/skorokithakis/django-loginas
# ------------------------------------------------------------------------------
INSTALLED_APPS += ["loginas"]
LOGINAS_USERNAME_FIELD = "email"


# dj_rest_auth
# https://github.com/iMerica/dj-rest-auth
# https://dj-rest-auth.readthedocs.io/en/latest/index.html
# ------------------------------------------------------------------------------
INSTALLED_APPS += ["dj_rest_auth", "dj_rest_auth.registration"]

REST_AUTH = {
    "LOGIN_SERIALIZER": "print_nanny_webapp.dj_rest_auth.serializers.LoginSerializer",
    "USER_DETAILS_SERIALIZER": "print_nanny_webapp.users.api.serializers.UserSerializer",
    "REGISTER_SERIALIZER": "print_nanny_webapp.dj_rest_auth.serializers.RegisterSerializer",
}

# django-nats-nkeys
# https://github.com/bitsy-ai/django-nats-nkeys
# -------------------------------------------------------p-----------------------
INSTALLED_APPS += ["organizations", "django_nats_nkeys"]
NATS_APP_MODEL = "devices.PiNatsApp"
NATS_SERVER_URI = env("NATS_SERVER_URI", default="nats://nats:4222")
NATS_MQTT_BROKER_HOST = env("NATS_MQTT_BROKER_HOST", default="nats")
NATS_MQTT_BROKER_PORT = env("NATS_MQTT_BROKER_PORT", default=1883)

NATS_WS_URI = env("NATS_WS_URI", default="ws://nats:8443")
NATS_NKEYS_OPERATOR_NAME = env(
    "NATS_NKEYS_OPERATOR_NAME", default="PrintNannyDjangoOperator"
)
NATS_NSC_RETRY_MODE = "IDEMPOTENT"

# django-vite
# ------------------------------------------------------------------------------
DJANGO_VITE_STATIC_URL_PREFIX = ""
INSTALLED_APPS += ["django_vite"]
DJANGO_VITE_ASSETS_PATH = str(ROOT_DIR / "ui")

# ref: https://github.com/MrBin99/django-vite#notes
# Vite generates files with 8 hash digits
# http://whitenoise.evans.io/en/stable/django.html#WHITENOISE_IMMUTABLE_FILE_TEST


def immutable_file_test(path, url):
    # Match filename with 12 hex digits before the extension
    # e.g. app.db8f2edc0c8a.js
    return re.match(r"^.+\.[0-9a-f]{8,12}\..+$", url)


WHITENOISE_IMMUTABLE_FILE_TEST = immutable_file_test

# django-oauth-toolkit
# https://github.com/jazzband/django-oauth-toolkit
# ------------------------------------------------------------------------------
INSTALLED_APPS += ["oauth2_provider"]
OAUTH2_PROVIDER = {
    "OIDC_ENABLED": True,
    "OIDC_RSA_PRIVATE_KEY": os.environ.get("OIDC_RSA_PRIVATE_KEY"),
    # https://django-oauth-toolkit.readthedocs.io/en/latest/oidc.html#rotating-the-rsa-private-key
    # "OIDC_RSA_PRIVATE_KEYS_INACTIVE": [],
    # https://django-oauth-toolkit.readthedocs.io/en/latest/oidc.html#customizing-the-oidc-responses
    "OAUTH2_VALIDATOR_CLASS": "print_nanny_webapp.oauth2_provider.oauth2_validators.CustomOAuth2Validator",
    "SCOPES": {
        "openid": "OpenID Connect scope",
        "profile": "User profile scope",
        "email": "User email scope",
        "alerts:read": "Read scope for alert resources",
        "alerts:write": "Write scope for alert resources",
        "read": "Read scope",
        "write": "Write scope",
        "devices:read": "Read scope for Raspberry Pi and printer resources",
        "devices:write": "Write scope for Raspberry Pi and printer resources",
    },
    "PKCE_REQUIRED": False,
}

# firehose NATS app
# ------------------------------------------------------------------------------
NATS_FIREHOSE_ACCOUNT_NAME = "firehose"
NATS_FIREHOSE_SUBJECT = "pi.>"
NATS_FIREHOSE_NKEY = env(
    "NATS_FIREHOSE_NKEY", default="/app/.envs/.local/.firehose/nkey"
)

# Celery
# ------------------------------------------------------------------------------
INSTALLED_APPS += ["django_celery_beat"]

# Celery
# ------------------------------------------------------------------------------
if USE_TZ:
    # https://docs.celeryq.dev/en/stable/userguide/configuration.html#std:setting-timezone
    CELERY_TIMEZONE = TIME_ZONE
# https://docs.celeryq.dev/en/stable/userguide/configuration.html#std:setting-broker_url
CELERY_BROKER_URL = env("CELERY_BROKER_URL", default=REDIS_URL)
# https://docs.celeryq.dev/en/stable/userguide/configuration.html#std:setting-result_backend
CELERY_RESULT_BACKEND = CELERY_BROKER_URL
# https://docs.celeryq.dev/en/stable/userguide/configuration.html#result-extended
CELERY_RESULT_EXTENDED = True
# https://docs.celeryq.dev/en/stable/userguide/configuration.html#result-backend-always-retry
# https://github.com/celery/celery/pull/6122
CELERY_RESULT_BACKEND_ALWAYS_RETRY = True
# https://docs.celeryq.dev/en/stable/userguide/configuration.html#result-backend-max-retries
CELERY_RESULT_BACKEND_MAX_RETRIES = 10
# https://docs.celeryq.dev/en/stable/userguide/configuration.html#std:setting-accept_content
CELERY_ACCEPT_CONTENT = ["json"]
# https://docs.celeryq.dev/en/stable/userguide/configuration.html#std:setting-task_serializer
CELERY_TASK_SERIALIZER = "json"
# https://docs.celeryq.dev/en/stable/userguide/configuration.html#std:setting-result_serializer
CELERY_RESULT_SERIALIZER = "json"
# https://docs.celeryq.dev/en/stable/userguide/configuration.html#task-time-limit
# TODO: set to whatever value is adequate in your circumstances
CELERY_TASK_TIME_LIMIT = 5 * 60
# https://docs.celeryq.dev/en/stable/userguide/configuration.html#task-soft-time-limit
# TODO: set to whatever value is adequate in your circumstances
CELERY_TASK_SOFT_TIME_LIMIT = 60
# https://docs.celeryq.dev/en/stable/userguide/configuration.html#beat-scheduler
CELERY_BEAT_SCHEDULER = "django_celery_beat.schedulers:DatabaseScheduler"
# https://docs.celeryq.dev/en/stable/userguide/configuration.html#worker-send-task-events
CELERY_WORKER_SEND_TASK_EVENTS = True
# https://docs.celeryq.dev/en/stable/userguide/configuration.html#std-setting-task_send_sent_event
CELERY_TASK_SEND_SENT_EVENT = True
