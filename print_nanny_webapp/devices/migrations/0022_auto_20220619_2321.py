# Generated by Django 3.2.12 on 2022-06-19 23:21

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0021_auto_20220619_2227'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AnsibleFactsd',
        ),
        migrations.AddField(
            model_name='device',
            name='license_key',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AlterIndexTogether(
            name='device',
            index_together={('hostname', 'created_dt')},
        ),
        migrations.DeleteModel(
            name='License',
        ),
        migrations.RemoveField(
            model_name='device',
            name='updated_dt',
        ),
    ]
