# Generated by Django 3.1.3 on 2020-11-15 08:59

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GcodeFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('file', models.FileField(upload_to='')),
                ('file_hash', models.CharField(max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'file_hash')},
            },
        ),
        migrations.CreateModel(
            name='PredictEventFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('annotated_image', models.ImageField(upload_to='')),
                ('original_image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='PrinterProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('axes_e_inverted', models.BooleanField()),
                ('axes_e_speed', models.IntegerField()),
                ('axes_x_speed', models.IntegerField()),
                ('axes_x_inverted', models.BooleanField()),
                ('axes_y_inverted', models.BooleanField()),
                ('axes_y_speed', models.IntegerField()),
                ('axes_z_inverted', models.BooleanField()),
                ('axes_z_speed', models.IntegerField()),
                ('extruder_count', models.IntegerField()),
                ('extruder_nozzle_diameter', models.FloatField()),
                ('extruder_offsets', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=2), null=True, size=None)),
                ('extruder_shared_nozzle', models.BooleanField()),
                ('heated_bed', models.BooleanField()),
                ('heated_chamber', models.BooleanField()),
                ('model', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('volume_custom_box', models.BooleanField()),
                ('volume_depth', models.FloatField()),
                ('volume_formfactor', models.CharField(max_length=255)),
                ('volume_height', models.FloatField()),
                ('volume_origin', models.CharField(max_length=255)),
                ('volume_width', models.FloatField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'name')},
            },
        ),
        migrations.CreateModel(
            name='PrintJob',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt', models.DateTimeField()),
                ('name', models.CharField(max_length=255)),
                ('gcode_file_hash', models.CharField(max_length=255, null=True)),
                ('last_status', models.CharField(choices=[('STARTED', 'Started'), ('DONE', 'Done'), ('FAILED', 'Failed'), ('CANCELLING', 'Cancelling'), ('CANCELLED', 'Cancelled'), ('RESUMED', 'Resumed')], default='STARTED', max_length=12)),
                ('gcode_file', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='client_events.gcodefile')),
                ('printer_profile', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='client_events.printerprofile')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'name', 'dt')},
            },
        ),
        migrations.CreateModel(
            name='PredictEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('event_data', models.JSONField(null=True)),
                ('plugin_version', models.CharField(max_length=30)),
                ('octoprint_version', models.CharField(max_length=30)),
                ('files', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client_events.predicteventfile')),
                ('print_job', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='client_events.printjob')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OctoPrintEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt', models.DateTimeField(db_index=True)),
                ('event_type', models.CharField(db_index=True, max_length=30)),
                ('event_data', models.JSONField()),
                ('plugin_version', models.CharField(max_length=30)),
                ('octoprint_version', models.CharField(max_length=30)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
