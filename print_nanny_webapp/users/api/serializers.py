from django.contrib.auth import get_user_model
from rest_framework import serializers

from django_nats_nkeys.services import nsc_generate_creds
from django_nats_nkeys.models import NatsOrganizationUser
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


class NatsOrganizationUserSerializer(serializers.ModelSerializer):

    creds = serializers.SerializerMethodField()

    def get_creds(self, obj) -> str:
        return nsc_generate_creds(obj.organization.name, app_name=obj.app_name)

    class Meta:
        model = NatsOrganizationUser
        fields = ("id", "app_name", "organization", "creds", "json")
