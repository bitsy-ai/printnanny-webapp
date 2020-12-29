# Generated by Django 3.1.3 on 2020-12-26 05:19

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_auto_20201206_2005"),
    ]

    operations = [
        migrations.AddField(
            model_name="inviterequest",
            name="created_dt",
            field=models.DateTimeField(
                auto_now_add=True,
                default=datetime.datetime(2020, 12, 26, 5, 19, 51, 310117, tzinfo=utc),
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="inviterequest",
            name="invited",
            field=models.BooleanField(default=False),
        ),
    ]
