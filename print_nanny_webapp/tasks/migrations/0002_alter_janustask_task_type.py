# Generated by Django 3.2.12 on 2022-02-17 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="janustask",
            name="task_type",
            field=models.CharField(
                choices=[
                    ("cloud_monitor_start", "Start PrintNanny Monitoring (Cloud)"),
                    ("cloud_monitor_stop", "Stop PrintNanny Monitoring (Cloud)"),
                    (
                        "edge_monitor_start",
                        "Start PrintNanny Monitoring (Private/Edge)",
                    ),
                    ("edge_monitor_stop", "Stop PrintNanny Monitoring (Private/Edge)"),
                ],
                max_length=32,
            ),
        ),
    ]
