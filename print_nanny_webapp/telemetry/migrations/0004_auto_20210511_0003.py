# Generated by Django 3.2.2 on 2021-05-11 07:03

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("telemetry", "0003_auto_20210510_2357"),
    ]

    operations = [
        migrations.AddField(
            model_name="octoprintevent",
            name="octoprint_job",
            field=django.contrib.postgres.fields.jsonb.JSONField(null=True),
        ),
        migrations.AddField(
            model_name="octoprintpluginevent",
            name="octoprint_job",
            field=django.contrib.postgres.fields.jsonb.JSONField(null=True),
        ),
        migrations.AddField(
            model_name="printstatusevent",
            name="octoprint_job",
            field=django.contrib.postgres.fields.jsonb.JSONField(null=True),
        ),
        migrations.AddField(
            model_name="remotecommandevent",
            name="octoprint_job",
            field=django.contrib.postgres.fields.jsonb.JSONField(null=True),
        ),
    ]
