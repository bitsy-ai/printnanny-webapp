# Generated by Django 4.1.7 on 2023-05-27 23:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("workspaces", "0002_workspace_description"),
    ]

    operations = [
        migrations.AddField(
            model_name="workspace",
            name="icon",
            field=models.ImageField(null=True, upload_to=""),
        ),
    ]
