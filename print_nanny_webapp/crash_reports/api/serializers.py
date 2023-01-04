from rest_framework import serializers

from print_nanny_webapp.crash_reports.models import CrashReport


class CrashReportSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="crash-reports:list")

    class Meta:
        model = CrashReport
        exclude = ("deleted",)
        read_only_fields = ("id", "url")
