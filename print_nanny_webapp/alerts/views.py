import logging
from django.shortcuts import render
from django.http import HttpResponseRedirect

from print_nanny_webapp.utils.multiform import MultiFormsView, BaseMultipleFormsView
from print_nanny_webapp.dashboard.views import DashboardView
from print_nanny_webapp.remote_control.models import OctoPrintDevice
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
# from .forms import (
#     ProgressAlertSettingsForm,
#     CommandAlertSettingsForm,
#     DiscordMethodSettingsForm,
# )
from .models import (
    Alert,
    # ProgressAlertSettings,
    # RemoteControlCommandAlertSettings,
    # DiscordMethodSettings,
)

logger = logging.getLogger(__name__)

from print_nanny_webapp.partners.models import GeeksToken

class AlertSettingsView(DashboardView, MultiFormsView):
    pass

# class AlertSettingsView(DashboardView, MultiFormsView):

#     success_url = "/alerts/settings"
#     form_classes = {
#         "progress": ProgressAlertSettingsForm,
#         "command": CommandAlertSettingsForm,
#         "discord": DiscordMethodSettingsForm,
#     }
#     template_name = "alerts/settings.html"

#     def create_progress_form(self, **kwargs):
#         instance, created = ProgressAlertSettings.objects.get_or_create(
#             user=self.request.user,
#         )
#         if instance is not None:
#             return ProgressAlertSettingsForm(instance=instance, **kwargs)
#         else:
#             return ProgressAlertSettingsForm(**kwargs)

#     def progress_form_valid(self, form):

#         obj = form.save(commit=False)
#         obj.user = self.request.user
#         obj.alert_type = Alert.AlertTypeChoices.PROGRESS
#         obj.save()

#         success_url = self.get_success_url()
#         return HttpResponseRedirect(success_url)

#     # TODO combine defect, end, progress events into PrintSessionAlert subtypes
#     # def create_defect_form(self, **kwargs):
#     #     instance, created = DefectAlertSettings.objects.get_or_create(
#     #         user=self.request.user,
#     #     )
#     #     if instance is not None:
#     #         return DefectAlertSettingsForm(instance=instance, **kwargs)
#     #     else:
#     #         return DefectAlertSettingsForm(**kwargs)

#     # def defect_form_valid(self, form):
#     #     form.user = self.request.user
#     #     form.alert_type = Alert.AlertTypeChoices.DEFECT
#     #     form.save()

#     #     success_url = self.get_success_url()
#     #     return HttpResponseRedirect(success_url)

#     def create_discord_form(self, **kwargs):
#         instance, created = DiscordMethodSettings.objects.get_or_create(
#             user=self.request.user,
#         )
#         if instance is not None:
#             return DiscordMethodSettingsForm(instance=instance, **kwargs)
#         else:
#             return DiscordMethodSettingsForm(**kwargs)

#     def discord_form_valid(self, form):
#         obj = form.save(commit=False)

#         obj.user = self.request.user
#         obj.method = Alert.AlertMethodChoices.DISCORD
#         obj.save()

#         success_url = self.get_success_url()
#         return HttpResponseRedirect(success_url)

#     def create_command_form(self, **kwargs):
#         instance, created = RemoteControlCommandAlertSettings.objects.get_or_create(
#             user=self.request.user,
#         )
#         if instance is not None:
#             return CommandAlertSettingsForm(instance=instance, **kwargs)
#         else:
#             return CommandAlertSettingsForm(**kwargs)

#     def command_form_valid(self, form):
#         form.user = self.request.user
#         form.alert_type = Alert.AlertTypeChoices.COMMAND
#         form.save()

#         success_url = self.get_success_url()
#         return HttpResponseRedirect(success_url)

#     def get_context_data(self, *args, **kwargs):
#         if kwargs.get("forms") is None:
#             tokens = GeeksToken.objects.filter(user=self.request.user)
#             form_classes = self.get_form_classes()
#             forms = self.get_forms(form_classes)
#             context = super().get_context_data(forms=forms, tokens=tokens, **kwargs)
#         else:
#             context = super().get_context_data(*args, **kwargs)
#         return context


class AlertListView(DashboardView):

    template_name = "alerts/list.html"
