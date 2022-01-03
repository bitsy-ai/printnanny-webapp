# from django.conf import settings
# EXTERNAL_AUTH = settings.get("EXTERNAL_AUTH", False, "@bool")
# if EXTERNAL_AUTH:
#     EXTERNAL_AUTH_MIDDLEWARE = ["django.contrib.auth.middleware.RemoteUserMiddleware"]
#     AUTHENTICATION_BACKENDS = ["django.contrib.auth.backends.RemoteUserBackend"]
#     REST_FRAMEWORK_AUTH = ("rest_framework.authentication.RemoteUserAuthentication",)
# else:
REST_FRAMEWORK_AUTH = ("rest_framework.authentication.BasicAuthentication",)

# fmt: off
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
] + [
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware"
]
MIDDLEWARE += [ 'allow_cidr.middleware.AllowCIDRMiddleware']
ALLOWED_CIDR_NETS = [
    '10.12.0.0/14',
    '10.16.0.0/20'
]