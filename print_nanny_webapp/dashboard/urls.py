from django.urls import path, include

from .views import (
    ecommerce_dashboard_view, 
    crm_dashboard_view,
    analytics_dashboard_view,
    projects_dashboard_view,
    home_dashboard_view,
    video_dashboard_detail_view,
    video_dashboard_list_view
    )

app_name = "dashboard"


report_cards_urls = [
    path("/", video_dashboard_list_view, name="list"),
    path("/<slug:pk>", video_dashboard_detail_view, name="detail")

]

urlpatterns = [
    # path("crm", view=crm_dashboard_view, name="crm"),
    # path("analytics", view=analytics_dashboard_view, name="analytics"),
    # path("projects", view=projects_dashboard_view, name="projects"),
    path("", view=home_dashboard_view, name="home"),
    # path("demo", view=home_dashboard_view, name="demo"),
    path("report-cards", include((report_cards_urls,app_name), namespace="report-cards")),

    path("", view=home_dashboard_view, name="ecommerce"),

]
