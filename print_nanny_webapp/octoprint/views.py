from django.apps import apps
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import OctoPrintSettingsForm

# Create your views here.
OctoPrintBackup = apps.get_model("octoprint", "OctoPrintBackup")
Device = apps.get_model("devices", "Device")


class OctoPrintPluginView(LoginRequiredMixin, FormView):
    template_name = "octoprint-dash.html"
    form_class = OctoPrintSettingsForm

    def get_context_data(self, **kwargs):
        devices = Device.objects.filter(user=self.request.user).all()
        context = super().get_context_data(**kwargs)
        context["devices"] = devices
        context["octoprint_backups"] = OctoPrintBackup.objects.filter(
            user=self.request.user
        ).order_by("-created_dt")[:10]
        return context
