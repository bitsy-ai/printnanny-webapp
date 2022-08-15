from django.contrib.auth.mixins import LoginRequiredMixin
from print_nanny_webapp.utils.api.permissions import HasActiveSubscription


class SubscriptionRequiredMixin(LoginRequiredMixin):
    permission_classes = [HasActiveSubscription]
