from django.urls import reverse
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from .models import RemoteAccessSurvey1
from .forms import RemoteAccessSurvey1Form

User = get_user_model()


class RemoteAccessSurvey1Success(TemplateView):
    template_name = "surveys/remote-access-thanks.html"


class RemoteAccessSurvey1Create(CreateView):
    template_name = "surveys/remote-access-form.html"
    models = RemoteAccessSurvey1
    form_class = RemoteAccessSurvey1Form

    def get_success_url(self):
        return reverse("surveys:remote-access-thanks")

    def form_valid(self, form):
        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())

    def save(self, *args, **kwargs):
        # check to see if provided email matches user
        if self.request.user.is_anonymous:
            email = self.cleaned_data["email"]
            user = User.objects.filter(email=email).first()
        else:
            user = self.request.user

        return super(RemoteAccessSurvey1Form, self).save(
            user=user, user_agent=self.request.META, *args, **kwargs
        )
