from django.db import models


class ReferralCodeType(models.TextChoices):
    FOUNDING_MEMBER_TRIAL = (
        "founding_member_trial",
        "A Founding Member has invited you to try PrintNanny",
    )
