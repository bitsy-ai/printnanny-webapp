# Generated by Django 3.2.9 on 2021-12-04 02:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("devices", "0023_auto_20211204_0212"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="device",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="tasks",
                to="devices.device",
            ),
        ),
    ]
