# Generated by Django 4.1.7 on 2023-05-27 17:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("workspaces", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="workspace",
            name="description",
            field=models.CharField(
                default="A shared PrintNanny workspace", max_length=255
            ),
            preserve_default=False,
        ),
    ]
