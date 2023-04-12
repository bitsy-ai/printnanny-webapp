# Generated by Django 4.1.7 on 2023-03-30 17:34

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("events", "0037_printjobalert_celery_task_id"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="printjobalert",
            name="image",
        ),
        migrations.AlterField(
            model_name="printjobalert",
            name="id",
            field=models.UUIDField(
                default=uuid.uuid4, editable=False, primary_key=True, serialize=False
            ),
        ),
    ]