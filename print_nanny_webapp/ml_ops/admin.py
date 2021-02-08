from django.apps import apps
from django.contrib import admin

ModelArtifact = apps.get_model('ml_ops', 'ModelArtifact')
ExperimentDeviceConfig = apps.get_model('ml_ops', 'ExperimentDeviceConfig')
Experiment = apps.get_model('ml_ops', 'Experiment')

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
    OctoPrintDevice = apps.get_model('remote_control', 'OctoPrintDevice')
    if len(queryset) > 1:
        raise ValueError(
            f"You selected {len(queryset)} experiments, but only one experiment can be active at a time"
        )
    # de-activate all experiments, activate selected experiment
    experiment = queryset.first()
    experiment.activate()
    # initialize device configs

    for device in OctoPrintDevice.objects.all().iterator():
        config = ExperimentDeviceConfig.objects.create(
            device=device,experiment=experiment,
        )
        config.publish()


@admin.register(Experiment)
class ExperimentAdmin(admin.ModelAdmin):
    list_display = (
        "created_dt",
        "active",
        "name",
        "hypothesis",
        "notion_url",
        "control",
        # "treatments",
    )

    actions = [activate_experiment]


@admin.register(ExperimentDeviceConfig)
class ExperimentDeviceConfigAdmin(admin.ModelAdmin):
    list_display = (
        "device",
        "created_dt",
        "experiment",
        "experiment_group",
    )
