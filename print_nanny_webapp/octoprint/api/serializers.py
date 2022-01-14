from rest_framework import serializers
from print_nanny_webapp.octoprint.models import OctoPrintBackup


class OctoPrintBackupSerializer(serializers.ModelSerializer):
    class Meta:
        model = OctoPrintBackup
        fields = "__all__"
        read_only_fields = ("user",)
