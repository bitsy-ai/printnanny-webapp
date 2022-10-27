from django.contrib import admin

from print_nanny_webapp.achievements.models import Achievement


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ("user", "type", "label", "created_dt")
