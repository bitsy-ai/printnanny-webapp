from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Release


class ReleaseListView(ListView):
    model = Release


class ReleaseDetailView(DetailView):
    model = Release
