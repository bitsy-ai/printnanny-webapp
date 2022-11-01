from django.db import models


class AchievementType(models.TextChoices):

    FREE_BETA = (
        "FreeBeta",
        "Participated in free beta program",
    )
    FOUNDING_MEMBER = (
        "FoundingMember",
        "Supported PrintNanny by pre-ordering an annual subscription",
    )
