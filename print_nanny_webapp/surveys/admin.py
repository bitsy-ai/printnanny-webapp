from django.contrib import admin
from print_nanny_webapp.surveys.models import RemoteAccessSurvey1


@admin.register(RemoteAccessSurvey1)
class RemoteAccessSurvey1Admin(admin.ModelAdmin):
    list_display = ("email", "first_name", "last_name", "created_dt")
    model = RemoteAccessSurvey1
