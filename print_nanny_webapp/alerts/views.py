import logging
from django.shortcuts import render
from django.http import  HttpResponseRedirect

from print_nanny_webapp.utils.multiform import MultiFormsView, BaseMultipleFormsView
from print_nanny_webapp.dashboard.views import DashboardView
from .forms import (ProgressAlertSettingsForm, DefectAlertSettingsForm, CommandAlertSettingsForm)
from .models import Alert, ProgressAlertSettings, DefectAlertSettings, RemoteControlCommandAlertSettings
logger = logging.getLogger(__name__)

class AlertSettingsView(DashboardView, MultiFormsView):

    success_url = "/alerts/settings"
    form_classes = {
        "progress": ProgressAlertSettingsForm,

        "defect": DefectAlertSettingsForm,

        "command": CommandAlertSettingsForm,
    }
    template_name = "alerts/settings.html"


    def create_progress_form(self, **kwargs):
        instance, created = ProgressAlertSettings.objects.get_or_create(
            user=self.request.user,
        )
        if instance is not None:
            return ProgressAlertSettingsForm(instance=instance, **kwargs)
        else:
            return ProgressAlertSettingsForm(**kwargs)

    def progress_form_valid(self, form):

        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.alert_type=Alert.AlertTypeChoices.PROGRESS
        obj.save()

        success_url = self.get_success_url()
        return HttpResponseRedirect(success_url)
    

    def create_defect_form(self, **kwargs):
        instance, created = DefectAlertSettings.objects.get_or_create(
            user=self.request.user,
        )
        if instance is not None:
            return DefectAlertSettingsForm(instance=instance, **kwargs)
        else:
            return DefectAlertSettingsForm(**kwargs)

    def defect_form_valid(self, form):
        form.user = self.request.user
        form.alert_type=Alert.AlertTypeChoices.DEFECT
        form.save()


        success_url = self.get_success_url()
        return HttpResponseRedirect(success_url)

    def create_command_form(self, **kwargs):
        instance, created = RemoteControlCommandAlertSettings.objects.get_or_create(
            user=self.request.user,
        )
        if instance is not None:
            return CommandAlertSettingsForm(instance=instance, **kwargs)
        else:
            return CommandAlertSettingsForm(**kwargs)


    def command_form_valid(self, form):
        form.user = self.request.user
        form.alert_type=Alert.AlertTypeChoices.COMMAND
        form.save()

        success_url = self.get_success_url()
        return HttpResponseRedirect(success_url)

    def get_context_data(self, *args, **kwargs):
        if kwargs.get('forms') is None:
            form_classes = self.get_form_classes()
            forms = self.get_forms(form_classes)
            context = super().get_context_data(forms=forms, **kwargs)
        else:
            context = super().get_context_data(*args, **kwargs)
        return context
class AlertListView(DashboardView):

    template_name = "alerts/list.html"

