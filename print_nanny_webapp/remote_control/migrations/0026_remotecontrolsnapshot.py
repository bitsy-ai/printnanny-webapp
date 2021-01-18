# Generated by Django 3.1.3 on 2021-01-18 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('remote_control', '0025_auto_20210118_1114'),
    ]

    operations = [
        migrations.CreateModel(
            name='RemoteControlSnapshot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='uploads/remote_control_snapshot/%Y/%m/%d/')),
                ('command', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='snapshot', to='remote_control.remotecontrolcommand')),
            ],
        ),
    ]
