# Generated by Django 3.2.9 on 2021-12-24 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("devices", "0036_alter_task_task_type"),
    ]

    operations = [
        migrations.AddField(
            model_name="device",
            name="monitoring_active",
            field=models.BooleanField(default=False),
        ),
    ]
