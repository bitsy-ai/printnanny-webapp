# Generated by Django 3.2.12 on 2022-07-30 20:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("devices", "0033_auto_20220728_0237"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="pi",
            name="ws_connected",
        ),
        migrations.AddField(
            model_name="pi",
            name="edition",
            field=models.CharField(
                choices=[("octoprint_lite", "OctoPrint Lite")],
                default="octoprint_lite",
                max_length=32,
            ),
        ),
    ]
