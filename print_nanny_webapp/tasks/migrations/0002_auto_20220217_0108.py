# Generated by Django 3.2.12 on 2022-02-17 01:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('devices', '0007_auto_20220217_0108'),
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('created_dt', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='devices.device')),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_tasks.task_set+', to='contenttypes.contenttype')),
            ],
            options={
                'ordering': ['-created_dt'],
                'index_together': {('device', 'created_dt')},
            },
        ),
        migrations.CreateModel(
            name='TaskStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('created_dt', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('status', models.CharField(choices=[('failed', 'Task failed.'), ('pending', 'Waiting for device to acknowledge task.'), ('started', 'Task is running.'), ('success', 'Task succeeded.'), ('timeout', 'Task timed out. Please try again.')], default='pending', max_length=16)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='status_set', to='tasks.task')),
            ],
            options={
                'ordering': ['-created_dt'],
                'index_together': {('task', 'status')},
            },
        ),
        migrations.RemoveField(
            model_name='event',
            name='polymorphic_ctype',
        ),
        migrations.RemoveField(
            model_name='event',
            name='user',
        ),
        migrations.RemoveField(
            model_name='testevent',
            name='deviceevent_ptr',
        ),
        migrations.CreateModel(
            name='JanusTask',
            fields=[
                ('task_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='tasks.task')),
                ('task_type', models.CharField(choices=[('cloud_monitor_start', 'Start PrintNanny Monitoring'), ('cloud_monitor_stop', 'Stop PrintNanny Monitoring')], max_length=32)),
                ('cloud_media_stream', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='devices.januscloudmediastream')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('tasks.task',),
        ),
        migrations.DeleteModel(
            name='DeviceEvent',
        ),
        migrations.DeleteModel(
            name='Event',
        ),
        migrations.DeleteModel(
            name='TestEvent',
        ),
    ]
