from django.contrib import admin
from .models import Task, TaskStatus


@admin.register(TaskStatus)
class TaskStatusAdmin(admin.ModelAdmin):
    list_display = ("status", "task", "created_dt")


@admin.register(Task)
class TaskStatusAdmin(admin.ModelAdmin):
    list_display = ("created_dt", "device", "last_status")
