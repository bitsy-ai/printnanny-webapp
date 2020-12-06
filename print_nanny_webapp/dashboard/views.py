import logging
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.apps import apps
from django.views.generic import TemplateView, DetailView, FormView, ListView
from django.core.files.uploadedfile import InMemoryUploadedFile, TemporaryUploadedFile
from rest_framework.authtoken.models import Token
from .forms import TimelapseUploadForm,TimelapseReuploadForm, FeedbackForm
from print_nanny_webapp.alerts.tasks.timelapse_alert import create_analyze_video_task, annotate_job_error
from print_nanny_webapp.utils.multiform import MultiFormsView
from django.shortcuts import redirect
from print_nanny_webapp.users.forms import UserSettingsForm
from django.forms.models import model_to_dict

User = get_user_model()
TimelapseAlert = apps.get_model('alerts', 'TimelapseAlert')
AlertMessage = apps.get_model('alerts', 'AlertMessage')
UserSettings = apps.get_model('users', 'UserSettings')

logger = logging.getLogger(__name__)


class DashboardView(LoginRequiredMixin, TemplateView):
    pass

ecommerce_dashboard_view = DashboardView.as_view(template_name="dashboard/ecommerce.html")
crm_dashboard_view = DashboardView.as_view(template_name="dashboard/crm.html")
analytics_dashboard_view = DashboardView.as_view(template_name="dashboard/analytics.html")
projects_dashboard_view = DashboardView.as_view(template_name="dashboard/projects.html")


class HomeDashboardView(LoginRequiredMixin, MultiFormsView):

    model = User
    template_name = 'dashboard/home.html'
    success_url = '/dashboard'

    form_classes = { 'upload': TimelapseUploadForm, 'user_settings': UserSettingsForm }


    def get_user_settings_initial(self):
        settings = UserSettings.objects.get(user=self.request.user.id)
        if settings:
            return model_to_dict(settings)
        return None

    def user_settings_form_valid(self, form):

        if form.is_valid():
            form.instance.user = self.request.user
            settings = UserSettings.objects.get(user=self.request.user.id)
            if settings:
                form = UserSettingsForm(self.request.POST, instance=settings)
            form.save()
        return redirect(self.get_success_url())

    def upload_form_valid(self, form):

        video_file = self.request.FILES.get('video_file')
        if video_file is not None:
            timelapse_alert = TimelapseAlert.objects.create(
                user=self.request.user,
                original_video=self.request.FILES['video_file'],
            )
            if isinstance(video_file, InMemoryUploadedFile):
                logging.info(f'File processed asInMemoryUploadedFile')
                logging.info(f'File info {timelapse_alert.original_video}')
                create_analyze_video_task.apply_async(
                    (timelapse_alert.id,),
                    link_error=annotate_job_error.si(timelapse_alert.id)
                )
            elif isinstance(video_file, TemporaryUploadedFile):
                logging.info(f'File processed as TemporaryUploadedFile')
                create_analyze_video_task.apply_async(
                    (timelapse_alert.id,),
                    link_error=annotate_job_error.si(timelapse_alert.id)
            )
        return redirect(reverse('dashboard:report-cards:list'))


    # def get_object(self):
    #     token, created = Token.objects.get_or_create(user=self.request.user)
    #     self.request.user.token = token
    #     self.request.user.active_alerts = self.request.user.alertmessage_set.filter(seen=False)
    #     return self.request.user

    def get_context_data(self, *args, **kwargs):
        context = super(HomeDashboardView, self).get_context_data(**kwargs)
        token, created = Token.objects.get_or_create(user=self.request.user)
        self.request.user.token = token
        self.request.user.active_alerts = self.request.user.alertmessage_set.filter(seen=False)

        context['object'] = self.request.user

        settings = UserSettings.objects.get(user=self.request.user.id)

        return context

home_dashboard_view = HomeDashboardView.as_view()



class VideoDashboardView(LoginRequiredMixin, MultiFormsView):
    success_url = '/dashboard/report-cards'

    form_classes = {
        'upload': TimelapseReuploadForm,
        'upvote': FeedbackForm,
        'downvote': FeedbackForm
    }
    template_name = 'dashboard/video-list.html'


    def upvote_form_valid(self, form):

        alert_id = self.request.POST.get('alert_id')
        alert = TimelapseAlert.objects.filter(
                id=alert_id
            ).update(
                feedback=True
            )
        
        return redirect(self.get_success_url())

    def downvote_form_valid(self, form):

        alert_id = self.request.POST.get('alert_id')
        alert = TimelapseAlert.objects.filter(
                id=alert_id
            ).update(
                feedback=False
            )
        
        return redirect(self.get_success_url())


    def upload_form_valid(self, form):

        failed_job = self.request.POST.get('alert_id')
        if failed_job is not None:
            logger.warning('Deleting TimelapseAlert with id {failed_job} (tombstones are disabled)')
            TimelapseAlert.objects.filter(id=failed_job).delete()
        


        video_file = self.request.FILES.get('video_file')

        if not video_file:
            return redirect(self.get_success_url())
        if video_file is not None:
            timelapse_alert = TimelapseAlert.objects.create(
                user=self.request.user,
                original_video=self.request.FILES['video_file'],
            )
            if isinstance(video_file, InMemoryUploadedFile):
                logging.info(f'File processed asInMemoryUploadedFile')
                logging.info(f'File info {timelapse_alert.original_video}')
                create_analyze_video_task.apply_async(
                    (timelapse_alert.id,),
                    link_error=annotate_job_error.si(timelapse_alert.id)
                )
            elif isinstance(video_file, TemporaryUploadedFile):
                logging.info(f'File processed as TemporaryUploadedFile')
                create_analyze_video_task.apply_async(
                    (timelapse_alert.id,),
                    link_error=annotate_job_error.si(timelapse_alert.id)
            )
        return redirect(self.get_success_url())

    def get_context_data(self, *args, **kwargs):
        context = super(VideoDashboardView, self).get_context_data(**kwargs)

        context['alerts_success'] = TimelapseAlert.objects\
            .filter(user=self.request.user.id, job_status=TimelapseAlert.JobStatusChoices.SUCCESS)\
            .order_by('-created_dt').all()


        context['alerts_failed'] = TimelapseAlert.objects\
            .filter(user=self.request.user.id, job_status=TimelapseAlert.JobStatusChoices.FAILURE)\
            .order_by('-created_dt').all()

        context['alerts_processing'] = TimelapseAlert.objects\
            .filter(user=self.request.user.id, job_status=TimelapseAlert.JobStatusChoices.PROCESSING)\
            .order_by('-created_dt').all()
        return context

video_dashboard_list_view = VideoDashboardView.as_view()


class VideoDashboardDetailView(LoginRequiredMixin, DetailView):

    model = AlertMessage
    # slug_field = "id"
    # slug_url_kwarg = "id"
    template_name = 'dashboard/video-detail.html'
    # def get_object(self):
        # logger.info(self.request)

video_dashboard_detail_view = VideoDashboardDetailView.as_view()

