# Generated by Django 3.2.7 on 2021-11-13 22:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("devices", "0004_auto_20211113_1935"),
    ]

    operations = [
        migrations.AddField(
            model_name="device",
            name="bootstrap_release",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.SET_DEFAULT,
                to="releases.release",
            ),
        ),
        migrations.AlterField(
            model_name="device",
            name="hostname",
            field=models.CharField(
                default="printnanny",
                help_text="Please enter the hostname you set in the Raspberry Pi Imager's Advanced Options menu (without .local extension)",
                max_length=255,
            ),
        ),
        migrations.AlterField(
            model_name="device",
            name="release_channel",
            field=models.CharField(
                choices=[
                    ("stable", "Stable mainline release channel"),
                    ("nightly", "Nightly developer release channel"),
                ],
                default="stable",
                help_text="WARNING: you should only use the nightly developer channel when guided by Print Nanny staff! This unstable channel is intended for QA and verifying bug fixes.",
                max_length=8,
            ),
        ),
    ]
