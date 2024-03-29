# Generated by Django 3.2.12 on 2023-01-11 02:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("devices", "0057_alter_systeminfo_os_build_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="systeminfo",
            name="os_build_id",
            field=models.CharField(
                blank=True,
                help_text="PrintNanny OS BUILD_ID from /etc/os-release",
                max_length=255,
            ),
        ),
        migrations.AlterField(
            model_name="systeminfo",
            name="os_version_id",
            field=models.CharField(
                blank=True,
                help_text="PrintNanny OS VERSION_ID from /etc/os-release",
                max_length=255,
            ),
        ),
    ]
