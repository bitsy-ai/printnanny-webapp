# Generated by Django 4.1.7 on 2023-05-09 16:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("videos", "0017_alter_demosubmission_result_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="demosubmission",
            name="feedback_adhesion",
            field=models.CharField(
                choices=[
                    ("pass", "Submission received positive (thumbs up) feedback"),
                    ("fail", "Submission received negative (thumbs down) feedback"),
                    ("na", "Submission received N/A (not applicable)"),
                ],
                max_length=25,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="demosubmission",
            name="feedback_nozzle",
            field=models.CharField(
                choices=[
                    ("pass", "Submission received positive (thumbs up) feedback"),
                    ("fail", "Submission received negative (thumbs down) feedback"),
                    ("na", "Submission received N/A (not applicable)"),
                ],
                max_length=25,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="demosubmission",
            name="feedback_print",
            field=models.CharField(
                choices=[
                    ("pass", "Submission received positive (thumbs up) feedback"),
                    ("fail", "Submission received negative (thumbs down) feedback"),
                    ("na", "Submission received N/A (not applicable)"),
                ],
                max_length=25,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="demosubmission",
            name="feedback_raft",
            field=models.CharField(
                choices=[
                    ("pass", "Submission received positive (thumbs up) feedback"),
                    ("fail", "Submission received negative (thumbs down) feedback"),
                    ("na", "Submission received N/A (not applicable)"),
                ],
                max_length=25,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="demosubmission",
            name="feedback_spaghetti",
            field=models.CharField(
                choices=[
                    ("pass", "Submission received positive (thumbs up) feedback"),
                    ("fail", "Submission received negative (thumbs down) feedback"),
                    ("na", "Submission received N/A (not applicable)"),
                ],
                max_length=25,
                null=True,
            ),
        ),
    ]
