# Generated by Django 3.2.12 on 2022-10-26 22:54

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("devices", "0048_auto_20220906_2040"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="pi",
            name="edition",
        ),
    ]
