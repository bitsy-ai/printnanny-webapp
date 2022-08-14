import re
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.apps import apps

from django_nats_nkeys.services import nsc_generate_creds
from django_nats_nkeys.models import NatsOrganizationUser
from print_nanny_webapp.users.models import EmailWaitlist


User = get_user_model()
MemberBadge = apps.get_model("subscriptions", "MemberBadge")


class MemberBadgeSerializer(serializers.ModelSerializer):
    type = serializers.SerializerMethodField()

    def get_type(self, obj) -> str:
        """
        splits MemberBadge.type on capital leaders
        """
        return " ".join(re.findall("[A-Z][^A-Z]*", obj.type))

    class Meta:
        model = MemberBadge
        fields = ("id", "created_dt", "updated_dt", "type", "label", "user")


class UserSerializer(serializers.ModelSerializer):
    member_badges = MemberBadgeSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = [
            "email",
            "id",
            "first_name",
            "last_name",
            "is_beta_tester",
            "member_badges",
        ]
        depth = 1


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
