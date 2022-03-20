import logging

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, DeleteView
from django.views.generic.base import TemplateView
from print_nanny_webapp.devices.models import Device

logger = logging.getLogger(__name__)


class ReleaseListView(TemplateView):
    template_name = "releases/releases-list.html"


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
    paginate_by = 10

    # TODO implement reverse for events using MultipleObjectMixin
    # def get_context_data(self, **kwargs):
    #     tasks = self.get_object().events.all()
    #     context = super().get_context_data(object_list=tasks, **kwargs)
    #     return context


class DeviceWelcomeView(LoginRequiredMixin, TemplateView):
    template_name = "device-welcome.html"


class DeviceWelcomeDetailView(LoginRequiredMixin, DetailView):
    model = Device
    template_name = "device-welcome.html"
    paginate_by = 10
