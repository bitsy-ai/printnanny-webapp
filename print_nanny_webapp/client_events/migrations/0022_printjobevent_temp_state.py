# Generated by Django 3.1.3 on 2021-01-21 07:07

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client_events', '0021_auto_20210118_1506'),
    ]

    operations = [
        migrations.AddField(
            model_name='printjobevent',
            name='temp_state',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={}),
        ),
    ]
