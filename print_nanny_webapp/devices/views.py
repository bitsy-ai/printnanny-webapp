import logging

from django.shortcuts import render
from django.apps import apps
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from print_nanny_webapp.devices.models import Appliance
from django.views.generic.detail import BaseDetailView

Appliance = apps.get_model("devices", "Appliance")
logger = logging.getLogger(__name__)


class ApplianceListView(LoginRequiredMixin, TemplateView):
    template_name = "devices/devices-list.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ApplianceListView, self).get_context_data(**kwargs)

        context["user"] = self.request.user

        context["appliances"] = Appliance.objects.filter(user=self.request.user).all()
        logger.info(context)

        return context

class ApplianceDetailView(LoginRequiredMixin, BaseDetailView):
    model = Appliance
    template_name = "devices/appliance-detail.html"