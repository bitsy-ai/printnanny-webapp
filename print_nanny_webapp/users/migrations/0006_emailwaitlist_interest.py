# Generated by Django 4.1.7 on 2023-04-25 19:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0005_alter_user_date_joined_alter_user_first_name_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="emailwaitlist",
            name="interest",
            field=models.CharField(
                choices=[
                    (
                        "printnanny",
                        "Subscribe to PrintNanny news and development updates",
                    ),
                    ("sdwire", "Get notified when SDWire is back in stock"),
                ],
                default="printnanny",
                max_length=32,
            ),
        ),
    ]