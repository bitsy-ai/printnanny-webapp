import json
import logging

from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, DeleteView, CreateView
from django.views import View
from django.http import HttpResponse
from django.views.generic.detail import SingleObjectMixin
from print_nanny_webapp.devices.models import Device, License
from .api.serializers import LicenseSerializer

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
    paginate_by = 10

    # TODO implement reverse for events using MultipleObjectMixin
    # def get_context_data(self, **kwargs):
    #     tasks = self.get_object().events.all()
    #     context = super().get_context_data(object_list=tasks, **kwargs)
    #     return context


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
        obj.user = self.request.user
        obj.save()
        self.object = obj

        success_url = self.get_success_url()
        return HttpResponseRedirect(success_url)


class LicenseDeleteView(LoginRequiredMixin, DeleteView):
    model = License
    template_name = "license-delete.html"
    success_url = "/dashboard/"


class LicenseDownloadView(LoginRequiredMixin, SingleObjectMixin, View):
    model = License
    slug_field = "id"

    def get(self, request, pk=None):
        obj = License.objects.get(id=pk)
        serializer = LicenseSerializer(instance=obj)
        json_str = json.dumps(serializer.data)
        response = HttpResponse(json_str, content_type="application/json")
        response["Content-Disposition"] = "attachment; filename=license.txt"
        return response
