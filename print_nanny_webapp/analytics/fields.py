from django.db import models


class MembershipTagType(models.TextChoices):

    BETA_FREE = (
        "BetaFree",
        "Participated in free beta program between January 2021 - July 2021",
    )
    BETA_PAID = "BetaPaid", "Participated in paid beta program starting July 2021"
