# Generated by Django 3.2.12 on 2022-08-23 19:34

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("devices", "0043_alter_pi_favorite"),
    ]

    operations = [
        migrations.DeleteModel(
            name="PublicKey",
        ),
    ]
