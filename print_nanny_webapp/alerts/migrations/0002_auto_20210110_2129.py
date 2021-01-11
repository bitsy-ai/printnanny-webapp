# Generated by Django 3.1.3 on 2021-01-11 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alerts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='remotecontrolcommandalert',
            name='alert_type',
            field=models.CharField(choices=[('RECEIVED', 'Command was received by Raspberry Pi'), ('SUCCESS', 'Command succeeded'), ('FAILED', 'Command failed')], max_length=255),
        ),
    ]
