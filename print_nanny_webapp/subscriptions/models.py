from django.utils import timezone
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from djstripe.enums import SubscriptionStatus

import djstripe.models
import logging

logger = logging.getLogger(__name__)

User = get_user_model()

class MemberBadge(models.Model):
    class Meta:
        unique_together = ("type", "user")
    class BadgeTypes(models.TextChoices):
        BETA_TESTER = "BETA_TESTER", "Early access Beta tester"
        FOUNDING_MEMBER = "FOUNDING_MEMBER", "Become a Founding Member to receive early access to Print Nanny"
    
    type = models.CharField(choices=BadgeTypes.choices, max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

##
# Disable trial for remainder of Beta
##

# @receiver(post_save, sender=User, dispatch_uid="subscriptions_start_trial")
# def start_trial(sender, instance=None, created=False, **kwargs):
#     if not created:
#         return

#     customer = djstripe.models.Customer.create(subscriber=instance)
#     logger.info(f"Created stripe customer {customer.id}")

#     plan = djstripe.models.Plan.objects.first()
#     customer.subscribe(plan, charge_immediately=False, trial_period_days=14)


# def is_trialing(self) -> bool:
#     customer = djstripe.models.Customer.objects.get(subscriber=self)
#     subscriptions = customer.subscriptions.filter(
#         current_period_end__gt=timezone.now(),
#         status=SubscriptionStatus.trialing,
#     )

#     return len(subscriptions) > 0


# User.add_to_class("is_trialing", is_trialing)


def is_subscribed(self) -> bool:
    customer = djstripe.models.Customer.objects.get(subscriber=self)
    return customer.has_any_active_subscription()


User.add_to_class("is_subscribed", is_subscribed)
