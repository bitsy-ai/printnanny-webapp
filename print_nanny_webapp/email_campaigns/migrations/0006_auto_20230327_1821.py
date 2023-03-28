# Generated by Django 3.2.12 on 2023-03-27 18:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("email_campaigns", "0005_alter_emailtrackingevent_esp_event"),
    ]

    operations = [
        migrations.AddField(
            model_name="campaign",
            name="deleted_by_cascade",
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AddField(
            model_name="emailmessage",
            name="deleted_by_cascade",
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AddField(
            model_name="emailtrackingevent",
            name="deleted_by_cascade",
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AlterField(
            model_name="campaign",
            name="deleted",
            field=models.DateTimeField(db_index=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name="emailmessage",
            name="deleted",
            field=models.DateTimeField(db_index=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name="emailtrackingevent",
            name="deleted",
            field=models.DateTimeField(db_index=True, editable=False, null=True),
        ),
    ]