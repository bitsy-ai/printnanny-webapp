# Generated by Django 3.2.12 on 2023-01-03 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("crash_reports", "0005_crashreport_related_crash_report"),
    ]

    operations = [
        migrations.AddField(
            model_name="crashreport",
            name="description",
            field=models.TextField(null=True),
        ),
    ]