import logging

import tempfile
from django.http import Http404
from django.shortcuts import render
from django.apps import apps
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, FormView, CreateView, DetailView
from print_nanny_webapp.devices.models import Device
from django.views.generic.detail import BaseDetailView
from django.http import FileResponse

from print_nanny_webapp.dashboard.views import DashboardView
from .services import generate_zipped_license_file

Device = apps.get_model("devices", "Device")
logger = logging.getLogger(__name__)


class DeviceCreateView(CreateView):
    template_name = "devices/create-form.html"
    success_url = "/devices"
    model = Device
    fields = ["hostname", "release_channel"]

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if kwargs["instance"] is None:
            kwargs["instance"] = self.model()
        kwargs["instance"].user = self.request.user
        return kwargs


class DeviceListView(DashboardView):
    template_name = "devices/devices-list.html"

    def get_context_data(self, *args, **kwargs):
        context = super(DeviceListView, self).get_context_data(**kwargs)

        context["user"] = self.request.user

        context["devices"] = Device.objects.filter(user=self.request.user).all()
        logger.info(context)

        return context


class DeviceDetailView(DashboardView):
    model = Device
    template_name = "devices/device-detail.html"


class DeviceLicenseDownload(DetailView):
    model = Device

    def get(self, request, *args, **kwargs):
        device = Device.objects.get(pk=kwargs["pk"])

        with tempfile.TemporaryDirectory() as tmp:
            filename = generate_zipped_license_file(device, request, tmp)
            # some_file = self.model.objects.get(imported_file=filename)
            response = FileResponse(
                open(filename, "rb"), content_type="application/zip"
            )
            # https://docs.djangoproject.com/en/1.11/howto/outputting-csv/#streaming-large-csv-files
            response[
                "Content-Disposition"
            ] = 'attachment; filename="printnanny_license.zip"'
            return response
