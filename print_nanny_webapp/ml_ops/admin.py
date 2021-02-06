from django.contrib import admin


from .models import ModelArtifact

def deploy_model(modeladmin, request, queryset):
    pass

@admin.register(ModelArtifact)
class ModelArtifactAdmin(admin.ModelAdmin):
    fields = ("version", "labels", "model", "metadata", "created_dt")

    actions = [deploy_model]


