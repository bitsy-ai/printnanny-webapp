import logging

from django.contrib.auth.mixins import LoginRequiredMixin
from django.apps import apps
from django.views.generic.list import MultipleObjectMixin
from django.views.generic import DetailView, DeleteView
from django.views.generic.base import TemplateView
from print_nanny_webapp.devices.models import Device

Device = apps.get_model("devices", "Device")
logger = logging.getLogger(__name__)


class ReleaseListView(TemplateView):
    template_name = "releases/releases-list.html"


class DeviceDeleteView(DeleteView, DetailView):
    template_name = "devices/delete-form.html"
    success_url = "/dashboard"
    model = Device


class DeviceVideoView(DetailView, LoginRequiredMixin):
    template_name = "device-video.html"
    model = Device


class DeviceDetailView(DetailView, LoginRequiredMixin):
    model = Device
    template_name = "devices/device-detail.html"
    paginate_by = 10

    # TODO implement reverse for events using MultipleObjectMixin
    # def get_context_data(self, **kwargs):
    #     tasks = self.get_object().events.all()
    #     context = super().get_context_data(object_list=tasks, **kwargs)
    #     return context


class DeviceWelcomeView(TemplateView, LoginRequiredMixin):
    template_name = "device-welcome.html"


class DeviceWelcomeDetailView(DetailView, LoginRequiredMixin):
    model = Device
    template_name = "device-welcome.html"
    paginate_by = 10
