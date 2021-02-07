from django.contrib import admin


from .models import ModelArtifact, Experiment, ExperimentDeviceConfig


@admin.register(ModelArtifact)
class ModelArtifactAdmin(admin.ModelAdmin):
    list_display = (
        "created_dt",
        "artifacts",
        "artifact_types",
        "labels",
        "metadata",
        "version",
    )


def activate_experiment(modeladmin, request, queryset):
    if len(queryset) > 1:
        raise ValueError(
            f"You selected {len(queryset)} experiments, but only one experiment can be active at a time"
        )
    # de-activate all experiments, activate selected experiment
    experiment = queryset.first()
    experiment.activate()
    # initialize device configs

    for device in OctoPrintDevice.objects.all().iterator():
        experiment_group = experiment.randomize_group()
        config = ExperimentDeviceConfig(
            device=device,
            experiment_group=experiment_group,
            experiment=exerpiment
        )
        config.save()
        config.publish()


@admin.register(Experiment)
class ExperimentAdmin(admin.ModelAdmin):
    fields = (
        "created_dt" "active",
        "name",
        "hypothesis",
        "notion_url",
        "control",
        "treatments",
    )

    actions = [activate_experiment]


@admin.register(ExperimentDeviceConfig)
class ExperimentDeviceConfig(admin.ModelAdmin):
    fields = (
        "artifacts",
        "artifact_types",
        "created_dt" "labels",
        "metadata",
        "model",
        "version",
    )
