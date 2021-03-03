import logging

from print_nanny_webapp.dashboard.views import DashboardView

logger = logging.getLogger(__name__)

class SubscriptionsListView(DashboardView):
    template_name = "subscriptions/list.html"
