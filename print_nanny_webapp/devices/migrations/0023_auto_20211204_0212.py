# Generated by Django 3.2.9 on 2021-12-04 02:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("devices", "0022_alter_systemtaskstatus_status"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="SystemTask",
            new_name="Task",
        ),
        migrations.RenameModel(
            old_name="SystemTaskStatus",
            new_name="TaskStatus",
        ),
        migrations.RenameField(
            model_name="taskstatus",
            old_name="system_task",
            new_name="task",
        ),
        migrations.AlterIndexTogether(
            name="taskstatus",
            index_together={("task", "status")},
        ),
    ]
