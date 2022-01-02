# Generated by Django 3.2.9 on 2022-01-01 23:50

from django.db import migrations, models
import print_nanny_webapp.utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ("surveys", "0003_alter_remoteaccesssurvey1_user_scale"),
    ]

    operations = [
        migrations.AddField(
            model_name="remoteaccesssurvey1",
            name="business",
            field=models.BooleanField(
                default=False,
                help_text="Do you operate a 3D printing or model design business?",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="remoteaccesssurvey1",
            name="first_name",
            field=models.CharField(default="", max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="remoteaccesssurvey1",
            name="last_name",
            field=models.CharField(default="", max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="remoteaccesssurvey1",
            name="num_printers",
            field=models.PositiveSmallIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="remoteaccesssurvey1",
            name="print_frequency",
            field=models.CharField(
                choices=[
                    ("DAILY", "At least once per day"),
                    ("WEEKLY", "At least once per week"),
                    ("MONTHLY", "At least once per month"),
                    ("YEARLY", "Occasionally, a few times a year"),
                ],
                default="DAILY",
                max_length=32,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="remoteaccesssurvey1",
            name="printer_models",
            field=print_nanny_webapp.utils.fields.ChoiceArrayField(
                base_field=models.CharField(
                    choices=[
                        ("PRUSA", "Prusa"),
                        ("CREALITY", "Creality"),
                        ("FLASHFORGE", "Flashforge"),
                        ("MONOPRICE", "Monoprice"),
                        ("FORMLABS", "Formlabs"),
                        ("LULZBOT", "LulzBot"),
                        ("ULTIMAKER", "Ultimaker"),
                        ("MARKFORGED", "Markforged"),
                        ("PEOPOLY", "Peopoly"),
                        ("TOYBOX", "Toybox"),
                        ("MAKERBOT", "Makerbot"),
                        ("DREMEL", "Dremel"),
                        ("OTHER", "Other"),
                    ],
                    max_length=32,
                ),
                default=["PRUSA"],
                help_text="Check all that apply",
                size=None,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="remoteaccesssurvey1",
            name="printer_models_other",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="remoteaccesssurvey1",
            name="referrer",
            field=models.CharField(
                default="",
                help_text="How did you hear about Print Nanny?",
                max_length=255,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="remoteaccesssurvey1",
            name="usage",
            field=models.TextField(
                default="",
                help_text="Describe your 3D printer usage. What type of things to you make?",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="remoteaccesssurvey1",
            name="worst",
            field=models.TextField(
                blank=True,
                help_text="Tell me what you hate most about 3D printing today",
                null=True,
            ),
        ),
    ]
