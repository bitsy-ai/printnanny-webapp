from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django import forms

from django.utils.translation import gettext_lazy as _
from django.views.generic import (
    DetailView,
    RedirectView,
    UpdateView,
    CreateView,
    TemplateView,
)
from rest_framework.authtoken.models import Token

from print_nanny_webapp.users.forms import InviteRequestForm
from .tasks import create_ghost_members
User = get_user_model()


class ThanksView(TemplateView):
    template_name = "users/thanks.html"


class InviteRequestView(CreateView):
    template_name = "users/inviterequest_form.html"
    success_url = "/thanks/"
    form_class = InviteRequestForm

    def form_valid(self, form):
        res = super().form_valid(form)
        task = create_ghost_members.delay([self.object.to_ghost_member()])
        return res


class UserDetailView(LoginRequiredMixin, DetailView):

    model = User
    slug_field = "email"
    slug_url_kwarg = "email"

    def get_object(self):

        return get_object_or_404(User, id=self.request.user.id)


user_detail_view = UserDetailView.as_view()


class UserUpdateView(LoginRequiredMixin, UpdateView):

    model = User
    fields = []

    def get_success_url(self):
        return reverse("users:detail", kwargs={"email": self.request.user.email})

    def get_object(self):

        return get_object_or_404(User, id=self.request.user.id)

    def form_valid(self, form):
        messages.add_message(
            self.request, messages.INFO, _("Infos successfully updated")
        )
        return super().form_valid(form)


user_update_view = UserUpdateView.as_view()


class UserRedirectView(LoginRequiredMixin, RedirectView):

    permanent = False

    def get_redirect_url(self):
        return reverse("dashboard:home")


user_redirect_view = UserRedirectView.as_view()
