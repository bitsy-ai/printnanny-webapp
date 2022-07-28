# Generated by Django 3.2.12 on 2022-07-28 02:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0012_auto_20220620_2205"),
        ("octoprint", "0018_auto_20220715_0111"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("devices", "0032_device_ws_connected"),
    ]

    operations = [
        migrations.CreateModel(
            name="PiSettings",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("deleted", models.DateTimeField(editable=False, null=True)),
                ("updated_dt", models.DateTimeField(auto_now=True)),
                (
                    "cloud_video_enabled",
                    models.BooleanField(
                        default=True, help_text="Send camera stream to PrintNanny Cloud"
                    ),
                ),
                (
                    "telemetry_enabled",
                    models.BooleanField(
                        default=False,
                        help_text="Send telemetry and performance profiling data to PrintNanny Cloud",
                    ),
                ),
            ],
        ),
        migrations.AlterIndexTogether(
            name="devicesettings",
            index_together=None,
        ),
        migrations.RemoveField(
            model_name="devicesettings",
            name="device",
        ),
        migrations.RemoveConstraint(
            model_name="cloudiotdevice",
            name="unique_cloud_iot_device_per_device",
        ),
        migrations.RemoveConstraint(
            model_name="publickey",
            name="unique_public_key_per_device",
        ),
        migrations.RemoveConstraint(
            model_name="systeminfo",
            name="unique_device_info_per_device",
        ),
        migrations.RemoveConstraint(
            model_name="webrtcstream",
            name="unique_janus_stream_per_device",
        ),
        migrations.RenameField(
            model_name="cloudiotdevice",
            old_name="device",
            new_name="pi",
        ),
        migrations.RenameField(
            model_name="publickey",
            old_name="device",
            new_name="pi",
        ),
        migrations.RenameField(
            model_name="systeminfo",
            old_name="device",
            new_name="pi",
        ),
        migrations.RenameField(
            model_name="webrtcstream",
            old_name="device",
            new_name="pi",
        ),
        migrations.AlterIndexTogether(
            name="cloudiotdevice",
            index_together={("pi", "public_key", "created_dt", "updated_dt")},
        ),
        migrations.AlterIndexTogether(
            name="publickey",
            index_together={("pi", "created_dt", "updated_dt")},
        ),
        migrations.AlterIndexTogether(
            name="systeminfo",
            index_together={
                ("pi", "created_dt", "updated_dt"),
                ("os_build_id", "os_variant_id", "os_version_id", "pi"),
            },
        ),
        migrations.AlterIndexTogether(
            name="webrtcstream",
            index_together={("pi", "created_dt", "updated_dt"), ("pi", "config_type")},
        ),
        migrations.AddConstraint(
            model_name="cloudiotdevice",
            constraint=models.UniqueConstraint(
                condition=models.Q(("deleted", None)),
                fields=("pi",),
                name="unique_cloud_iot_device_per_pi",
            ),
        ),
        migrations.AddConstraint(
            model_name="publickey",
            constraint=models.UniqueConstraint(
                condition=models.Q(("deleted", None)),
                fields=("pi",),
                name="unique_public_key_per_pi",
            ),
        ),
        migrations.AddConstraint(
            model_name="systeminfo",
            constraint=models.UniqueConstraint(
                condition=models.Q(("deleted", None)),
                fields=("pi",),
                name="unique_system_info_per_pi",
            ),
        ),
        migrations.AddConstraint(
            model_name="webrtcstream",
            constraint=models.UniqueConstraint(
                condition=models.Q(("deleted", None)),
                fields=("pi", "config_type"),
                name="unique_janus_stream_per_pi",
            ),
        ),
        migrations.RenameModel(
            old_name="Device",
            new_name="Pi",
        ),
        migrations.DeleteModel(
            name="DeviceSettings",
        ),
        migrations.AddField(
            model_name="pisettings",
            name="pi",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="devices.pi"
            ),
        ),
        migrations.AddConstraint(
            model_name="pisettings",
            constraint=models.UniqueConstraint(
                condition=models.Q(("deleted", None)),
                fields=("pi",),
                name="unique_settings_per_pi",
            ),
        ),
        migrations.AlterIndexTogether(
            name="pisettings",
            index_together={("pi", "updated_dt")},
        ),
    ]
