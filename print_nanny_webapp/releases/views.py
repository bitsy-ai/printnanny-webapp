from django.shortcuts import render
from django.views.generic.base import TemplateView


class ReleaseListView(TemplateView):
    template_name = "releases/releases-list.html"
