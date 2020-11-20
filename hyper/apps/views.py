from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import TemplateView

User = get_user_model()

class AppsView(LoginRequiredMixin, TemplateView):
    pass

# calendar
apps_calendar_calendar_view = AppsView.as_view(template_name="apps/calendar/calendar.html")

#chat
apps_chat_chat_view = AppsView.as_view(template_name="apps/chat/chat.html")

# ecommerce
apps_ecommerce_checkout_view = AppsView.as_view(template_name="apps/ecommerce/checkout.html")
apps_ecommerce_customers_view = AppsView.as_view(template_name="apps/ecommerce/customers.html")
apps_ecommerce_orders_details_view = AppsView.as_view(template_name="apps/ecommerce/orders-details.html")
apps_ecommerce_orders_view = AppsView.as_view(template_name="apps/ecommerce/orders.html")
apps_ecommerce_products_details_view = AppsView.as_view(template_name="apps/ecommerce/products-details.html")
apps_ecommerce_products_view = AppsView.as_view(template_name="apps/ecommerce/products.html")
apps_ecommerce_sellers_view = AppsView.as_view(template_name="apps/ecommerce/sellers.html")
apps_ecommerce_shopping_cart_view = AppsView.as_view(template_name="apps/ecommerce/shopping-cart.html")

# email
apps_email_indox_view = AppsView.as_view(template_name="apps/email/inbox.html")
apps_email_read_view = AppsView.as_view(template_name="apps/email/read.html")

# projects
apps_projects_add_view = AppsView.as_view(template_name="apps/projects/add.html")
apps_projects_details_view = AppsView.as_view(template_name="apps/projects/details.html")
apps_projects_gantt_view = AppsView.as_view(template_name="apps/projects/gantt.html")
apps_projects_list_view = AppsView.as_view(template_name="apps/projects/list.html")

# social
apps_social_feed_view = AppsView.as_view(template_name="apps/social/feed.html")

# tasks
apps_tasks_details_view = AppsView.as_view(template_name="apps/tasks/details.html")
apps_tasks_kanban_view = AppsView.as_view(template_name="apps/tasks/kanban.html")
apps_tasks_list_view = AppsView.as_view(template_name="apps/tasks/list.html")
