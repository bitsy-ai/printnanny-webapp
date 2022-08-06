# Generated by Django 3.2.12 on 2022-08-06 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0018_auto_20220805_0050"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pisoftwareupdateevent",
            name="event_type",
            field=models.CharField(
                choices=[
                    ("UpdateCommand", "Update PrintNanny OS to target version"),
                    ("UpdateStarted", "Started PrintNanny OS update"),
                    ("UpdateSuccess", "PrintNanny OS update succeeded"),
                    ("UpdateError", "Error updating Raspberry Pi"),
                ],
                max_length=32,
            ),
        ),
    ]
