from django.urls import reverse
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from .models import RemoteAccessSurvey1
from .forms import RemoteAccessSurvey1Form


class RemoteAccessSurvey1Success(TemplateView):
    template_name = "surveys/remote-access-thanks.html"


class RemoteAccessSurvey1Create(CreateView):
    template_name = "surveys/remote-access-form.html"
    models = RemoteAccessSurvey1
    form_class = RemoteAccessSurvey1Form

    def get_success_url(self):
        return reverse("surveys:remote-access-thanks")
