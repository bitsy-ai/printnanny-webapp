# Generated by Django 3.2.9 on 2021-12-29 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("releases", "0005_alter_release_variant"),
    ]

    operations = [
        migrations.AlterField(
            model_name="release",
            name="variant",
            field=models.CharField(
                choices=[
                    ("Desktop", "Customizable Desktop Edition"),
                    ("OctoPrint", "OctoPrint Edition"),
                    ("Mainsail", "Mainsail Edition"),
                    ("REPETIER", "Repetier Edition"),
                ],
                max_length=32,
            ),
        ),
    ]
