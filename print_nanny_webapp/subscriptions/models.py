from django.utils import timezone
from django.db import models

import djstripe.models
import logging

logger = logging.getLogger(__name__)


class MemberBadgeType(models.TextChoices):

    FREE_BETA = (
        "FreeBeta",
        "Participated in free beta program between January 2021 - July 2021",
    )
    PAID_BETA = "PaidBeta", "Participated in paid beta program starting July 2021"


class MemberBadge(models.Model):

    Types = MemberBadgeType

    class Meta:
        unique_together = ("type", "user")

    created_dt = models.DateTimeField(auto_now_add=True)
    updated_dt = models.DateTimeField(auto_now=True)
    type = models.CharField(choices=MemberBadgeType.choices, max_length=24)
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="member_badges"
    )
