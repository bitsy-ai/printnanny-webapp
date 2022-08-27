# Generated by Django 3.2.12 on 2022-08-26 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("devices", "0044_delete_publickey"),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name="webrtcstream",
            name="unique_port",
        ),
        migrations.AddField(
            model_name="webrtcstream",
            name="data_rtp_port",
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name="webrtcstream",
            name="video_rtp_port",
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AlterIndexTogether(
            name="webrtcstream",
            index_together={
                ("pi", "created_dt", "updated_dt"),
                ("pi", "config_type", "video_rtp_port", "data_rtp_port"),
            },
        ),
        migrations.AddConstraint(
            model_name="webrtcstream",
            constraint=models.UniqueConstraint(
                condition=models.Q(("config_type", "cloud"), ("deleted", None)),
                fields=("video_rtp_port",),
                name="unique_video_rtp_port",
            ),
        ),
        migrations.AddConstraint(
            model_name="webrtcstream",
            constraint=models.UniqueConstraint(
                condition=models.Q(("config_type", "cloud"), ("deleted", None)),
                fields=("data_rtp_port",),
                name="unique_data_rtp_port",
            ),
        ),
        migrations.RemoveField(
            model_name="webrtcstream",
            name="rtp_port",
        ),
    ]