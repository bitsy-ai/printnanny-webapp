from django.urls import path

from .views import (
    ecommerce_dashboard_view, 
    crm_dashboard_view,
    analytics_dashboard_view,
    projects_dashboard_view,
    )

app_name = "dashboard"
urlpatterns = [
    path("crm", view=crm_dashboard_view, name="crm"),
    path("analytics", view=analytics_dashboard_view, name="analytics"),
    path("projects", view=projects_dashboard_view, name="projects"),
    path("", view=ecommerce_dashboard_view, name="ecommerce"),
]
