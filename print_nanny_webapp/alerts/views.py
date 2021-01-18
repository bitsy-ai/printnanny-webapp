import logging
from django.shortcuts import render

from print_nanny_webapp.utils.multiform import MultiFormsView, BaseMultipleFormsView
from print_nanny_webapp.dashboard.views import DashboardView
from .forms import (ProgressAlertSettingsForm, DefectAlertSettingsForm, CommandAlertSettingsForm)

logger = logging.getLogger(__name__)

class AlertSettingsView(DashboardView, MultiFormsView):

    # AlertSettings.AlertMethodChoices
    form_classes = {
        "progress__ui": ProgressAlertSettingsForm,
        "progress__email": ProgressAlertSettingsForm,

        "defect__ui": DefectAlertSettingsForm,
        "defect__email": DefectAlertSettingsForm,

        "command__ui": CommandAlertSettingsForm,
        "command__email": CommandAlertSettingsForm
    }

    def progress__ui_form_valid(self):
        pass

    def progress__email_form_valid(self):
        pass
    
    def defect__ui_form_valid(self):
        pass
    def defect__email_form_valid(self):
        pass
    def command__ui_form_valid(self):
        pass
    def command__email_form_valid(self):
        pass

    template_name = "alerts/settings.html"

    def get_context_data(self, *args, **kwargs):
        form_classes = self.get_form_classes()
        forms = self.get_forms(form_classes)
        context = super().get_context_data(forms=forms, **kwargs)
        return context
class AlertListView(DashboardView):

    template_name = "alerts/list.html"

