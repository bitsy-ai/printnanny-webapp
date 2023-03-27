# Generated by Django 3.2.12 on 2023-03-27 00:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("devices", "0059_webrtcstream_mountpoint"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("events", "0032_auto_20220819_1939"),
    ]

    operations = [
        migrations.AddField(
            model_name="printjobalert",
            name="email_message_id",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="printjobalert",
            name="event_source",
            field=models.CharField(
                choices=[
                    ("octoprint", "Events originating from OctoPrint"),
                    ("printnanny_os", "Event originating from PrintNanny OS"),
                    (
                        "printnanny_cloud",
                        "Events originating from PrintNanny Cloud services",
                    ),
                    ("mainsail", "Events originating from moonraker"),
                ],
                default="octoprint",
                max_length=32,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="printjobalert",
            name="user",
            field=models.ForeignKey(
                default=1, on_delete=django.db.models.deletion.CASCADE, to="users.user"
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="printjobalert",
            name="id",
            field=models.UUIDField(editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterIndexTogether(
            name="printjobalert",
            index_together={
                ("id", "email_message_id"),
                ("id", "user", "pi", "created_dt"),
            },
        ),
        migrations.RemoveField(
            model_name="printjobalert",
            name="deleted",
        ),
        migrations.RemoveField(
            model_name="printjobalert",
            name="polymorphic_ctype",
        ),
    ]
