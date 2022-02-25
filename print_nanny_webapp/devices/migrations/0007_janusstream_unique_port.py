# Generated by Django 3.2.12 on 2022-02-25 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("devices", "0006_janusstream_port"),
    ]

    operations = [
        migrations.AddConstraint(
            model_name="janusstream",
            constraint=models.UniqueConstraint(
                condition=models.Q(("deleted", None)),
                fields=("port",),
                name="unique_port",
            ),
        ),
    ]
