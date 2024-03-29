# Generated by Django 3.2.12 on 2022-08-01 19:32

from django.db import migrations, models
import print_nanny_webapp.utils.fields


class Migration(migrations.Migration):
    dependencies = [
        ("events", "0015_emailalertsettings_printjobalert"),
    ]

    operations = [
        migrations.AddField(
            model_name="emailalertsettings",
            name="progress_percent",
            field=models.IntegerField(default=25),
        ),
        migrations.AlterField(
            model_name="emailalertsettings",
            name="event_types",
            field=print_nanny_webapp.utils.fields.ChoiceArrayField(
                base_field=models.CharField(
                    choices=[
                        ("PrintQuality", "Quality control alerts"),
                        ("PrintStarted", "Triggered on print job start"),
                        ("PrintDone", "Triggered when print job is finished"),
                        (
                            "PrintProgress",
                            "Triggered when print job progress reaches %percent",
                        ),
                        ("PrintPaused", "Triggered when print job is paused"),
                        ("PrintCancelled", "Triggered when print job is cancelled"),
                    ],
                    max_length=255,
                ),
                blank=True,
                default=["PrintQuality", "PrintDone", "PrintProgress"],
                size=None,
            ),
        ),
        migrations.AlterField(
            model_name="printjobalert",
            name="event_type",
            field=models.CharField(
                choices=[
                    ("PrintQuality", "Quality control alerts"),
                    ("PrintStarted", "Triggered on print job start"),
                    ("PrintDone", "Triggered when print job is finished"),
                    (
                        "PrintProgress",
                        "Triggered when print job progress reaches %percent",
                    ),
                    ("PrintPaused", "Triggered when print job is paused"),
                    ("PrintCancelled", "Triggered when print job is cancelled"),
                ],
                max_length=32,
            ),
        ),
    ]
