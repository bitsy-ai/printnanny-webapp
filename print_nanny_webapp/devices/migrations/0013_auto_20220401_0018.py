# Generated by Django 3.2.12 on 2022-04-01 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("devices", "0012_auto_20220305_2030"),
    ]

    operations = [
        migrations.AddField(
            model_name="janusstream",
            name="admin_port",
            field=models.IntegerField(default=7088),
        ),
        migrations.AddField(
            model_name="janusstream",
            name="api_domain",
            field=models.CharField(default="aurora", max_length=255),
        ),
        migrations.AddField(
            model_name="janusstream",
            name="api_port",
            field=models.IntegerField(default=8088),
        ),
        migrations.AddField(
            model_name="janusstream",
            name="rtp_domain",
            field=models.CharField(default="aurora", max_length=255),
        ),
        migrations.AddField(
            model_name="janusstream",
            name="ws_port",
            field=models.IntegerField(default=8188),
        ),
    ]
