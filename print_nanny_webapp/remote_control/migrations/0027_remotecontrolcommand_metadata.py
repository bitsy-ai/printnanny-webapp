# Generated by Django 3.1.3 on 2021-01-18 19:35

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('remote_control', '0026_remotecontrolsnapshot'),
    ]

    operations = [
        migrations.AddField(
            model_name='remotecontrolcommand',
            name='metadata',
            field=django.contrib.postgres.fields.jsonb.JSONField(null=True),
        ),
    ]
