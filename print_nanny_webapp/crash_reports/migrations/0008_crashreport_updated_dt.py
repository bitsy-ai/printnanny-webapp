# Generated by Django 3.2.12 on 2023-01-04 04:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("crash_reports", "0007_auto_20230104_0044"),
    ]

    operations = [
        migrations.AddField(
            model_name="crashreport",
            name="updated_dt",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
