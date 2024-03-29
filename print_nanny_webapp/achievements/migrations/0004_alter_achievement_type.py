# Generated by Django 3.2.12 on 2023-02-28 20:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("achievements", "0003_alter_achievement_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="achievement",
            name="type",
            field=models.CharField(
                choices=[
                    ("FreeBeta", "Participated in free beta program"),
                    (
                        "FoundingMember",
                        "Supported PrintNanny by pre-ordering an annual subscription",
                    ),
                    ("Cloud Starter", "Subscribed to PrintNanny Cloud Starter plan"),
                    ("Cloud Scaler", "Subscribed to PrintNanny Cloud Scaler plan"),
                ],
                max_length=24,
            ),
        ),
    ]
