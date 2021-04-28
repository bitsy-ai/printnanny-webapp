# Generated by Django 3.1.7 on 2021-04-03 04:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("alerts", "0042_auto_20210329_1411"),
    ]

    operations = [
        migrations.AlterField(
            model_name="alert",
            name="alert_type",
            field=models.CharField(
                choices=[
                    ("COMMAND", "Remote command status updates"),
                    ("PRINT_PROGRESS", "Percentage-based print progress"),
                    (
                        "MANUAL_VIDEO_UPLOAD",
                        "Manually-uploaded video is ready for review",
                    ),
                    ("DEFECT", "Defect detected in print"),
                    ("PRINT_SESSION_DONE", "Print job is finished"),
                ],
                max_length=255,
            ),
        ),
        migrations.AlterField(
            model_name="alertsettings",
            name="alert_type",
            field=models.CharField(
                choices=[
                    ("COMMAND", "Remote command status updates"),
                    ("PRINT_PROGRESS", "Percentage-based print progress"),
                    (
                        "MANUAL_VIDEO_UPLOAD",
                        "Manually-uploaded video is ready for review",
                    ),
                    ("DEFECT", "Defect detected in print"),
                    ("PRINT_SESSION_DONE", "Print job is finished"),
                ],
                max_length=255,
            ),
        ),
        migrations.CreateModel(
            name="PrintSessionDoneAlert",
            fields=[
                (
                    "alert_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="alerts.alert",
                    ),
                ),
                (
                    "print_session",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="remote_control.printsession",
                    ),
                ),
            ],
            options={
                "abstract": False,
                "base_manager_name": "objects",
            },
            bases=("alerts.alert",),
        ),
    ]
