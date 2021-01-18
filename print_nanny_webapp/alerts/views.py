from django.shortcuts import render

from print_nanny_webapp.utils.multiform import MultiFormsView, BaseMultipleFormsView
from print_nanny_webapp.dashboard.views import DashboardView



class AlertSettingsView(DashboardView):

    template_name = "alerts/settings.html"

class AlertListView(DashboardView):

    template_name = "alerts/list.html"

