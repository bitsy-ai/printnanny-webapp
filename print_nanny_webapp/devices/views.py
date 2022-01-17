import logging

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


class CameraCreateView(CreateView):
    template_name = "devices/camera-form.html"
    model = Camera
    form_class = CameraCreateForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        device_id = self.kwargs["device_id"]
        device = Device.objects.get(id=device_id)
        if kwargs["instance"] is None:
            kwargs["instance"] = self.model()
        kwargs["instance"].device = device
        return kwargs

    def form_valid(self, *args, **kwargs):
        return super().form_valid(*args, **kwargs)

    def get_success_url(self):
        return reverse("devices:detail", args=(self.object.device.id,))

    def get_context_data(self, *args, **kwargs):
        context = super(CameraCreateView, self).get_context_data(*args, **kwargs)

        context["user"] = self.request.user
        device_id = self.kwargs["device_id"]
        context["device"] = Device.objects.get(id=device_id)
        return context


class DeviceCreateView(CreateView):
    template_name = "devices/device-form.html"
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

        context["devices"] = (
            Device.objects.filter(user=self.request.user).order_by("-updated_dt").all()
        )
        logger.info(context)

        return context


class DeviceDetailView(DetailView, MultipleObjectMixin):
    model = Device
    template_name = "devices/device-detail.html"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        tasks = self.get_object().tasks.all()
        context = super().get_context_data(object_list=tasks, **kwargs)
        return context


class DeviceOnboardingView(DetailView):
    model = Device
    template_name = "device-onboarding.html"
