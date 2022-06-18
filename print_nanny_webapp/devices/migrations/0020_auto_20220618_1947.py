# Generated by Django 3.2.12 on 2022-06-18 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0019_auto_20220618_1850'),
    ]

    operations = [
        migrations.AddField(
            model_name='systeminfo',
            name='os_release_json',
            field=models.JSONField(default=dict, help_text='Full contents of /etc/os-release in key:value format'),
        ),
        migrations.AddField(
            model_name='systeminfo',
            name='os_variant_id',
            field=models.CharField(default='printnanny-octoprint', help_text='PrintNanny OS VARIANT_ID from /etc/os-release', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterIndexTogether(
            name='systeminfo',
            index_together={('os_build_id', 'os_variant_id', 'os_version_id', 'device'), ('device', 'created_dt', 'updated_dt')},
        ),
        migrations.RemoveField(
            model_name='systeminfo',
            name='hardware',
        ),
    ]
