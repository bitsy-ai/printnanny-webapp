# Generated by Django 3.1.3 on 2021-01-21 07:12
from __future__ import unicode_literals
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("client_events", "0023_auto_20210120_2307"),
    ]

    operations = [
        migrations.RenameField(
            model_name="printjobevent", old_name="state", new_name="temp_state2"
        ),
        migrations.RenameField(
            model_name="printjobevent", old_name="temp_state", new_name="state"
        ),
    ]
