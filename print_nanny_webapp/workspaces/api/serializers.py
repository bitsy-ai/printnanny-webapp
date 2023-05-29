import logging
from typing import Any, Tuple

from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.exceptions import PermissionDenied
from organizations.backends import invitation_backend

from print_nanny_webapp.users.api.serializers import UserSerializer
from print_nanny_webapp.workspaces.models import (
    Workspace,
    WorkspaceUser,
    WorkspaceOwner,
    WorkspaceInvitation,
)
from print_nanny_webapp.workspaces.services import verify_workspace_invite
from print_nanny_webapp.users.models import User

logger = logging.getLogger(__name__)


class WorkspaceInviteVerifySerializer(serializers.Serializer):
    token = serializers.UUIDField(format="hex_verbose")
    email = serializers.EmailField()
    password = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()

    def update_or_create(self, validated_data: Any) -> Tuple[WorkspaceInvitation, bool]:
        token = validated_data["token"]
        email = validated_data["email"]
        instance = verify_workspace_invite(token, email)
        try:
            user = User.objects.get(email=email)
            user.first_name = validated_data["first_name"]
            user.last_name = validated_data["last_name"]
            user.is_active = True
            user.set_password(validated_data["password"])
            user.save()
            _, created = instance.organization.get_or_add_user(user)
            instance.invitee = user
            instance.save()
            return instance, created
        except User.DoesNotExist:
            user = User.objects.create(
                email=validated_data["email"],
                first_name=validated_data["first_name"],
                last_name=validated_data["last_name"],
                is_active=True,
            )
            user.set_password(validated_data["password"])
            user.save()

            instance.organization.add_user(user)
            instance.invitee = user
            instance.save()
            return instance, True

    def create(self, instance: WorkspaceInvitation) -> WorkspaceInvitation:
        raise NotImplementedError

    def update(
        self,
        instance: WorkspaceInvitation,
        validated_data: Any,
    ) -> WorkspaceInvitation:
        raise NotImplementedError


class WorkspaceInviteSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkspaceInvitation
        fields = "__all__"


class WorkspaceInviteRemindSerializer(serializers.Serializer):
    workspace_invite = serializers.PrimaryKeyRelatedField(  # type: ignore[var-annotated]
        queryset=WorkspaceInvitation.objects.all()
    )

    def create(self, validated_data: Any) -> Any:
        raise NotImplementedError

    def update(self, instance: Any, validated_data: Any) -> Any:
        raise NotImplementedError


class WorkspaceInviteCreateSerializer(serializers.Serializer):
    email = serializers.EmailField()
    workspace = serializers.PrimaryKeyRelatedField(queryset=Workspace.objects.all())  # type: ignore[var-annotated]

    def create(
        self,
        validated_data: Any,
    ) -> WorkspaceInvitation:
        raise NotImplementedError

    def update(self, instance: Any, validated_data: Any) -> Any:
        raise NotImplementedError


class WorkspaceUserSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = WorkspaceUser
        fields = "__all__"


class WorkspaceOwnerSerializer(serializers.ModelSerializer):
    organization_user = WorkspaceUserSerializer()

    class Meta:
        model = WorkspaceOwner
        fields = "__all__"


class WorkspaceSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True, read_only=True)
    owner = WorkspaceOwnerSerializer(read_only=True)
    pending_invites = WorkspaceInviteSerializer(read_only=True, many=True)

    class Meta:
        model = Workspace
        fields = "__all__"
