from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie
from django.apps import apps
from django.views.generic import TemplateView
from print_nanny_webapp.utils.permissions import HasActiveSubscription

Alert = apps.get_model("alerts", "AlertMessage")
OctoPrintDevice = apps.get_model("remote_control", "OctoPrintDevice")


class SubscriptionRequiredMixin(LoginRequiredMixin):
    permission_classes = [HasActiveSubscription]


class DashboardView(SubscriptionRequiredMixin, TemplateView):
    @method_decorator(
        (ensure_csrf_cookie,),
        name="dispatch",
    )
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, *args, **kwargs):

        context = super().get_context_data(**kwargs)

        context["user"] = self.request.user
        context["recent_alerts"] = (
            Alert.objects.filter(
                user=self.request.user,
            )
            .order_by("-created_dt")
            .all()
        )

        context["octoprint_devices"] = OctoPrintDevice.objects.filter(
            user=self.request.user
        ).all()
        return context
