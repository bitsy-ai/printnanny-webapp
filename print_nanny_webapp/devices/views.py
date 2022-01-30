from distutils.log import Log
import logging

from django.contrib.auth.mixins import LoginRequiredMixin
from django.apps import apps
from django.urls import reverse
from django.views.generic.list import MultipleObjectMixin
from django.views.generic import CreateView, DetailView, DeleteView
from django.views.generic.base import TemplateView
from print_nanny_webapp.devices.forms import CameraCreateForm
from print_nanny_webapp.devices.models import Device

from print_nanny_webapp.dashboard.views import DashboardView
from .forms import CameraCreateForm

Device = apps.get_model("devices", "Device")
Camera = apps.get_model("devices", "Camera")
logger = logging.getLogger(__name__)


class ReleaseListView(TemplateView):
    template_name = "releases/releases-list.html"


class DeviceDeleteView(DeleteView, DetailView):
    template_name = "devices/delete-form.html"
    success_url = "/devices"
    model = Device


class DeviceDetailView(DetailView, MultipleObjectMixin, LoginRequiredMixin):
    model = Device
    template_name = "devices/device-detail.html"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        tasks = self.get_object().tasks.all()
        context = super().get_context_data(object_list=tasks, **kwargs)
        return context


class DeviceWelcomeView(TemplateView, LoginRequiredMixin):
    template_name = "device-welcome.html"


class DeviceWelcomeDetailView(DetailView, LoginRequiredMixin):
    model = Device
    template_name = "device-welcome.html"
    paginate_by = 10
