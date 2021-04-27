from django.apps import apps
from rest_framework.viewsets import ViewSet

from print_nanny_webapp.partners.authentication import GeeksTokenAuthentication

from .serializers import GeeksMetadataSerializer

GeeksToken = apps.get_model("partners", "GeeksToken")
OctoPrintDevice = apps.get_model("remote_control", "OctoPrintDevice")


class GeeksViewSet(ViewSet):
    """
    3D Geeks calls this endpoint to validate token & fetch printer metadata
    """

    authentication_classes = [GeeksTokenAuthentication]
