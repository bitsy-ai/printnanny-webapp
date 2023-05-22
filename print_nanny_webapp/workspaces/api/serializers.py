from rest_framework import serializers
from print_nanny_webapp.workspaces.models import (
    Workspace,
    WorkspaceUser,
    WorkspaceOwner,
)


class WorkspaceUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkspaceUser
        fields = "__all__"


class WorkspaceOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkspaceOwner
        fields = "__all__"


class WorkspaceSerializer(serializers.ModelSerializer):
    workspace_users = WorkspaceUserSerializer(many=True)
    owner = WorkspaceOwnerSerializer()

    class Meta:
        model = Workspace
        fields = "__all__"
