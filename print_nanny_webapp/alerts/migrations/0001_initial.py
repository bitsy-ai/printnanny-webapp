# Generated by Django 3.1.3 on 2021-01-11 04:41

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import print_nanny_webapp.alerts.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
        ('remote_control', '0019_auto_20210109_2034'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_dt', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_dt', models.DateTimeField(auto_now=True, db_index=True)),
                ('dismissed', models.BooleanField(default=True)),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_alerts.alert_set+', to='contenttypes.contenttype')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
        ),
        migrations.CreateModel(
            name='ManualVideoUploadAlert',
            fields=[
                ('alert_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='alerts.alert')),
                ('job_status', models.CharField(choices=[('Processing', 'Processing'), ('SUCCESS', 'Success'), ('FAILURE', 'Failure'), ('CANCELLED', 'Cancelled')], default='Processing', max_length=32)),
                ('dataframe', models.FileField(null=True, upload_to=print_nanny_webapp.alerts.models._upload_to)),
                ('original_video', models.FileField(null=True, upload_to=print_nanny_webapp.alerts.models._upload_to)),
                ('annotated_video', models.FileField(null=True, upload_to=print_nanny_webapp.alerts.models._upload_to)),
                ('feedback', models.BooleanField(null=True)),
                ('length', models.FloatField(null=True)),
                ('fps', models.FloatField(null=True)),
                ('notify_seconds', models.IntegerField(null=True)),
                ('notify_timecode', models.CharField(max_length=32, null=True)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('alerts.alert',),
        ),
        migrations.CreateModel(
            name='RemoteControlCommandAlert',
            fields=[
                ('alert_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='alerts.alert')),
                ('alert_type', models.CharField(choices=[('RECEIVED', 'Command was received by Raspberry Pi'), ('SUCCESS', 'Command executed sucessfully'), ('FAILED', 'Command execution failed')], max_length=255)),
                ('command', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='remote_control.remotecontrolcommand')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('alerts.alert',),
        ),
        migrations.CreateModel(
            name='DefectAlert',
            fields=[
                ('alert_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='alerts.alert')),
                ('last_action', models.CharField(choices=[('PENDING', 'Pending User Action'), ('RESUME_ALERTS', 'Resume for Print Job'), ('CANCEL_PRINT', 'Cancel Print Job Cancel')], default='PENDING', max_length=16)),
                ('tags', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), default=['defect-alert'], size=None)),
                ('print_job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='remote_control.printjob')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('alerts.alert',),
        ),
        migrations.CreateModel(
            name='AlertPlot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=print_nanny_webapp.alerts.models._upload_to)),
                ('html', models.FileField(upload_to=print_nanny_webapp.alerts.models._upload_to)),
                ('title', models.CharField(max_length=65)),
                ('description', models.CharField(max_length=255)),
                ('function', models.CharField(max_length=65)),
                ('alert', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alerts.manualvideouploadalert')),
            ],
        ),
        migrations.CreateModel(
            name='ProgressAlert',
            fields=[
                ('alert_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='alerts.alert')),
                ('progress', models.IntegerField(default=0)),
                ('tags', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), default=['progress-alert'], size=None)),
                ('print_job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='remote_control.printjob')),
            ],
            options={
                'unique_together': {('print_job_id', 'progress')},
            },
            bases=('alerts.alert',),
        ),
    ]
