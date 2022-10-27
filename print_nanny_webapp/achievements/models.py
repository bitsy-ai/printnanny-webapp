from django.db import models
from django.contrib.auth import get_user_model

from print_nanny_webapp.achievements.enum import AchievementType

# Create your models here.

UserModel = get_user_model()


class Achievement(models.Model):
    class Meta:
        unique_together = ("type", "user")

    created_dt = models.DateTimeField(auto_now_add=True)
    type = models.CharField(choices=AchievementType.choices, max_length=24)
    user = models.ForeignKey(
        UserModel, on_delete=models.CASCADE, related_name="achievements"
    )

    @property
    def label(self):
        return AchievementType(self.type).label
