# Generated by Django 3.2.12 on 2023-03-27 18:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("moonraker", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="moonrakerserver",
            name="deleted_by_cascade",
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AlterField(
            model_name="moonrakerserver",
            name="deleted",
            field=models.DateTimeField(db_index=True, editable=False, null=True),
        ),
    ]