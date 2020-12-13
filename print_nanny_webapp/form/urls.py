from django.urls import path

from .views import (
    form_advanced_view,
    form_basic_view,
    form_editors_view,
    form_elements_view,
    form_fileuploads_view,
    form_validation_view,
    form_wizard_view,
)


app_name = "form"
urlpatterns = [
    path("advanced", view=form_advanced_view, name="form.advanced"),
    path("basic", view=form_basic_view, name="form.basic"),
    path("editors", view=form_editors_view, name="form.editors"),
    path("elements", view=form_elements_view, name="form.elements"),
    path("fileuploads", view=form_fileuploads_view, name="form.fileuploads"),
    path("validation", view=form_validation_view, name="form.validation"),
    path("wizard", view=form_wizard_view, name="form.wizard"),
]
