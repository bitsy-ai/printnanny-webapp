from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path, re_path
from django.views import defaults as default_views
from django.views.generic import TemplateView
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.permissions import AllowAny
import django_prometheus
#from drf_yasg.views import get_schema_view
#from drf_yasg import openapi
from drf_spectacular.views import SpectacularJSONAPIView, SpectacularRedocView, SpectacularSwaggerView

#from config.api_schema import CustomOpenAPISchemaGenerator

# Webapp urls
urlpatterns = [
    path("", TemplateView.as_view(template_name="landing/landing.html"), name="home"),
    path(
        "about/", TemplateView.as_view(template_name="pages/about.html"), name="about"
    ),
    # Django Admin, use {% url 'admin:index' %}
    path(settings.ADMIN_URL, admin.site.urls),
    # User management
    #path("dashboard/", view=home_dashboard_view, name="dashboard"),
    path("users/", include("print_nanny_webapp.users.urls", namespace="users")),
    path("accounts/", include("allauth.urls")),
    # Your stuff: custom urls includes go here
    # hyper templates

    path("form/",
         include("print_nanny_webapp.form.urls", namespace="form"), ),
    path("pages/",
         include("print_nanny_webapp.pages.urls", namespace="pages"), ),
    path("apps/",
         include("print_nanny_webapp.apps.urls", namespace="apps"), ),
    path("components/",
         include("print_nanny_webapp.components.urls", namespace="components"), ),
    path("layouts/",
         include("print_nanny_webapp.layouts.urls", namespace="layouts"), ),
    path("",
         include("print_nanny_webapp.dashboard.urls", namespace="dashboard"), ),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    # Static file serving when using Gunicorn + Uvicorn for local web socket development
    urlpatterns += staticfiles_urlpatterns()

# API URLS

urlpatterns += [
    # API base url
    path("api/", include("config.api_router")),
    # DRF auth token
    path("api/auth-token/", obtain_auth_token),

    # OpenAPI Schema
    path('api/schema/', SpectacularJSONAPIView.as_view(), name='schema'),
    # OpenAPI UIs
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('', include('django_prometheus.urls')),
    path('anymail/', include('anymail.urls')),


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

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
