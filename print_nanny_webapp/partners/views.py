from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import TemplateView

User = get_user_model()
