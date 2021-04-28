# Generated by Django 3.1.7 on 2021-04-28 04:51

from django.db import migrations, models
import print_nanny_webapp.utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('alerts', '0073_auto_20210427_2146'),
    ]

    operations = [
        migrations.AddField(
            model_name='alerteventsettings',
            name='alert_methods',
            field=print_nanny_webapp.utils.fields.ChoiceArrayField(base_field=models.CharField(choices=[('PrintProgress', 'Print progress notifications'), ('PrintHealth', 'Print health alerts'), ('PrintStatus', 'Print status updates (started, paused, resumed, cancelling, cancelled, failed)')], max_length=255), blank=True, default=('UI', 'EMAIL'), size=None),
        ),
        migrations.AlterField(
            model_name='alert',
            name='alert_method',
            field=models.CharField(choices=[('UI', 'Receive Print Nanny UI notifications'), ('EMAIL', 'Receive email notifications'), ('DISCORD', 'Receive notifications through Discord'), ('PARTNER_3DGEEKS', 'Receive notifications in 3D Geeks mobile app')], max_length=255),
        ),
        migrations.DeleteModel(
            name='AlertMethodSettings',
        ),
    ]
