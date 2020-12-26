# Generated by Django 3.0.11 on 2020-11-12 05:42

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="TFLiteModel",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_dt", models.DateTimeField(auto_now_add=True)),
                ("modified_dt", models.DateTimeField(auto_now=True)),
                ("labels", models.FileField(upload_to="")),
                ("model", models.FileField(upload_to="")),
                ("metadata", django.contrib.postgres.fields.jsonb.JSONField()),
            ],
        ),
    ]
