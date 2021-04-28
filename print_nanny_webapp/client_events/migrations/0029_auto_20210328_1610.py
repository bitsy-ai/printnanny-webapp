# Generated by Django 3.1.7 on 2021-03-28 23:10

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("client_events", "0024_auto_20210313_1428_squashed_0025_auto_20210313_1447"),
    ]

    operations = [
        migrations.AddField(
            model_name='monitoringframeevent',
            name='event_type',
            field=models.CharField(choices=[('monitoring_frame_raw', 'Monitoring frame sent without model annotations'), ('monitoring_frame_post', 'Monitoring frame sent with on-device annotations')], db_index=True, default='monitoring_frame_raw', max_length=255),
        ),
        migrations.DeleteModel(
            name='MonitoringFrameEvent',
        ),
        migrations.AddField(
            model_name='octoprintevent',
            name='print_session',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='remote_control.printsession'),
        ),
        migrations.AddField(
            model_name='printjobstate',
            name='print_session',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='remote_control.printsession'),
        ),
        migrations.CreateModel(
            name="PrintSessionState",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_dt", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("event_data", models.JSONField(null=True)),
                ("plugin_version", models.CharField(max_length=60)),
                ("client_version", models.CharField(max_length=60)),
                ("octoprint_version", models.CharField(max_length=60)),
                (
                    "event_type",
                    models.CharField(
                        choices=[
                            ("Error", "Error"),
                            ("PrintCancelled", "PrintCancelled"),
                            ("PrintCancelling", "PrintCancelling"),
                            ("PrintDone", "PrintDone"),
                            ("PrintFailed", "PrintFailed"),
                            ("PrintPaused", "PrintPaused"),
                            ("PrintResumed", "PrintResumed"),
                            ("PrintStarted", "PrintStarted"),
                        ],
                        db_index=True,
                        max_length=255,
                    ),
                ),
                ("state", django.contrib.postgres.fields.jsonb.JSONField(default=dict)),
                ("current_z", models.FloatField(null=True)),
                (
                    "progress",
                    django.contrib.postgres.fields.jsonb.JSONField(default=dict),
                ),
                ("job_data_file", models.CharField(max_length=255)),
                (
                    "device",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="remote_control.octoprintdevice",
                    ),
                ),
                (
                    "print_session",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="remote_control.printsession",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.DeleteModel(
            name="PrintJobState",
        ),
    ]
