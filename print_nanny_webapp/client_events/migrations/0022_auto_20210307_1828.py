# Generated by Django 3.1.7 on 2021-03-08 02:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('remote_control', '0047_remove_printjob_last_status'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('client_events', '0021_auto_20210307_1637'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientevent',
            name='client_event_type',
            field=models.CharField(choices=[('plugin', 'OctoPrint Nanny plugin events'), ('octoprint', 'OctoPrint core and bundled plugins events'), ('octoprint_job', 'OctoPrint print job events')], db_index=True, default='plugin', max_length=255),
        ),
        migrations.AddField(
            model_name='clientevent',
            name='created_dt',
            field=models.DateTimeField(auto_now_add=True, db_index=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='clientevent',
            name='device',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='remote_control.octoprintdevice'),
        ),
        migrations.AddField(
            model_name='clientevent',
            name='event_data',
            field=models.JSONField(default={}),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='clientevent',
            name='octoprint_version',
            field=models.CharField(default='migration_default', max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='clientevent',
            name='plugin_version',
            field=models.CharField(default='migration_default', max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='clientevent',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
