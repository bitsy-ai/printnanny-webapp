from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path, re_path
from django.views import defaults as default_views
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from drf_spectacular.views import (
    SpectacularJSONAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

from anymail.webhooks.mailgun import (
    MailgunTrackingWebhookView,
    MailgunInboundWebhookView,
)

# non-API urls
# front-end routes should be registeredin ui/routes/index.ts, not here
# this section is for backend urls that aren't part of the REST API, for example health pages and admin panel
urlpatterns = [
    re_path(r"^health/", include("health_check.urls"), name="health"),
    # Django Admin, use {% url 'admin:index' %}
    # django-loginas urls must be defined before admin.site.urls
    path(settings.ADMIN_URL, include("loginas.urls")),
    path(settings.ADMIN_URL, admin.site.urls),
    path("accounts/", include("allauth.urls")),
    re_path(r"^invitations/", include("invitations.urls", namespace="invitations")),
    path("", include("qr_code.urls", namespace="qr_code")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += (path("stripe/", include("djstripe.urls", namespace="djstripe")),)

urlpatterns += [
    path("o/", include("oauth2_provider.urls", namespace="oauth2_provider")),
]


if settings.DEBUG:
    # Static file serving when using Gunicorn + Uvicorn for local web socket development
    urlpatterns += staticfiles_urlpatterns()

# API URLS

# https://drf-spectacular.readthedocs.io/en/latest/blueprints.html
# do not remove the following line!

urlpatterns += [
    # API base urls
    path("api/", include("config.api_router")),
    # OpenAPI Schema
    path("api/schema/", SpectacularJSONAPIView.as_view(), name="schema"),
    path("api/accounts/", include("dj_rest_auth.urls")),
    path("api/accounts/registration/", include("dj_rest_auth.registration.urls")),
    # OpenAPI UIs
    path(
        "api/schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/schema/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
    path("", include("django_prometheus.urls")),
    # exclude anymail webhook from csrf checks
    re_path(
        r"^anymail/mailgun/tracking/$",
        csrf_exempt(MailgunTrackingWebhookView.as_view()),
        name="mailgun_tracking_webhook",
    ),
    re_path(
        r"^anymail/mailgun/inbound(_mime)?/$",
        csrf_exempt(MailgunInboundWebhookView.as_view()),
        name="mailgun_inbound_webhook",
    ),
    # https://github.com/aaronn/django-rest-framework-passwordless
    path("", include("print_nanny_webapp.drfpasswordless.urls")),
    # pass to front-end
    re_path(r"^.*$", TemplateView.as_view(template_name="index.j2")),
    # this url is used to generate password reset email content
    re_path(
        r"^password-reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,32})/$",
        TemplateView.as_view(template_name="index.j2"),
        name="password_reset_confirm",
    ),
    # this url is used to generate account confirmation email content
    re_path(
        r"^account-confirm-email/(?P<key>[-:\w]+)/$",
        TemplateView.as_view(template_name="index.j2"),
        name="account_confirm_email",
    ),
]


if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns += [path("__debug__/", include(debug_toolbar.urls))]
