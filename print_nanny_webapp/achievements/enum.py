from django.db import models


class AchievementType(models.TextChoices):

    FREE_BETA = (
        "Free Beta",
        "Participated in free beta program",
    )
    FOUNDING_MEMBER = (
        "Founding Member",
        "Supported PrintNanny by pre-ordering an annual subscription",
    )
