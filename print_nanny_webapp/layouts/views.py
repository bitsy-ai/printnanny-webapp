from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import TemplateView


User = get_user_model()


class LayoutsView(LoginRequiredMixin, TemplateView):
    pass


horizontal_layouts_view = LayoutsView.as_view(template_name="layouts/horizontal.html")
detached_layouts_view = LayoutsView.as_view(template_name="layouts/detached.html")
