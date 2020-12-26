from django.urls import path

from .views import (
    apps_calendar_calendar_view,
    apps_chat_chat_view,
    apps_ecommerce_checkout_view,
    apps_ecommerce_customers_view,
    apps_ecommerce_orders_details_view,
    apps_ecommerce_orders_view,
    apps_ecommerce_products_details_view,
    apps_ecommerce_products_view,
    apps_ecommerce_sellers_view,
    apps_ecommerce_shopping_cart_view,
    apps_email_indox_view,
    apps_email_read_view,
    apps_projects_add_view,
    apps_projects_details_view,
    apps_projects_gantt_view,
    apps_projects_list_view,
    apps_social_feed_view,
    apps_tasks_details_view,
    apps_tasks_kanban_view,
    apps_tasks_list_view,
    apps_coming_soon_view,
)


app_name = "apps"
urlpatterns = [
    # calendar
    path("calendar", view=apps_calendar_calendar_view, name="calendar"),
    # chat
    path("chat", view=apps_chat_chat_view, name="chat"),
    # ecommerce
    path(
        "ecommerce/checkout",
        view=apps_ecommerce_checkout_view,
        name="ecommerce.checkout",
    ),
    path(
        "ecommerce/customers",
        view=apps_ecommerce_customers_view,
        name="ecommerce.customers",
    ),
    path(
        "ecommerce/orders-details",
        view=apps_ecommerce_orders_details_view,
        name="ecommerce.orders-details",
    ),
    path("ecommerce/orders", view=apps_ecommerce_orders_view, name="ecommerce.orders"),
    path(
        "ecommerce/products-details",
        view=apps_ecommerce_products_details_view,
        name="ecommerce.products-details",
    ),
    path(
        "ecommerce/products",
        view=apps_ecommerce_products_view,
        name="ecommerce.products",
    ),
    path(
        "ecommerce/sellers", view=apps_ecommerce_sellers_view, name="ecommerce.sellers"
    ),
    path(
        "ecommerce/shopping-cart",
        view=apps_ecommerce_shopping_cart_view,
        name="ecommerce.shopping-cart",
    ),
    # email
    path("email/indox", view=apps_email_indox_view, name="email.indox"),
    path("email/read", view=apps_email_read_view, name="email.read"),
    # projects //TODO
    path("projects/add", view=apps_projects_add_view, name="projects.add"),
    path("projects/details", view=apps_projects_details_view, name="projects.details"),
    path("projects/gantt", view=apps_projects_gantt_view, name="projects.gantt"),
    path("projects/list", view=apps_projects_list_view, name="projects.list"),
    # social
    path("social/feed", view=apps_social_feed_view, name="social.feed"),
    # tasks
    path("tasks/details", view=apps_tasks_details_view, name="tasks.details"),
    path("tasks/kanban", view=apps_tasks_kanban_view, name="tasks.kanban"),
    path("tasks/list", view=apps_tasks_list_view, name="tasks.list"),
    # custom
    path(
        "coming-soon-remote-control",
        view=apps_coming_soon_view,
        name="coming-soon-remote-control",
    ),
    path(
        "coming-soon-print-library",
        view=apps_coming_soon_view,
        name="coming-soon-print-library",
    ),
    path(
        "coming-soon-webhooks", view=apps_coming_soon_view, name="coming-soon-webhooks"
    ),
    path(
        "coming-soon-webhooks", view=apps_coming_soon_view, name="coming-soon-webhooks"
    ),
]
