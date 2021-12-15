# Generated by Django 3.2.9 on 2021-12-15 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("devices", "0032_alter_taskstatus_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="task_type",
            field=models.CharField(
                choices=[
                    ("check_license", "License Verification"),
                    ("software_update", "Software Updating"),
                ],
                default="software_update",
                max_length=255,
            ),
        ),
    ]
