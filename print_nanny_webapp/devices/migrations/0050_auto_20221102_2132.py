# Generated by Django 3.2.12 on 2022-11-02 21:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("devices", "0049_remove_pi_edition"),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name="systeminfo",
            index_together={
                ("pi", "created_dt", "updated_dt"),
                ("os_build_id", "os_version_id", "pi"),
            },
        ),
        migrations.RemoveField(
            model_name="systeminfo",
            name="os_variant_id",
        ),
    ]
