import logging
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages

from print_nanny_webapp.utils.multiform import MultiFormsView, BaseMultipleFormsView
from print_nanny_webapp.dashboard.views import DashboardView
from print_nanny_webapp.remote_control.models import OctoPrintDevice
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

from .models import (
    AlertSettings,
    AlertMessage
)

from print_nanny_webapp.alerts.tasks.alerts import AlertTask

logger = logging.getLogger(__name__)

from print_nanny_webapp.alerts.forms import (
    AlertSettingsForm,
    AlertMethodSettingsForm,
    AlertTestForm
)


class AlertSettingsView(DashboardView, MultiFormsView):

    success_url = "/alerts/settings"
    form_classes = {
        "event_settings": AlertSettingsForm,
        "alert_methods": AlertMethodSettingsForm,
        "test_alert": AlertTestForm
    }
    template_name = "alerts/settings.html"

    def test_alert_form_valid(self, *args, **kwargs):
        instance, created = AlertSettings.objects.get_or_create(
            user=self.request.user,
        )
        for alert_method in instance.alert_methods:
            alert_message = AlertMessage.objects.create(
                alert_method=alert_method,
                event_type=AlertMessage.AlertMessageType.TEST,
                user=instance.user,
            )
            task = AlertTask(alert_message)
            task.trigger_alert()     
        messages.success(self.request, 'Test alert was sent! Check your inbox.')
        return HttpResponseRedirect(self.request.path_info)

    def create_alert_methods_form(self, **kwargs):
        instance, created = AlertSettings.objects.get_or_create(
            user=self.request.user,
        )
        if instance is not None:
            return AlertMethodSettingsForm(instance=instance, **kwargs)
        else:
            return AlertMethodSettingsForm(**kwargs)

    def alert_methods_form_valid(self, form):

        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()

        success_url = self.get_success_url()
        return HttpResponseRedirect(success_url)

    def create_event_settings_form(self, **kwargs):
        instance, created = AlertSettings.objects.get_or_create(
            user=self.request.user,
        )
        if instance is not None:
            return AlertSettingsForm(instance=instance, **kwargs)
        else:
            return AlertSettingsForm(**kwargs)

    def event_settings_form_valid(self, form):

        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()

        success_url = self.get_success_url()
        return HttpResponseRedirect(success_url)

    def get_context_data(self, *args, **kwargs):
        # initialize form context if missing
        if kwargs.get("forms") is None:
            form_classes = self.get_form_classes()
            forms = self.get_forms(form_classes)
            context = super().get_context_data(forms=forms, **kwargs)
        else:
            context = super().get_context_data(*args, **kwargs)
        return context


class AlertListView(DashboardView):

    template_name = "alerts/list.html"
