# Generated by Django 3.2.12 on 2022-08-12 15:50

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("devices", "0038_auto_20220807_2138"),
    ]

    operations = [
        migrations.DeleteModel(
            name="CloudiotDevice",
        ),
    ]
