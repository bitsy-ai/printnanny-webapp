from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import UniqueConstraint
from safedelete.models import SafeDeleteModel, SOFT_DELETE
from .enum import ReferralCodeType

User = get_user_model()


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
                fields=["user", "code"],
                condition=models.Q(deleted=None),
                name="unique_referral_code_per_user",
            )
        ]

    created_dt = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="referral_codes"
    )
    code = models.CharField(max_length=255)
    code_type = models.CharField(
        max_length=32,
        default=ReferralCodeType.FOUNDING_MEMBER_TRIAL,
        choices=ReferralCodeType.choices,
    )


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
        User, on_delete=models.CASCADE, related_name="referral_invitations"
    )
    recipient = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        related_name="referral_invitations_recipient",
    )
