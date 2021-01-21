# Generated by Django 3.1.3 on 2021-01-19 04:15

from django.db import migrations, models
import print_nanny_webapp.utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ("alerts", "0027_alert_alert_method"),
    ]

    operations = [
        migrations.AlterField(
            model_name="remotecontrolcommandalertsettings",
            name="start_print",
            field=print_nanny_webapp.utils.fields.ChoiceArrayField(
                base_field=models.CharField(
                    choices=[
                        ("RECEIVED", "Command was acknowledged by device"),
                        ("FAILED", "Command failed"),
                        ("SUCCESS", "Command succeeded"),
                    ],
                    max_length=255,
                ),
                blank=True,
                default=("FAILED",),
                help_text="Fires on <strong>StartPrint</strong> command status changes. Helpful for verifying a print job started without a problem.",
                size=None,
            ),
        ),
    ]
