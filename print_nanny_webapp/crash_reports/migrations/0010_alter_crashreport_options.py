# Generated by Django 3.2.12 on 2023-01-30 02:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("crash_reports", "0009_auto_20230115_0001"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="crashreport",
            options={"ordering": ["-created_dt"]},
        ),
    ]