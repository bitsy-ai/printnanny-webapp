# Generated by Django 3.1.3 on 2021-02-06 22:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        (
            "remote_control",
            "0002_auto_20201126_1453_squashed_0040_octoprintdevice_configs",
        ),
        ("ml_ops", "0003_auto_20210206_1259"),
    ]

    operations = [
        migrations.CreateModel(
            name="Experiment",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_dt", models.DateTimeField(auto_now_add=True)),
                ("active", models.BooleanField(default=False)),
                ("name", models.CharField(max_length=255)),
                ("hypothesis", models.CharField(max_length=255)),
                ("notion_url", models.CharField(max_length=255, null=True)),
                (
                    "control",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="control",
                        to="ml_ops.modelartifact",
                    ),
                ),
                (
                    "treatments",
                    models.ManyToManyField(
                        related_name="treatment", to="ml_ops.ModelArtifact"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ExperimentDeviceConfig",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_dt", models.DateTimeField(auto_now_add=True)),
                ("experiment_group", models.IntegerField()),
                (
                    "device",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="remote_control.octoprintdevice",
                    ),
                ),
                (
                    "experiment",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ml_ops.experiment",
                    ),
                ),
            ],
        ),
    ]
