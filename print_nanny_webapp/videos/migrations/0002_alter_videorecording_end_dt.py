# Generated by Django 3.2.12 on 2023-01-12 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("videos", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="videorecording",
            name="end_dt",
            field=models.DateTimeField(null=True),
        ),
    ]