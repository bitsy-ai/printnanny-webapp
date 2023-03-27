# Generated by Django 3.2.2 on 2021-05-31 19:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("remote_control", "0008_auto_20210531_1202"),
    ]

    operations = [
        migrations.AddField(
            model_name="octoprintdevice",
            name="print_job_status",
            field=models.CharField(
                choices=[
                    ("PrintCancelled", "PrintCancelled"),
                    ("PrintCancelling", "PrintCancelling"),
                    ("PrintDone", "PrintDone"),
                    ("PrintFailed", "PrintFailed"),
                    ("PrintPaused", "PrintPaused"),
                    ("PrintResumed", "PrintResumed"),
                    ("PrintStarted", "PrintStarted"),
                ],
                db_index=True,
                max_length=36,
                null=True,
            ),
        ),
    ]
