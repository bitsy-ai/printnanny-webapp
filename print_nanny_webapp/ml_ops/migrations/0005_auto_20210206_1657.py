# Generated by Django 3.1.3 on 2021-02-07 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ml_ops', '0004_experiment_experimentdeviceconfig'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experiment',
            name='treatments',
            field=models.ManyToManyField(null=True, related_name='treatment', to='ml_ops.ModelArtifact'),
        ),
    ]
