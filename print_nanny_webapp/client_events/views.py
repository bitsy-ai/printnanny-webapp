from django.shortcuts import render
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from print_nanny_webapp.client_events.models import AlertMessage

class AlertMessageDetailView(LoginRequiredMixin, DetailView):

    model = AlertMessage
    queryset = AlertMessage.objects.all()

    template_name = 'alerts/alerts_feedback.html'

    slug_field = "id"
    slug_url_kwarg = "id"


    def get_queryset(self, *args, **kwargs):
        return self.queryset.filter(user_id=self.request.user.id)


class AlertMessageListView(LoginRequiredMixin, ListView):

    template_name = 'alerts/alerts_list.html'

    model = AlertMessage
    queryset = AlertMessage.objects.all()
    slug_field = "id"
    slug_url_kwarg = "id"


    def get_queryset(self, *args, **kwargs):
        return self.queryset.filter(user_id=self.request.user.id)