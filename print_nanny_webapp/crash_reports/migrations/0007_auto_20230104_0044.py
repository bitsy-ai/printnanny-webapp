# Generated by Django 3.2.12 on 2023-01-04 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("crash_reports", "0006_crashreport_description"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="crashreport",
            name="related_crash_report",
        ),
        migrations.AddField(
            model_name="crashreport",
            name="status",
            field=models.CharField(
                choices=[
                    ("Investigating", "Your report is being investigated, thank you!"),
                    (
                        "Fixed",
                        "A fix for your issue has been released. Please submit another crash report if the problem persists.",
                    ),
                ],
                default="Investigating",
                max_length=255,
            ),
        ),
        migrations.AddField(
            model_name="crashreport",
            name="support_comment",
            field=models.TextField(null=True),
        ),
    ]