# Generated by Django 3.2.12 on 2022-11-05 19:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("django_nats_nkeys", "0009_auto_20221105_1755"),
        ("devices", "0050_auto_20221102_2132"),
    ]

    operations = [
        migrations.AddField(
            model_name="pinatsapp",
            name="bearer",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="pinatsapp",
            name="organization",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="devices_pinatsapp",
                to="django_nats_nkeys.natsorganization",
            ),
        ),
        migrations.AlterField(
            model_name="pinatsapp",
            name="organization_user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="devices_pinatsapp",
                to="django_nats_nkeys.natsorganizationuser",
            ),
        ),
    ]
