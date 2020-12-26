from django.urls import path

from .views import (
    horizontal_layouts_view,
    detached_layouts_view,
)

app_name = "layouts"
urlpatterns = [
    path("horizontal", view=horizontal_layouts_view, name="layouts.horizontal"),
    path("detached", view=detached_layouts_view, name="layouts.detached"),
]
