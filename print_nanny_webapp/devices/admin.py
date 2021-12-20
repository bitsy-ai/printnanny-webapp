from django.contrib import admin
from print_nanny_webapp.devices.models import Task, TaskStatus

# Register your models here.


@admin.register(TaskStatus)
class TaskStatusAdmin(admin.ModelAdmin):
    list_display = ("status", "task", "created_dt")


@admin.register(Task)
class TaskStatusAdmin(admin.ModelAdmin):
    list_display = ("active", "task_type", "created_dt", "device", "last_status")
