from rest_framework import serializers
from print_nanny_webapp.achievements.models import Achievement


class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = ("created_dt", "type", "label", "user")
