import logging
import google.api_core.exceptions
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.apps import apps
from django.views.generic import TemplateView, FormView
from django.views.generic.detail import BaseDetailView
from rest_framework.authtoken.models import Token
from .forms import (
    FeedbackForm,
    AppNotificationForm,
    RemoteControlCommandForm,
    RemoveDeviceForm,
)

from django.http import HttpResponseRedirect

from django.db.models import Q, Count
from django.contrib import messages
from django.forms.models import model_to_dict
from django.shortcuts import redirect

from print_nanny_webapp.utils.multiform import MultiFormsView
from print_nanny_webapp.partners.forms import RevokeGeeksTokenForm
from print_nanny_webapp.alerts.tasks.alerts import AlertTask
from print_nanny_webapp.utils.views import DashboardView
from django.contrib import messages

User = get_user_model()
Alert = apps.get_model("alerts", "AlertMessage")
GeeksToken = apps.get_model("partners", "GeeksToken")

OctoPrintBackups = apps.get_model("octoprint", "OctoPrintBackup")
UserSettings = apps.get_model("users", "UserSettings")
OctoPrintDevice = apps.get_model("remote_control", "OctoPrintDevice")
PrinterProfile = apps.get_model("remote_control", "PrinterProfile")
RemoteControlCommand = apps.get_model("remote_control", "RemoteControlCommand")
AppCard = apps.get_model("dashboard", "AppCard")
AppNotification = apps.get_model("dashboard", "AppNotification")
AlertSettings = apps.get_model("alerts", "AlertSettings")
TestAlert = apps.get_model("alerts", "TestAlert")
VideoStatusAlert = apps.get_model("alerts", "VideoStatusAlert")
logger = logging.getLogger(__name__)


class HomeDashboardView(DashboardView):

    model = User
    template_name = "dashboard/home.html"
    success_url = "/dashboard"

    def get_user_settings_initial(self):
        settings = UserSettings.objects.filter(user=self.request.user.id).first()
        if settings:
            return model_to_dict(settings)
        return None

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        logger.info(context)
        # logger.info(context)
        token, created = Token.objects.get_or_create(user=self.request.user)
        octoprint_backups = OctoPrintBackups.objects.filter(user=self.request.user)[:10]
        context["user"].token = token
        context["octoprint_backups"] = octoprint_backups

        return context


home_dashboard_view = HomeDashboardView.as_view()


class AppDashboardListView(DashboardView, FormView):
    template_name = "dashboard/apps-list.html"
    success_url = "/dashboard/apps/"
    # Incompatible types in assignment (expression has type "str", base class "MultiFormMixin" defined the type as "None")

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


class OctoPrintDevicesDetailView(MultiFormsView, LoginRequiredMixin, BaseDetailView):
    model = OctoPrintDevice
    template_name = "dashboard/octoprint-devices-detail.html"

    form_classes = {
        "remote_command": RemoteControlCommandForm,
        "remove_device": RemoveDeviceForm,
        "revoke_3dgeeks": RevokeGeeksTokenForm,
        "test_3dgeeks": RevokeGeeksTokenForm,
    }

    def test_3dgeeks_form_valid(self, form):
        octoprint_device_id = self.request.POST.get("octoprint_device_id")
        alert_message = TestAlert.objects.create(
            alert_method=AlertSettings.AlertMethod.PARTNER_3DGEEKS,
            event_type=TestAlert.TestAlertEventType.PRINT_NANNY_WEBAPP,
            user=self.request.user,
        )
        task = AlertTask(alert_message)
        task.trigger_alert()
        messages.success(self.request, "Test alert was sent! Check the 3D Geeks app.")
        return HttpResponseRedirect(self.request.path_info)

    def revoke_3dgeeks_form_valid(self, form):
        octoprint_device_id = self.request.POST.get("octoprint_device_id")
        token = GeeksToken.objects.get(octoprint_device=octoprint_device_id)
        token.delete()
        octoprint_device = OctoPrintDevice.objects.get(id=octoprint_device_id)
        token, created = GeeksToken.objects.get_or_create(
            octoprint_device=octoprint_device, user=self.request.user, deleted=None
        )
        return redirect("dashboard:octoprint-devices:detail", pk=octoprint_device.id)

    def remove_device_form_valid(self, form):
        octoprint_device_id = self.request.POST.get("octoprint_device_id")
        device = OctoPrintDevice.objects.get(id=octoprint_device_id)
        device.delete()
        return redirect("dashboard:octoprint-devices:list")

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_classes = self.get_form_classes()
        forms = self.get_forms(form_classes)
        context = self.get_context_data(object=self.object, forms=forms)
        return self.render_to_response(context)

    def remote_command_form_valid(self, form):
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
        token, created = GeeksToken.objects.get_or_create(
            octoprint_device=self.object, user=self.request.user, deleted=None
        )
        return self.object

    def get_context_data(self, *args, **kwargs):
        self.get_object()

        context = super(OctoPrintDevicesDetailView, self).get_context_data(**kwargs)

        context["sent_commands"] = RemoteControlCommand.objects.filter(
            user_id=self.request.user
        ).order_by("-created_dt")[:5]

        return context

    def create_remote_command_form(self, **kwargs):
        obj = self.get_object()
        print_job_status = (
            obj.active_session.print_job_status if obj.active_session else None
        )
        command_choices = RemoteControlCommand.get_valid_actions(print_job_status)
        form = RemoteControlCommandForm(command_choices=command_choices, **kwargs)
        return form


octoprint_device_dashboard_detail_view = OctoPrintDevicesDetailView.as_view()


class OctoPrintDeviceListView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard/octoprint-devices-list.html"

    def get_context_data(self, *args, **kwargs):
        context = super(OctoPrintDeviceListView, self).get_context_data(**kwargs)
        Token.objects.get_or_create(user=self.request.user)

        context["user"] = self.request.user

        context["octoprint_devices"] = OctoPrintDevice.objects.filter(
            user=self.request.user
        ).all()

        context["printer_profiles"] = PrinterProfile.objects.filter(
            user=self.request.user
        ).all()

        return context


octoprint_device_dashboard_list_view = OctoPrintDeviceListView.as_view()


class VideoDashboardView(LoginRequiredMixin, TemplateView, MultiFormsView):
    template_name = "dashboard/video-list.html"
    success_url = "/dashboard/videos/"  # type: ignore
    form_classes = {
        "needs_review": FeedbackForm,
    }

    def needs_review_form_valid(self, form):
        alert_id = self.request.POST.get("alert_id")
        needs_review = bool(int(self.request.POST.get("needs_review", False)))
        if alert_id is not None and needs_review is not None:
            # python, i love you, but i'm breaking up with your type system
            Alert.objects.filter(id=alert_id).update(needs_review=needs_review)

        return redirect(reverse("dashboard:videos:list"))

    def get_context_data(self, *args, **kwargs):
        context = super(VideoDashboardView, self).get_context_data(**kwargs)

        context["user"] = self.request.user
        alerts = (
            VideoStatusAlert.objects.filter(user=self.request.user)
            .order_by("-created_dt")
            .all()
        )
        context["alerts"] = alerts
        return context


video_list_view = VideoDashboardView.as_view()

# class VideoDashboardView(LoginRequiredMixin, MultiFormsView):
#     success_url = "/dashboard/report-cards/"

#     form_classes = {
#         "upload": TimelapseUploadForm,
#         "upvote": FeedbackForm,
#         "downvote": FeedbackForm,
#         "dismiss": TimelapseCancelForm,
#         "cancel": TimelapseCancelForm,
#     }
#     template_name = "dashboard/report-cards-list.html"

#     def dismiss_form_valid(self, form):
#         failed_job = self.request.POST.get("alert_id")
#         if failed_job is not None:
#             ManualVideoUploadAlert.objects.filter(id=failed_job).update(
#                 seen=True, dismissed=True
#             )

#         return redirect(reverse("dashboard:report-cards:list"))

#     def cancel_form_valid(self, form):
#         failed_job = self.request.POST.get("alert_id")
#         if failed_job is not None:
#             ManualVideoUploadAlert.objects.filter(id=failed_job).update(
#                 job_status=ManualVideoUploadAlert.JobStatusChoices.CANCELLED
#             )

#         return redirect(reverse("dashboard:report-cards:list"))

#     def upvote_form_valid(self, form):

#         alert_id = self.request.POST.get("alert_id")
#         alert = ManualVideoUploadAlert.objects.filter(id=alert_id).update(feedback=True)

#         return redirect(self.get_success_url())

#     def downvote_form_valid(self, form):

#         alert_id = self.request.POST.get("alert_id")
#         alert = ManualVideoUploadAlert.objects.filter(id=alert_id).update(
#             feedback=False
#         )

#         return redirect(self.get_success_url())

#     def upload_form_valid(self, form):

#         video_file = self.request.FILES.get("video_file")
#         if video_file is not None:
#             timelapse_alert = ManualVideoUploadAlert.objects.create(
#                 user=self.request.user,
#                 original_video=self.request.FILES["video_file"],
#             )
#             if isinstance(video_file, InMemoryUploadedFile):
#                 logging.info(f"File processed asInMemoryUploadedFile")
#                 logging.info(f"File info {timelapse_alert.original_video}")
#                 create_analyze_video_task.apply_async(
#                     (timelapse_alert.id,),
#                     link_error=annotate_job_error.si(timelapse_alert.id),
#                 )
#             elif isinstance(video_file, TemporaryUploadedFile):
#                 logging.info(f"File processed as TemporaryUploadedFile")
#                 create_analyze_video_task.apply_async(
#                     (timelapse_alert.id,),
#                     link_error=annotate_job_error.si(timelapse_alert.id),
#                 )
#         return redirect(reverse("dashboard:report-cards:list"))

#     def get_context_data(self, *args, **kwargs):
#         context = super(VideoDashboardView, self).get_context_data(**kwargs)

#         context["alerts_success"] = (
#             ManualVideoUploadAlert.objects.filter(
#                 user=self.request.user.id,
#                 job_status=ManualVideoUploadAlert.JobStatusChoices.SUCCESS,
#             )
#             .order_by("-created_dt")
#             .all()
#         )

#         context["alerts_failed"] = (
#             ManualVideoUploadAlert.objects.filter(
#                 user=self.request.user.id,
#                 job_status=ManualVideoUploadAlert.JobStatusChoices.FAILURE,
#                 dismissed=False,
#             )
#             .order_by("-created_dt")
#             .all()
#         )

#         context["alerts_processing"] = (
#             ManualVideoUploadAlert.objects.filter(
#                 user=self.request.user.id,
#                 job_status=ManualVideoUploadAlert.JobStatusChoices.PROCESSING,
#             )
#             .order_by("-created_dt")
#             .all()
#         )

#         return context


# video_dashboard_list_view = VideoDashboardView.as_view()


# class VideoDashboardDetailView(LoginRequiredMixin, DetailView):

#     model = ManualVideoUploadAlert
#     # slug_field = "id"
#     # slug_url_kwarg = "id"
#     template_name = "dashboard/report-cards-detail.html"

#     def get_object(self):
#         obj = super().get_object()

#         # obj.seen = True
#         obj.save()
#         return obj


# video_dashboard_detail_view = VideoDashboardDetailView.as_view()
