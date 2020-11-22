# Generated by Django 3.1.3 on 2020-11-22 06:17

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import print_nanny_webapp.alerts.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('remote_control', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimelapseAlert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_dt', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_dt', models.DateTimeField(auto_now=True, db_index=True)),
                ('original_video', models.FileField(null=True, upload_to=print_nanny_webapp.alerts.models.AnnotatedVideo.upload_to)),
                ('annotated_video', models.FileField(null=True, upload_to=print_nanny_webapp.alerts.models.AnnotatedVideo.upload_to)),
                ('dataframe', models.JSONField(null=True)),
                ('summary', models.JSONField(null=True)),
                ('feedback', models.BooleanField(null=True)),
                ('provider_id', models.CharField(db_index=True, max_length=255, null=True)),
                ('seen', models.BooleanField(default=False)),
                ('tags', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), default=['timelapse-alert'], size=None)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DefectAlert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_dt', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_dt', models.DateTimeField(auto_now=True, db_index=True)),
                ('original_video', models.FileField(null=True, upload_to=print_nanny_webapp.alerts.models.AnnotatedVideo.upload_to)),
                ('annotated_video', models.FileField(null=True, upload_to=print_nanny_webapp.alerts.models.AnnotatedVideo.upload_to)),
                ('dataframe', models.JSONField(null=True)),
                ('summary', models.JSONField(null=True)),
                ('feedback', models.BooleanField(null=True)),
                ('provider_id', models.CharField(db_index=True, max_length=255, null=True)),
                ('seen', models.BooleanField(default=False)),
                ('last_action', models.CharField(choices=[('PENDING', 'Pending User Action'), ('RESUME_ALERTS', 'Resume for Print Job'), ('CANCEL_PRINT', 'Cancel Print Job Cancel')], default='PENDING', max_length=16)),
                ('tags', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), default=['defect-alert'], size=None)),
                ('print_job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='remote_control.printjob')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
