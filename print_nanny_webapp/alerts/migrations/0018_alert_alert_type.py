# Generated by Django 3.1.3 on 2021-01-17 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alerts', '0017_auto_20210116_1605'),
    ]

    operations = [
        migrations.AddField(
            model_name='alert',
            name='alert_type',
            field=models.CharField(choices=[('COMMAND', 'Remote command status updates'), ('PRINT_PROGRESS', 'Percentage-based print progress'), ('MANUAL_VIDEO_UPLOAD', 'Manually-uploaded video is ready for review'), ('DEFECT', 'Defect detected in print')], default='ALERT', max_length=255),
            preserve_default=False,
        ),
    ]
