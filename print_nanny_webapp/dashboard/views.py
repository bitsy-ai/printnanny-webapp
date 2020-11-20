from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import TemplateView


User = get_user_model()

class DashboardView(LoginRequiredMixin, TemplateView):
    pass

ecommerce_dashboard_view = DashboardView.as_view(template_name="dashboard/ecommerce.html")
crm_dashboard_view = DashboardView.as_view(template_name="dashboard/crm.html")
analytics_dashboard_view = DashboardView.as_view(template_name="dashboard/analytics.html")
projects_dashboard_view = DashboardView.as_view(template_name="dashboard/projects.html")


class HomeDashboardView(LoginRequiredMixin, TemplateView):

    model = User
    template_name = 'dashboard/home.html'
    def get_object(self):
        token, created = Token.objects.get_or_create(user=self.request.user)
        self.request.user.token = token
        return self.request.user

home_dashboard_view = HomeDashboardView.as_view()