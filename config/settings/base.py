"""
Base settings to build other settings files upon.
"""
from typing import List
from pathlib import Path
import os
import socket
import environ
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
    # "print_nanny_webapp.alerts.apps.AlertsConfig",
    "print_nanny_webapp.devices.apps.DevicesConfig",
    # "print_nanny_webapp.partners.apps.PartnersConfig",
    # "print_nanny_webapp.remote_control.apps.RemoteControlConfig",
    # "print_nanny_webapp.telemetry.apps.TelemetryConfig",
    "print_nanny_webapp.users.apps.UsersConfig",
    "print_nanny_webapp.surveys.apps.SurveysConfig",
    "print_nanny_webapp.octoprint.apps.OctoprintConfig",
    "print_nanny_webapp.subscriptions.apps.SubscriptionsConfig",
    "print_nanny_webapp.shop.apps.ShopConfig",
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
    "django_prometheus.middleware.PrometheusBeforeMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "print_nanny_webapp.utils.middleware.DomainRedirectMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
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

# @TODO rm these staticfiles dirs
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
ANYMAIL = {
    "MAILGUN_API_KEY": env("MAILGUN_API_KEY"),
    "MAILGUN_SENDER_DOMAIN": env("MAILGUN_DOMAIN"),
    "MAILGUN_API_URL": env("MAILGUN_API_URL", default="https://api.mailgun.net/v3"),
    # "WEBHOOK_SECRET": env("MAILGUN_WEBHOOK_SECRET")
}

# Discord
# ------------------------------------------------------------------------------
DISCORD_TOKEN = env("DISCORD_TOKEN", default="")
DISCORD_NEW_SIGNUP_WEBHOOK = env("DISCORD_NEW_SIGNUP_WEBHOOK", default=None)


# ADMIN
# ------------------------------------------------------------------------------
# Django Admin URL.
ADMIN_URL = "admin/"
# https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = [("""Leigh Johnson""", "leigh@printnanny.ai")]
# https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS
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

API_VERSION = open("version.txt", "r").read()

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
        "OsEdition": "print_nanny_webapp.devices.enum.OsEdition",
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
        # begin OctoPrint polymorphic event types
        "OctoPrintPrintJobStatusType": "print_nanny_webapp.octoprint.enum.OctoPrintPrintJobStatusType",
        "OctoPrintServerStatusType": "print_nanny_webapp.octoprint.enum.OctoPrintServerStatusType",
        "OctoPrintPrinterStatusType": "print_nanny_webapp.octoprint.enum.OctoPrintPrinterStatusType",
        "OctoPrintClientStatusType": "print_nanny_webapp.octoprint.enum.OctoPrintClientStatusType",
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

# django-invitations
# ------------------------------------------------------------------------------
INSTALLED_APPS += [
    "invitations",
]
ACCOUNT_ADAPTER = "invitations.models.InvitationsAdapter"
INVITATIONS_ADAPTER = ACCOUNT_ADAPTER
INVITATIONS_INVITATION_ONLY = False
INVITATIONS_INVITATION_EXPIRY = 30
INVITATIONS_EMAIL_SUBJECT_PREFIX = "[PrintNanny]"
INVITATIONS_ACCEPT_INVITE_AFTER_SIGNUP = True

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
DOCS_SITE_URL = "https://docs.printnanny.ai/docs/category/quick-start/"
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

STRIPE_PORTAL_URL = env("STRIPE_PORTAL_URL", default="")

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
    "PASSWORDLESS_EMAIL_NOREPLY_ADDRESS": "noreply@print-nanny.com",
    "PASSWORDLESS_EMAIL_PLAINTEXT_MESSAGE": "Enter this token to sign in: %s",
    "PASSWORDLESS_AUTH_PREFIX": "accounts/2fa-auth/",
    "PASSWORDLESS_VERIFY_PREFIX": "accounts/2fa-auth/verify/",
}

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
    "http://localhost:3000",
    "http://localhost:3001",
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    f"http://{socket.gethostname()}:8000",
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
REST_AUTH_SERIALIZERS = {
    "LOGIN_SERIALIZER": "print_nanny_webapp.dj_rest_auth.serializers.LoginSerializer",
    "USER_DETAILS_SERIALIZER": "print_nanny_webapp.users.api.serializers.UserSerializer",
}
REST_AUTH_REGISTER_SERIALIZERS = {
    "REGISTER_SERIALIZER": "print_nanny_webapp.dj_rest_auth.serializers.RegisterSerializer"
}

# django-nats-nkeys
# https://github.com/bitsy-ai/django-nats-nkeys
# ------------------------------------------------------------------------------
INSTALLED_APPS += ["organizations", "django_nats_nkeys"]
NATS_APP_MODEL = "devices.PiNatsApp"
NATS_SERVER_URI = env("NATS_SERVER_URI", default="nats://nats:4222")
NATS_WS_URI = env("NATS_WS_URI", default="ws://nats:8443")
NATS_NKEYS_OPERATOR_NAME = env(
    "NATS_NKEYS_OPERATOR_NAME", default="PrintNannyDjangoOperator"
)
NATS_NSC_RETRY_MODE = "IDEMPOTENT"
