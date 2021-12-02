import logging

from django.apps import apps
from django.urls import reverse
from django.views.generic.list import MultipleObjectMixin
from django.views.generic import CreateView, DetailView, DeleteView
from print_nanny_webapp.devices.models import Device

from print_nanny_webapp.dashboard.views import DashboardView
from .services import generate_zipped_license_response

Device = apps.get_model("devices", "Device")
logger = logging.getLogger(__name__)


class DeviceCreateView(CreateView):
    template_name = "devices/create-form.html"
    model = Device
    fields = ["hostname", "release_channel"]

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if kwargs["instance"] is None:
            kwargs["instance"] = self.model()
        kwargs["instance"].user = self.request.user
        return kwargs

    def get_success_url(self):
        return reverse("devices:detail", args=(self.object.id,))


class DeviceDeleteView(DeleteView, DetailView):
    template_name = "devices/delete-form.html"
    success_url = "/devices"
    model = Device


class DeviceListView(DashboardView):
    template_name = "devices/devices-list.html"

    def get_context_data(self, *args, **kwargs):
        context = super(DeviceListView, self).get_context_data(**kwargs)

        context["user"] = self.request.user

        context["devices"] = Device.objects.filter(user=self.request.user).all()
        logger.info(context)

        return context


class DeviceDetailView(DetailView, MultipleObjectMixin):
    model = Device
    template_name = "devices/device-detail.html"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        system_tasks = self.get_object().system_tasks.all()
        context = super().get_context_data(object_list=system_tasks, **kwargs)
        return context


class DeviceLicenseDownload(DetailView):
    model = Device

    def get(self, request, *args, **kwargs):
        device = Device.objects.get(pk=kwargs["pk"])

        return generate_zipped_license_response(device, request)
