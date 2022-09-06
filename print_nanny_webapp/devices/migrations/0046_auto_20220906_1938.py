# Generated by Django 3.2.12 on 2022-09-06 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0045_auto_20220826_2146'),
    ]

    operations = [
        migrations.AddField(
            model_name='systeminfo',
            name='bootfs_size',
            field=models.IntegerField(default=0, help_text='Size of /dev/mmcblk0p1 filesystem in bytes'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='systeminfo',
            name='bootfs_used',
            field=models.IntegerField(default=0, help_text='Space used in /dev/mmcblk0p1 filesystem in bytes'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='systeminfo',
            name='datafs_size',
            field=models.IntegerField(default=0, help_text='Size of /dev/mmcblk0p4 filesystem in bytes'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='systeminfo',
            name='datafs_used',
            field=models.IntegerField(default=0, help_text='Space used in /dev/mmcblk0p4 filesystem in bytes'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='systeminfo',
            name='rootfs_size',
            field=models.IntegerField(default=0, help_text='Size of /dev/root filesystem in bytes'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='systeminfo',
            name='rootfs_used',
            field=models.IntegerField(default=0, help_text='Space used in /dev/root filesystem in bytes'),
            preserve_default=False,
        ),
    ]
