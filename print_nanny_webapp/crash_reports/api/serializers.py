from rest_framework import serializers

from print_nanny_webapp.crash_reports.models import CrashReport


class CrashReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = CrashReport
        exclude = ("deleted",)
        read_only_fields = ("id",)
