# Generated by Django 4.1.7 on 2023-03-27 23:05

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("events", "0035_auto_20230327_1821"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="pibootcommand",
            name="basepievent_ptr",
        ),
        migrations.RemoveField(
            model_name="pibootstatus",
            name="basepievent_ptr",
        ),
        migrations.RemoveField(
            model_name="picamcommand",
            name="basepievent_ptr",
        ),
        migrations.RemoveField(
            model_name="picamstatus",
            name="basepievent_ptr",
        ),
        migrations.AlterIndexTogether(
            name="pisoftwareupdatecommand",
            index_together=None,
        ),
        migrations.RemoveField(
            model_name="pisoftwareupdatecommand",
            name="basepievent_ptr",
        ),
        migrations.AlterIndexTogether(
            name="pisoftwareupdatestatus",
            index_together=None,
        ),
        migrations.RemoveField(
            model_name="pisoftwareupdatestatus",
            name="basepievent_ptr",
        ),
        migrations.DeleteModel(
            name="BasePiEvent",
        ),
        migrations.DeleteModel(
            name="PiBootCommand",
        ),
        migrations.DeleteModel(
            name="PiBootStatus",
        ),
        migrations.DeleteModel(
            name="PiCamCommand",
        ),
        migrations.DeleteModel(
            name="PiCamStatus",
        ),
        migrations.DeleteModel(
            name="PiSoftwareUpdateCommand",
        ),
        migrations.DeleteModel(
            name="PiSoftwareUpdateStatus",
        ),
    ]
