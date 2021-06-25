from django.utils import timezone
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from djstripe.enums import SubscriptionStatus
from django.db.models import Q

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
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="member_badges"
    )


def is_subscribed(self) -> bool:
    customer = djstripe.models.Customer.objects.get(subscriber=self)
    return customer.has_any_active_subscription()


def is_paid_beta_tester(self) -> bool:
    badge = self.member_badges.filter(type=MemberBadgeType.PAID_BETA).first()
    return badge is not None


def is_free_beta_tester(self) -> bool:
    badge = self.member_badges.filter(type=MemberBadgeType.FREE_BETA).first()
    return badge is not None


def is_beta_tester(self) -> bool:
    return self.is_free_beta_tester or self.is_paid_beta_tester


User.add_to_class("is_paid_beta_tester", is_paid_beta_tester)
User.add_to_class("is_free_beta_tester", is_free_beta_tester)
User.add_to_class("is_beta_tester", is_beta_tester)
User.add_to_class("is_subscribed", is_subscribed)
