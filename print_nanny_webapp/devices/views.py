import logging

from django.shortcuts import render
from django.apps import apps
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from print_nanny_webapp.devices.models import Device
from django.views.generic.detail import BaseDetailView

Device = apps.get_model("devices", "Device")
logger = logging.getLogger(__name__)


class DeviceListView(LoginRequiredMixin, TemplateView):
    template_name = "devices/devices-list.html"

    def get_context_data(self, *args, **kwargs):
        context = super(DeviceListView, self).get_context_data(**kwargs)

        context["user"] = self.request.user

        context["devices"] = Device.objects.filter(user=self.request.user).all()
        logger.info(context)

        return context


class DeviceDetailView(LoginRequiredMixin, BaseDetailView):
    model = Device
    template_name = "devices/device-detail.html"
