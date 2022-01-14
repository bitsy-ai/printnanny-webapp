from django.apps import apps
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
OctoPrintBackup = apps.get_model("octoprint", "OctoPrintBackup")


class OctoPrintBackupsList(LoginRequiredMixin, TemplateView):
    template_name = "backups-list.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["user"] = self.request.user
        context["octoprint_backups"] = OctoPrintBackup.objects.filter(
            user=self.request.user
        ).order_by("-created_dt")[:10]
        return context
