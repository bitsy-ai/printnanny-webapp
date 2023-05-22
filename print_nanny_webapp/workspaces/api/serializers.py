import logging
from rest_framework import serializers
from organizations.utils import create_organization
from print_nanny_webapp.workspaces.models import (
    Workspace,
    WorkspaceUser,
    WorkspaceOwner,
)

logger = logging.getLogger(__name__)


class WorkspaceUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkspaceUser
        fields = "__all__"


class WorkspaceOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkspaceOwner
        fields = "__all__"


class WorkspaceSerializer(serializers.ModelSerializer):
    workspace_users = WorkspaceUserSerializer(many=True, read_only=True)
    owner = WorkspaceOwnerSerializer(read_only=True)

    class Meta:
        model = Workspace
        fields = "__all__"
        read_only_fields = ("workspace_users", "owner")
