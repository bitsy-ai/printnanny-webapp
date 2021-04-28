# Generated by Django 3.1.7 on 2021-04-28 19:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    # replaces = [('remote_control', '0042_auto_20210207_2249'), ('remote_control', '0043_auto_20210207_2332'), ('remote_control', '0044_remove_octoprintdevice_configs'), ('remote_control', '0045_octoprintdevice_monitoring_mode'), ('remote_control', '0046_auto_20210219_1648'), ('remote_control', '0047_remove_printjob_last_status'), ('remote_control', '0048_auto_20210321_1312'), ('remote_control', '0049_auto_20210321_1313')]

    dependencies = [
        ('remote_control', '0041_octoprintdevice_cloudiot_device_path'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='octoprintdevice',
            name='configs',
        ),
        migrations.AddField(
            model_name='octoprintdevice',
            name='monitoring_mode',
            field=models.CharField(choices=[('active_learning', 'Active Learning'), ('lite', 'Lite')], default='lite', max_length=32),
        ),
        migrations.AlterField(
            model_name='remotecontrolcommand',
            name='command',
            field=models.CharField(choices=[('monitoring_stop', 'Stop Print Nanny Monitoring'), ('monitoring_start', 'Start Print Nanny Monitoring'), ('snapshot', 'Capture a webcam snapshot'), ('print_start', 'Start Print'), ('print_stop', 'Stop Print'), ('print_pause', 'Pause Print'), ('print_resume', 'Resume Print'), ('move_nozzle', 'Move Nozzle')], max_length=255),
        ),
        migrations.RemoveField(
            model_name='printjob',
            name='last_status',
        ),
        migrations.RemoveField(
            model_name='printjob',
            name='last_seen',
        ),
        migrations.CreateModel(
            name='PrintSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_dt', models.DateTimeField(db_index=True)),
                ('end_dt', models.DateTimeField(db_index=True, null=True)),
                ('session', models.CharField(db_index=True, max_length=255)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='remote_control.octoprintdevice')),
            ],
            options={
                'unique_together': {('device', 'session')},
            },
        ),
        migrations.AddField(
            model_name='printjob',
            name='print_session',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='remote_control.printsession'),
        ),
    ]
