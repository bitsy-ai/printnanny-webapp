# Generated by Django 3.1.3 on 2021-01-30 20:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('remote_control', '0034_auto_20210129_2321'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='printerprofile',
            name='volume_custom_box',
        ),
    ]
