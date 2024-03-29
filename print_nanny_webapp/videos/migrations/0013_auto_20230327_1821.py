# Generated by Django 3.2.12 on 2023-03-27 18:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("videos", "0012_auto_20230326_1736"),
    ]

    operations = [
        migrations.AddField(
            model_name="videorecording",
            name="deleted_by_cascade",
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AddField(
            model_name="videorecordingpart",
            name="deleted_by_cascade",
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AlterField(
            model_name="videorecording",
            name="deleted",
            field=models.DateTimeField(db_index=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name="videorecordingpart",
            name="deleted",
            field=models.DateTimeField(db_index=True, editable=False, null=True),
        ),
    ]
