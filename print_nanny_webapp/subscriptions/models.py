from time import timezone
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.dispatch import receiver

import djstripe.models
import logging

logger = logging.getLogger(__name__)

User = get_user_model()

@receiver(post_save, sender=User)
def start_trial(sender, instance=None, **kwargs):
    if not instance._state.adding:
        return

    customer = djstripe.models.Customer.create(subscriber=instance)

    plan = djstripe.models.Plan.objects.first()
    customer.subscribe(plan, charge_immediately=False, trial_period_days=14)
