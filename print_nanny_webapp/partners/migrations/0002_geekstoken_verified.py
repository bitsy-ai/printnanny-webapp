# Generated by Django 3.1.7 on 2021-04-27 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("partners", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="geekstoken",
            name="verified",
            field=models.BooleanField(default=False),
        ),
    ]
