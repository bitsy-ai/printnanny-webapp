from rest_framework import serializers
from print_nanny_webapp.octoprint.models import OctoPrintBackup, OctoPrintSettings
from print_nanny_webapp.utils.api.views import (
    generic_create_errors,
    generic_list_errors,
    generic_get_errors,
    generic_update_errors,
)


class OctoPrintSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OctoPrintSettings
        exclude = ("deleted",)
        read_only_fields = ("user",)

    def update_or_create(self, validated_data, user):
        return OctoPrintSettings.objects.filter(user=user).update_or_create(
            defaults=validated_data
        )


class OctoPrintBackupSerializer(serializers.ModelSerializer):
    class Meta:
        model = OctoPrintBackup
        fields = "__all__"
        read_only_fields = ("user",)
