# Generated by Django 3.1.7 on 2021-04-06 06:12

from django.db import migrations, models
import print_nanny_webapp.alerts.models


class Migration(migrations.Migration):

    dependencies = [
        ('alerts', '0047_printsessionalert_annotated_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='printsessionalert',
            name='annotated_video',
            field=models.FileField(upload_to=print_nanny_webapp.alerts.models._upload_to),
        ),
    ]
