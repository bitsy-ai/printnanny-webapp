# Generated by Django 3.1.3 on 2020-11-19 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client_events', '0003_auto_20201119_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alertmessage',
            name='last_action',
            field=models.CharField(choices=[('PENDING', 'Pending User Action'), ('RESUME_ALERTS', 'Resume for Print Job'), ('CANCEL_PRINT', 'Cancel Print Job Cancel')], default='PENDING', max_length=16),
        ),
    ]
