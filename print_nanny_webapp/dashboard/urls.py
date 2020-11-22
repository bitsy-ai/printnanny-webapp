from django.urls import path

from .views import (
    ecommerce_dashboard_view, 
    crm_dashboard_view,
    analytics_dashboard_view,
    projects_dashboard_view,
    home_dashboard_view
    )

app_name = "dashboard"
urlpatterns = [
    path("crm", view=crm_dashboard_view, name="crm"),
    path("analytics", view=analytics_dashboard_view, name="analytics"),
    path("projects", view=projects_dashboard_view, name="projects"),
    path("dashboard", view=home_dashboard_view, name="home"),
    path("demo", view=home_dashboard_view, name="demo"),
    path("timelapse", view=home_dashboard_view, name="timelapse"),

    path("", view=home_dashboard_view, name="ecommerce"),

]
