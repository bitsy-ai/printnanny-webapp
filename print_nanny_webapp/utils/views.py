from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie
from django.apps import apps
from django.views.generic import TemplateView
from rest_framework.request import Request
from print_nanny_webapp.utils.permissions import HasActiveSubscription
from print_nanny_webapp.users.models import User


class AuthenticatedHttpRequest(Request):
    user: User


class SubscriptionRequiredMixin(LoginRequiredMixin):
    permission_classes = [HasActiveSubscription]
