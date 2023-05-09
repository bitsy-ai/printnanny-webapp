# Generated by Django 4.1.7 on 2023-05-09 08:28

from django.db import migrations, models
import print_nanny_webapp.videos.models


class Migration(migrations.Migration):
    dependencies = [
        ("videos", "0016_demosubmission"),
    ]

    operations = [
        migrations.AlterField(
            model_name="demosubmission",
            name="result",
            field=models.FileField(
                max_length=255,
                upload_to=print_nanny_webapp.videos.models.demo_result_filepath,
            ),
        ),
        migrations.AlterField(
            model_name="demosubmission",
            name="submission",
            field=models.FileField(
                max_length=255,
                upload_to=print_nanny_webapp.videos.models.demo_submission_filepath,
            ),
        ),
    ]
