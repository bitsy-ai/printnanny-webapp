# Generated by Django 3.2.9 on 2022-01-02 19:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("telemetry", "0023_alter_printerevent_printer_state"),
    ]

    operations = [
        migrations.AddField(
            model_name="telemetryevent",
            name="print_nanny_beta_client_version",
            field=models.CharField(max_length=60, null=True),
        ),
    ]
