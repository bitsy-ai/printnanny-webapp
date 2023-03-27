# Generated by Django 3.2.12 on 2023-03-27 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("devices", "0059_webrtcstream_mountpoint"),
    ]

    operations = [
        migrations.AddField(
            model_name="networksettings",
            name="deleted_by_cascade",
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AddField(
            model_name="pi",
            name="deleted_by_cascade",
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AddField(
            model_name="pinatsapp",
            name="deleted_by_cascade",
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AddField(
            model_name="systeminfo",
            name="deleted_by_cascade",
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AddField(
            model_name="webrtcstream",
            name="deleted_by_cascade",
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AlterField(
            model_name="networksettings",
            name="deleted",
            field=models.DateTimeField(db_index=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name="pi",
            name="deleted",
            field=models.DateTimeField(db_index=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name="pinatsapp",
            name="deleted",
            field=models.DateTimeField(db_index=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name="systeminfo",
            name="deleted",
            field=models.DateTimeField(db_index=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name="webrtcstream",
            name="deleted",
            field=models.DateTimeField(db_index=True, editable=False, null=True),
        ),
    ]
