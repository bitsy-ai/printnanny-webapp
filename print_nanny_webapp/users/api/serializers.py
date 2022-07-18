from django.contrib.auth import get_user_model
from rest_framework import serializers

from print_nanny_webapp.users.models import EmailWaitlist

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "id", "first_name", "last_name", "is_beta_tester"]


class EmailWaitlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailWaitlist
        fields = "__all__"
