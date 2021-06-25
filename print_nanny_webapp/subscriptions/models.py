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


class MemberBadgeType(models.TextChoices):

    FREE_BETA = (
        "FreeBeta",
        "Participated in free beta program between January 2021 - July 2021",
    )
    PAID_BETA = "PaidBeta", "Participated in paid beta program starting July 2021"


class MemberBadge(models.Model):
    class Meta:
        unique_together = ("type", "user")

    created_dt = models.DateTimeField(auto_now_add=True)
    updated_dt = models.DateTimeField(auto_now=True)
    type = models.CharField(choices=MemberBadgeType.choices, max_length=24)
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
