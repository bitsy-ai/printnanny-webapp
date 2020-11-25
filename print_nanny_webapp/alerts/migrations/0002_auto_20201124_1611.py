# Generated by Django 3.1.3 on 2020-11-25 00:11

from django.db import migrations, models
import print_nanny_webapp.alerts.models


class Migration(migrations.Migration):

    dependencies = [
        ('alerts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alertplot',
            name='html',
            field=models.FileField(upload_to=print_nanny_webapp.alerts.models._upload_to),
        ),
        migrations.AlterField(
            model_name='alertplot',
            name='image',
            field=models.ImageField(upload_to=print_nanny_webapp.alerts.models._upload_to),
        ),
    ]
