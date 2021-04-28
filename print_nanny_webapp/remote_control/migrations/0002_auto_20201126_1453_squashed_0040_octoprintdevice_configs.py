# Generated by Django 3.1.7 on 2021-04-28 19:15

import datetime
from django.conf import settings
import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import print_nanny_webapp.utils.storages


class Migration(migrations.Migration):

    dependencies = [
        ('remote_control', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        # ('client_events', '0002_predictsession_channel_name_squashed_0009_auto_20201228_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='printjob',
            name='gcode_file',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='remote_control.gcodefile'),
        ),
        migrations.AlterField(
            model_name='printjob',
            name='printer_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='remote_control.printerprofile'),
        ),
        migrations.RemoveField(
            model_name='printjob',
            name='gcode_file_hash',
        ),
        migrations.AddField(
            model_name='printerprofile',
            name='octoprint_id',
            field=models.CharField(db_index=True, default=0, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='printerprofile',
            unique_together={('user', 'octoprint_id')},
        ),
        migrations.CreateModel(
            name='OctoPrintDevice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_dt', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('name', models.CharField(max_length=255)),
                ('public_key', models.TextField()),
                ('fingerprint', models.CharField(max_length=255)),
                ('cloudiot_device', django.contrib.postgres.fields.jsonb.JSONField()),
                ('cloudiot_device_num_id', models.BigIntegerField()),
                ('model', models.CharField(max_length=255)),
                ('platform', models.CharField(max_length=255)),
                ('cpu_flags', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), size=None)),
                ('hardware', models.CharField(max_length=255)),
                ('revision', models.CharField(max_length=255)),
                ('serial', models.CharField(max_length=255)),
                ('cores', models.IntegerField()),
                ('ram', models.IntegerField()),
                ('python_version', models.CharField(max_length=255)),
                ('pip_version', models.CharField(max_length=255)),
                ('virtualenv', models.CharField(max_length=255)),
                ('octoprint_version', models.CharField(max_length=255)),
                ('plugin_version', models.CharField(max_length=255)),
                ('print_nanny_client_version', models.CharField(max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('cloudiot_device_name', models.CharField(default='serial-1234', max_length=255)),
                ('monitoring_active', models.BooleanField(default=False)),
                ('configs', models.JSONField(default=[])),
            ],
            options={
                'unique_together': {('user', 'serial')},
            },
        ),
        migrations.AddField(
            model_name='printjob',
            name='octoprint_device',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='remote_control.octoprintdevice'),
        ),
        migrations.AlterField(
            model_name='printerprofile',
            name='axes_e_inverted',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='printerprofile',
            name='axes_e_speed',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='printerprofile',
            name='axes_x_inverted',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='printerprofile',
            name='axes_x_speed',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='printerprofile',
            name='axes_y_inverted',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='printerprofile',
            name='axes_y_speed',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='printerprofile',
            name='axes_z_inverted',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='printerprofile',
            name='axes_z_speed',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='printerprofile',
            name='extruder_count',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='printerprofile',
            name='extruder_nozzle_diameter',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='printerprofile',
            name='extruder_shared_nozzle',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='printerprofile',
            name='heated_bed',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='printerprofile',
            name='heated_chamber',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='printerprofile',
            name='volume_depth',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='printerprofile',
            name='volume_formfactor',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='printerprofile',
            name='volume_height',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='printerprofile',
            name='volume_origin',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='printerprofile',
            name='volume_width',
            field=models.FloatField(null=True),
        ),
        migrations.RenameField(
            model_name='printerprofile',
            old_name='octoprint_id',
            new_name='octoprint_key',
        ),
        migrations.AddField(
            model_name='printerprofile',
            name='octoprint_device',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='remote_control.octoprintdevice'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='printerprofile',
            unique_together={('user', 'octoprint_key')},
        ),
        migrations.AddField(
            model_name='gcodefile',
            name='octoprint_device',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='remote_control.octoprintdevice'),
        ),
        migrations.AddField(
            model_name='printjob',
            name='created_dt',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2021, 1, 18, 18, 40, 9, 137640, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='printjob',
            name='updated_dt',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterUniqueTogether(
            name='printjob',
            unique_together={('user', 'name', 'created_dt')},
        ),
        migrations.RemoveField(
            model_name='printjob',
            name='dt',
        ),
        migrations.AddField(
            model_name='printjob',
            name='progress',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={}),
        ),
        migrations.AlterField(
            model_name='printjob',
            name='last_status',
            field=models.CharField(choices=[('Error', 'Error'), ('PrintCancelled', 'PrintCancelled'), ('PrintCancelling', 'PrintCancelling'), ('PrintDone', 'PrintDone'), ('PrintFailed', 'PrintFailed'), ('PrintPaused', 'PrintPaused'), ('PrintResumed', 'PrintResumed'), ('PrintStarted', 'PrintStarted')], default='PrintStarted', max_length=56),
        ),
        migrations.CreateModel(
            name='RemoteControlCommand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_dt', models.DateTimeField(auto_now_add=True)),
                ('command', models.CharField(choices=[('MonitoringStop', 'Stop Print Nanny Monitoring'), ('MonitoringStart', 'Start Print Nanny Monitoring'), ('Snapshot', 'Capture a webcam snapshot'), ('PrintStart', 'Start Print'), ('MoveNozzle', 'Move Nozzle'), ('PrintStop', 'Stop Print'), ('PrintPause', 'Pause Print'), ('PrintResume', 'Resume Print')], max_length=255)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commands', to='remote_control.octoprintdevice')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('iotcore_response', django.contrib.postgres.fields.jsonb.JSONField(default={})),
                ('received', models.BooleanField(default=False)),
                ('success', models.BooleanField(null=True)),
                ('metadata', django.contrib.postgres.fields.jsonb.JSONField(default={})),
            ],
        ),
        migrations.RemoveField(
            model_name='printerprofile',
            name='volume_custom_box',
        ),
        migrations.AddField(
            model_name='printerprofile',
            name='volume_custom_box',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={}),
        ),
        migrations.CreateModel(
            name='RemoteControlSnapshot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(storage=print_nanny_webapp.utils.storages.PublicGoogleCloudStorage(), upload_to='uploads/remote_control_snapshot/%Y/%m/%d/')),
                ('command', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='snapshots', to='remote_control.remotecontrolcommand')),
                ('created_dt', models.DateTimeField(auto_now_add=True, default=datetime.datetime(2021, 1, 19, 4, 15, 19, 171717, tzinfo=utc))),
            ],
        ),
    ]
