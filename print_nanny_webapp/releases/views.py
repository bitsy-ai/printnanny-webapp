from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Release
from .choices import ReleaseVariant, ReleaseChannel


class ReleaseListView(ListView):
    template_name = "releases/releases-list.html"
    model = Release

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["desktop_stable"] = Release.objects.filter(
            variant=ReleaseVariant.DESKTOP, release_channel=ReleaseChannel.STABLE
        ).first()

        context["desktop_nightly"] = Release.objects.filter(
            variant=ReleaseVariant.DESKTOP, release_channel=ReleaseChannel.NIGHTLY
        )

        return context


class ReleaseDetailView(DetailView):
    template_name = "releases/release-list.html"
    slug_field = "name"
    model = Release
