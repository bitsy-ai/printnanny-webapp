# Generated by Django 3.2.12 on 2023-01-03 18:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("crash_reports", "0003_crashreport_serial"),
    ]

    operations = [
        migrations.AddField(
            model_name="crashreport",
            name="posthog_session",
            field=models.CharField(max_length=255, null=True),
        ),
    ]
