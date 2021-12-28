from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Release


class ReleaseListView(ListView):
    template_name = "releases/releases-list.html"
    model = Release


class ReleaseDetailView(DetailView):
    template_name = "releases/release-list.html"
    slug_field = "name"
    model = Release
