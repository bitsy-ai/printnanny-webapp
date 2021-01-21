# Generated by Django 3.1.3 on 2021-01-18 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("alerts", "0026_remotecontrolcommandalertsettings_snapshot"),
    ]

    operations = [
        migrations.AddField(
            model_name="alert",
            name="alert_method",
            field=models.CharField(
                choices=[
                    ("UI", "Recive Print Nanny UI notifations"),
                    ("EMAIL", "Receive email notifications"),
                ],
                default="UI",
                max_length=255,
            ),
            preserve_default=False,
        ),
    ]
