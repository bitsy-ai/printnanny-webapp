import logging
from typing import Any
from rest_framework import serializers
from organizations.backends import invitation_backend

from print_nanny_webapp.users.api.serializers import UserSerializer
from print_nanny_webapp.workspaces.models import (
    Workspace,
    WorkspaceUser,
    WorkspaceOwner,
    WorkspaceInvitation,
)

logger = logging.getLogger(__name__)


class WorkspaceInviteSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkspaceInvitation
        fields = "__all__"


class WorkspaceInviteCreateSerializer(serializers.Serializer):
    email = serializers.EmailField()
    workspace = serializers.PrimaryKeyRelatedField(queryset=Workspace.objects.all())

    def create(
        self,
        validated_data: Any,
        user,
    ) -> WorkspaceInvitation:
        email = validated_data.get("email")
        workspace = validated_data.get("workspace")
        backend = invitation_backend()
        return backend.invite_by_email(email, user, workspace)

    def update(self, instance: Any, validated_data: Any) -> Any:
        raise NotImplemented


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
