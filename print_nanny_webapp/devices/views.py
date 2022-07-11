import toml
import json
import logging

from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, DeleteView, CreateView
from django.views import View
from django.http import HttpResponse
from print_nanny_webapp.devices.models import Device, DeviceSettings
from print_nanny_webapp.utils.api.service import get_api_config
from print_nanny_webapp.utils.multiform import MultiFormsView
from .api.serializers import ConfigSerializer
from .forms import DeviceSettingsForm
from print_nanny_webapp.octoprint.forms import OctoPrintSettingsForm

logger = logging.getLogger(__name__)


class DeviceDeleteView(DeleteView, DetailView):
    template_name = "devices/delete-form.html"
    success_url = "/dashboard"
    model = Device


class DeviceVideoView(LoginRequiredMixin, DetailView):
    template_name = "device-video.html"
    model = Device


class DeviceDetailView(LoginRequiredMixin, DetailView):
    model = Device
    template_name = "devices/device-detail.html"


class DeviceSettingsView(LoginRequiredMixin, DetailView, MultiFormsView):
    model = DeviceSettings
    fields = ["octoprint_enabled", "cloud_video_enabled", "telemetry_enabled"]
    template_name = "device-settings.html"
    form_classes = {
        "device_settings": DeviceSettingsForm,
        "octoprint_settings": OctoPrintSettingsForm,
    }

    def device_settings_form_valid(self, form):
        form.save()
        success_url = self.get_success_url()
        return HttpResponseRedirect(success_url)

    def octoprint_settings_form_valid(self, form):
        form.save()
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


class DeviceCreateView(LoginRequiredMixin, CreateView):
    template_name = "device-create.html"
    success_url = "/dashboard"
    # form_class = DeviceCreateForm
    model = Device
    fields = ("hostname",)

    def form_valid(self, form):
        """
        Save form with request.user data
        """

        obj = form.save(commit=False)
        # TODO remove hard-coded .local and replace with Wireguard fqdn
        obj.fqdn = f"{obj.hostname}.local"
        obj.user = self.request.user
        obj.save()
        self.object = obj

        success_url = self.get_success_url()
        return HttpResponseRedirect(success_url)


class ConfigDownloadView(LoginRequiredMixin, View):
    model = Device
    slug_field = "id"

    def get(self, request, pk=None):
        device = Device.objects.get(id=pk)
        api = get_api_config(request, device.user)
        instance = dict(device=device, api=api)

        serializer = ConfigSerializer(instance=instance)
        # use .toml for user-facing configs
        # I'm sure there's a better way to serialize than DRF to_representation() -> JSON string -> Dict -> TOML string
        json_str = json.dumps(serializer.data)
        toml_str = toml.dumps(json.loads(json_str))
        response = HttpResponse(toml_str, content_type="application/toml")
        response["Content-Disposition"] = "attachment; filename=printnanny.toml"
        return response
