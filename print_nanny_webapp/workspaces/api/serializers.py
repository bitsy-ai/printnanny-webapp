import logging
from typing import Any
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

logger = logging.getLogger(__name__)


class WorkspaceInviteSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkspaceInvitation
        fields = "__all__"


class WorkspaceInviteRemindSerializer(serializers.Serializer):
    workspace_invite = serializers.PrimaryKeyRelatedField(
        queryset=WorkspaceInvitation.objects.all()
    )

    def create(
        self,
        validated_data: Any,
        user,
    ) -> WorkspaceInvitation:
        workspace_invite = validated_data.get("workspace_invite")
        # assert user is member of workspace
        if workspace_invite.organization.is_member(user) is False:
            raise PermissionDenied(
                detail="You are not authorized to manage users in this workspace"
            )
        backend = invitation_backend()
        backend.send_invitation(workspace_invite)
        return workspace_invite

    def update(self, instance: Any, validated_data: Any) -> Any:
        raise NotImplementedError


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
