# Generated by Django 3.1.3 on 2021-01-18 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("client_events", "0020_printjobevent_progress"),
    ]

    operations = [
        migrations.AlterField(
            model_name="printjobevent",
            name="current_z",
            field=models.FloatField(null=True),
        ),
    ]
