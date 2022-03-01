import logging
from django.db import models
from django.db.models import UniqueConstraint
from django.utils.http import urlencode
from django.urls import reverse
from django.contrib.sites.models import Site
from safedelete.models import SafeDeleteModel, SOFT_DELETE
from .enum import ReferralCodeType


logger = logging.getLogger(__name__)


class MemberBadge(models.Model):
    class MemberBadgeType(models.TextChoices):

        FREE_BETA = (
            "FreeBeta",
            "Participated in free beta program between January 2021 - July 2021",
        )
        PAID_BETA = "PaidBeta", "Participated in paid beta program starting July 2021"

    class Meta:
        unique_together = ("type", "user")

    created_dt = models.DateTimeField(auto_now_add=True)
    updated_dt = models.DateTimeField(auto_now=True)
    type = models.CharField(choices=MemberBadgeType.choices, max_length=24)
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="member_badges"
    )


class ReferralCode(SafeDeleteModel):
    """
    Generate a referral code
    """

    _safedelete_policy = SOFT_DELETE

    class Meta:
        index_together = (
            (
                "user",
                "created_dt",
                "code_type",
                "code",
            ),
        )
        constraints = [
            UniqueConstraint(
                fields=["code"],
                condition=models.Q(deleted=None),
                name="unique_referral_code",
            )
        ]

    created_dt = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="referral_codes"
    )
    code = models.CharField(max_length=255)
    code_type = models.CharField(
        max_length=32,
        default=ReferralCodeType.FOUNDING_MEMBER_TRIAL,
        choices=ReferralCodeType.choices,
    )

    def referral_url(self):
        domain = Site.objects.get_current().domain

        url_path = reverse("trial")
        q = urlencode({"code": self.code})
        return f"https://{domain}{url_path}?{q}"


class ReferralInvite(SafeDeleteModel):
    """
    Send referral code via email
    """

    class Meta:
        index_together = (
            (
                "email",
                "referrer",
            ),
        )
        constraints = [
            UniqueConstraint(
                fields=["email", "referrer"],
                condition=models.Q(deleted=None),
                name="unique_email_per_referrer",
            )
        ]

    created_dt = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()
    referrer = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="referral_invitations"
    )
    recipient = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        null=True,
        related_name="referral_invitations_recipient",
    )


class ReferralSignup(SafeDeleteModel):
    code = models.ForeignKey(
        ReferralCode,
        related_name="referral_signups",
        on_delete=models.CASCADE,
    )
    referrer = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="referral_signups_referrer"
    )
    recipient = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        null=True,
        related_name="referral_signups_recipient",
    )
    created_dt = models.DateTimeField(auto_now_add=True)
