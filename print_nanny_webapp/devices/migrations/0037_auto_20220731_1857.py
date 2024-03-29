# Generated by Django 3.2.12 on 2022-07-31 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("django_nats_nkeys", "0001_initial"),
        ("devices", "0036_pi_setup_finished"),
    ]

    operations = [
        migrations.CreateModel(
            name="PiNatsApp",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("deleted", models.DateTimeField(editable=False, null=True)),
                ("name", models.CharField(max_length=255)),
                (
                    "json",
                    models.JSONField(
                        help_text="Output of `nsc describe account`", max_length=255
                    ),
                ),
                (
                    "organization",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="nats_pi_apps",
                        to="django_nats_nkeys.natsorganization",
                    ),
                ),
                (
                    "organization_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="nats_pi_apps",
                        to="django_nats_nkeys.natsorganizationuser",
                    ),
                ),
                (
                    "pi",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="devices.pi"
                    ),
                ),
            ],
        ),
        migrations.AddConstraint(
            model_name="pinatsapp",
            constraint=models.UniqueConstraint(
                fields=("name", "organization"), name="unique_app_name_per_org"
            ),
        ),
        migrations.AddConstraint(
            model_name="pinatsapp",
            constraint=models.UniqueConstraint(
                condition=models.Q(("deleted", None)),
                fields=("pi",),
                name="unique_nats_app_per_pi",
            ),
        ),
    ]
