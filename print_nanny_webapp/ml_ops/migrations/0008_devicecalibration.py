# Generated by Django 3.1.3 on 2021-02-13 10:16

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('remote_control', '0044_remove_octoprintdevice_configs'),
        ('ml_ops', '0007_auto_20210206_1828'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeviceCalibration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_dt', models.DateTimeField(auto_now_add=True)),
                ('updated_dt', models.DateTimeField(auto_now=True)),
                ('mask', django.contrib.postgres.fields.jsonb.JSONField(null=True)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='remote_control.octoprintdevice')),
            ],
        ),
    ]
