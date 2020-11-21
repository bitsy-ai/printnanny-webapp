from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.apps import apps
from django.views.generic import TemplateView, DetailView
from rest_framework.authtoken.models import Token

User = get_user_model()
AlertMessage = apps.get_model('alerts', 'AlertMessage')

class DashboardView(LoginRequiredMixin, TemplateView):
    pass

ecommerce_dashboard_view = DashboardView.as_view(template_name="dashboard/ecommerce.html")
crm_dashboard_view = DashboardView.as_view(template_name="dashboard/crm.html")
analytics_dashboard_view = DashboardView.as_view(template_name="dashboard/analytics.html")
projects_dashboard_view = DashboardView.as_view(template_name="dashboard/projects.html")


class HomeDashboardView(LoginRequiredMixin, DetailView):

    model = User
    template_name = 'dashboard/home.html'
    def get_object(self):
        token, created = Token.objects.get_or_create(user=self.request.user)
        self.request.user.token = token
        self.request.user.active_alerts = self.request.user.alertmessage_set.filter(last_action=AlertMessage.ActionChoices.PENDING)
        return self.request.user

home_dashboard_view = HomeDashboardView.as_view()