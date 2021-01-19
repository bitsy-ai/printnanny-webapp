import logging

from django.views.decorators.csrf import ensure_csrf_cookie
from django.utils.decorators import method_decorator
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.apps import apps
from django.views.generic import TemplateView, DetailView, FormView, ListView
from django.core.files.uploadedfile import InMemoryUploadedFile, TemporaryUploadedFile
from rest_framework.authtoken.models import Token
from .forms import (
    TimelapseUploadForm,
    TimelapseCancelForm,
    FeedbackForm,
    AppNotificationForm,
    RemoteControlCommandForm,
)
from print_nanny_webapp.alerts.tasks.timelapse_alert import (
    create_analyze_video_task,
    annotate_job_error,
)
from django.db.models import Q, Count
from django.contrib import messages
from django.forms.models import model_to_dict
from django.shortcuts import redirect
import google.api_core.exceptions

from print_nanny_webapp.utils.multiform import MultiFormsView, BaseMultipleFormsView
from print_nanny_webapp.users.forms import UserSettingsForm

User = get_user_model()
Alert = apps.get_model("alerts", "Alert")
ManualVideoUploadAlert = apps.get_model("alerts", "ManualVideoUploadAlert")

UserSettings = apps.get_model("users", "UserSettings")
OctoPrintDevice = apps.get_model("remote_control", "OctoPrintDevice")
PrinterProfile = apps.get_model("remote_control", "PrinterProfile")
RemoteControlCommand = apps.get_model("remote_control", "RemoteControlCommand")
AppCard = apps.get_model("dashboard", "AppCard")
AppNotification = apps.get_model("dashboard", "AppNotification")
logger = logging.getLogger(__name__)


class DashboardView(LoginRequiredMixin, TemplateView):
    @method_decorator(ensure_csrf_cookie)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, *args, **kwargs):

        context = super().get_context_data(**kwargs)

        context["user"] = self.request.user
        context["recent_alerts"] = (
            Alert.objects.filter(
                user=self.request.user,
            )
            .exclude(dismissed=True)
            .order_by("-created_dt")
            .all()
        )

        context["octoprint_devices"] = OctoPrintDevice.objects.filter(
            user=self.request.user
        ).all()
        return context


class HomeDashboardView(DashboardView, MultiFormsView):

    model = User
    template_name = "dashboard/home.html"
    success_url = "/dashboard"

    form_classes = {
        "upload": TimelapseUploadForm,
        "user_settings": UserSettingsForm,
    }

    def get_user_settings_initial(self):
        settings = UserSettings.objects.filter(user=self.request.user.id).first()
        if settings:
            return model_to_dict(settings)
        return None

    def user_settings_form_valid(self, form):

        if form.is_valid():
            form.instance.user = self.request.user
            settings = UserSettings.objects.filter(user=self.request.user.id).first()
            if settings:
                form = UserSettingsForm(self.request.POST, instance=settings)
            form.save()
        return redirect(self.get_success_url())

    def upload_form_valid(self, form):

        video_file = self.request.FILES.get("video_file")
        if video_file is not None:
            timelapse_alert = ManualVideoUploadAlert.objects.create(
                user=self.request.user,
                original_video=self.request.FILES["video_file"],
            )
            if isinstance(video_file, InMemoryUploadedFile):
                logging.info(f"File processed asInMemoryUploadedFile")
                logging.info(f"File info {timelapse_alert.original_video}")
                create_analyze_video_task.apply_async(
                    (timelapse_alert.id,),
                    link_error=annotate_job_error.si(timelapse_alert.id),
                )
            elif isinstance(video_file, TemporaryUploadedFile):
                logging.info(f"File processed as TemporaryUploadedFile")
                create_analyze_video_task.apply_async(
                    (timelapse_alert.id,),
                    link_error=annotate_job_error.si(timelapse_alert.id),
                )
        return redirect(reverse("dashboard:report-cards:list"))

    def get_context_data(self, *args, **kwargs):
        form_classes = self.get_form_classes()
        forms = self.get_forms(form_classes)
        context = super().get_context_data(forms=forms, **kwargs)
        logger.info(context)
        # logger.info(context)
        token, created = Token.objects.get_or_create(user=self.request.user)
        context["user"].token = token

        return context


home_dashboard_view = HomeDashboardView.as_view()


class AppDashboardListView(DashboardView, FormView):
    template_name = "dashboard/apps-list.html"
    success_url = "/dashboard/apps/"

    form_class = AppNotificationForm

    def form_valid(self, form):

        app_id = self.request.POST.get("app_id")

        AppNotification.objects.get_or_create(user=self.request.user, app_id=app_id)
        return redirect(self.get_success_url())

    def get_context_data(self, *args, **kwargs):
        context = super(AppDashboardListView, self).get_context_data(**kwargs)

        context["ecommerce_apps"] = (
            AppCard.objects.filter(category="Ecommerce")
            .prefetch_related("appnotification_set")
            .annotate(watching=Count(Q(appnotification__user=self.request.user)))
        )

        # context["notification_apps"] = AppCard.objects.filter(category="Notifications").prefetch_related('appnotification_set').filter(appnotification__user=self.request.user.id).all()
        context["notification_apps"] = (
            AppCard.objects.filter(category="Notifications")
            .prefetch_related("appnotification_set")
            .annotate(watching=Count(Q(appnotification__user=self.request.user)))
        )

        context["automation_apps"] = (
            AppCard.objects.filter(category="Automation")
            .prefetch_related("appnotification_set")
            .annotate(watching=Count(Q(appnotification__user=self.request.user)))
        )

        return context


app_dashboard_list_view = AppDashboardListView.as_view()


class OctoPrintDevicesDetailView(DashboardView, DetailView, FormView):
    model = OctoPrintDevice
    # slug_field = "id"
    # slug_url_kwarg = "id"
    form_class = RemoteControlCommandForm

    template_name = "dashboard/octoprint-devices-detail.html"

    def form_valid(self, form):
        device = self.get_object()
        command = form.cleaned_data.get("command")

        try:
            RemoteControlCommand.objects.create(
                user=self.request.user, device=device, command=command
            )
        except google.api_core.exceptions.FailedPrecondition:
            messages.add_message(
                self.request,
                messages.ERROR,
                "Command failed! Device received conflicting instructions. Refresh this page to try again.",
            )
        return redirect("dashboard:octoprint-devices:detail", pk=device.id)

    def get_object(self):
        self.object = super().get_object()

        return self.object

    def get_context_data(self, *args, **kwargs):
        self.get_object()
        context = super(OctoPrintDevicesDetailView, self).get_context_data(**kwargs)
        # context["valid_actions"] = RemoteControlCommand.VALID_ACTIONS[context["object"].print_job_status]

        context["sent_commands"] = RemoteControlCommand.objects.filter(
            user_id=self.request.user
        ).order_by("-created_dt")[:5]

        return context

    def get_form_kwargs(self):
        kwargs = super(OctoPrintDevicesDetailView, self).get_form_kwargs()

        obj = super().get_object()

        kwargs["command_choices"] = RemoteControlCommand.VALID_ACTIONS[
            obj.print_job_status
        ]
        return kwargs


octoprint_device_dashboard_detail_view = OctoPrintDevicesDetailView.as_view()


class OctoPrintDeviceListView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard/octoprint-devices-list.html"

    def get_context_data(self, *args, **kwargs):
        context = super(OctoPrintDeviceListView, self).get_context_data(**kwargs)
        token, created = Token.objects.get_or_create(user=self.request.user)
        self.request.user.token = token

        context["user"] = self.request.user

        context["octoprint_devices"] = OctoPrintDevice.objects.filter(
            user=self.request.user
        ).all()

        context["printer_profiles"] = PrinterProfile.objects.filter(
            user=self.request.user
        ).all()

        return context


octoprint_device_dashboard_list_view = OctoPrintDeviceListView.as_view()


class VideoDashboardView(LoginRequiredMixin, MultiFormsView):
    success_url = "/dashboard/report-cards/"

    form_classes = {
        "upload": TimelapseUploadForm,
        "upvote": FeedbackForm,
        "downvote": FeedbackForm,
        "dismiss": TimelapseCancelForm,
        "cancel": TimelapseCancelForm,
    }
    template_name = "dashboard/video-list.html"

    def dismiss_form_valid(self, form):
        failed_job = self.request.POST.get("alert_id")
        if failed_job is not None:
            ManualVideoUploadAlert.objects.filter(id=failed_job).update(seen=True)

        return redirect(reverse("dashboard:report-cards:list"))

    def cancel_form_valid(self, form):
        failed_job = self.request.POST.get("alert_id")
        if failed_job is not None:
            ManualVideoUploadAlert.objects.filter(id=failed_job).update(
                job_status=ManualVideoUploadAlert.JobStatusChoices.CANCELLED
            )

        return redirect(reverse("dashboard:report-cards:list"))

    def upvote_form_valid(self, form):

        alert_id = self.request.POST.get("alert_id")
        alert = ManualVideoUploadAlert.objects.filter(id=alert_id).update(feedback=True)

        return redirect(self.get_success_url())

    def downvote_form_valid(self, form):

        alert_id = self.request.POST.get("alert_id")
        alert = ManualVideoUploadAlert.objects.filter(id=alert_id).update(
            feedback=False
        )

        return redirect(self.get_success_url())

    def upload_form_valid(self, form):

        video_file = self.request.FILES.get("video_file")
        if video_file is not None:
            timelapse_alert = ManualVideoUploadAlert.objects.create(
                user=self.request.user,
                original_video=self.request.FILES["video_file"],
            )
            if isinstance(video_file, InMemoryUploadedFile):
                logging.info(f"File processed asInMemoryUploadedFile")
                logging.info(f"File info {timelapse_alert.original_video}")
                create_analyze_video_task.apply_async(
                    (timelapse_alert.id,),
                    link_error=annotate_job_error.si(timelapse_alert.id),
                )
            elif isinstance(video_file, TemporaryUploadedFile):
                logging.info(f"File processed as TemporaryUploadedFile")
                create_analyze_video_task.apply_async(
                    (timelapse_alert.id,),
                    link_error=annotate_job_error.si(timelapse_alert.id),
                )
        return redirect(reverse("dashboard:report-cards:list"))

    def get_context_data(self, *args, **kwargs):
        context = super(VideoDashboardView, self).get_context_data(**kwargs)

        context["alerts_success"] = (
            ManualVideoUploadAlert.objects.filter(
                user=self.request.user.id,
                job_status=ManualVideoUploadAlert.JobStatusChoices.SUCCESS,
            )
            .order_by("-created_dt")
            .all()
        )

        context["alerts_failed"] = (
            ManualVideoUploadAlert.objects.filter(
                user=self.request.user.id,
                job_status=ManualVideoUploadAlert.JobStatusChoices.FAILURE,
            )
            .order_by("-created_dt")
            .all()
        )

        context["alerts_processing"] = (
            ManualVideoUploadAlert.objects.filter(
                user=self.request.user.id,
                job_status=ManualVideoUploadAlert.JobStatusChoices.PROCESSING,
            )
            .order_by("-created_dt")
            .all()
        )

        return context


video_dashboard_list_view = VideoDashboardView.as_view()


class VideoDashboardDetailView(LoginRequiredMixin, DetailView):

    model = ManualVideoUploadAlert
    # slug_field = "id"
    # slug_url_kwarg = "id"
    template_name = "dashboard/video-detail.html"

    def get_object(self):
        obj = super().get_object()

        # obj.seen = True
        obj.save()
        return obj


video_dashboard_detail_view = VideoDashboardDetailView.as_view()
