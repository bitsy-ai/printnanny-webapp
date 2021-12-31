from django.apps import apps
from django.contrib import admin

Releases = apps.get_model("releases", "Release")


@admin.register(Releases)
class ModelArtifactAdmin(admin.ModelAdmin):
    list_display = ("created_dt", "id", "name", "zip_url", "variant", "release_channel")
