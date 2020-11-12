from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin, CreateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ViewSet
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.views import APIView
from rest_framework.parsers  import MultiPartParser, FormParser, JSONParser, FileUploadParser

from .serializers import OctoPrintEventSerializer, PredictEventSerializer


from ..models import OctoPrintEvent, PredictEvent

class OctoPrintEventViewSet(CreateModelMixin, GenericViewSet):
    serializer_class = OctoPrintEventSerializer
    queryset = OctoPrintEvent.objects.all()
    lookup_field = "id"
    

    def get_queryset(self, *args, **kwargs):
        return self.queryset.filter(user_id=self.request.user.id)

# class PredictEventViewSet(CreateModelMixin, GenericViewSet):
#     serializer_class = PredictEventSerializer
#     queryset = PredictEvent.objects.all()
#     lookup_field = "id"

#     def get_queryset(self, *args, **kwargs):
#         return self.queryset.filter(user_id=self.request.user.id)



class PredictEventView(APIView):
		# MultiPartParser AND FormParser
		# https://www.django-rest-framework.org/api-guide/parsers/#multipartparser
		# "You will typically want to use both FormParser and MultiPartParser
		# together in order to fully support HTML form data."
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = PredictEventSerializer
    queryset = PredictEvent.objects.all()


    @swagger_auto_schema(
        operation_id='predictEvent', 
        type=openapi.TYPE_OBJECT,
        manual_parameters=[
            openapi.Parameter(
                'dt',
                openapi.IN_FORM,
                required=True,
                type=openapi.TYPE_STRING
            ),
            openapi.Parameter(
                'plugin_version',
                openapi.IN_FORM,
                required=True,
                type=openapi.TYPE_STRING
            ),
            openapi.Parameter(
                    'octoprint_version',
                    openapi.IN_FORM,
                    required=True,
                    type=openapi.TYPE_STRING
            ),
            openapi.Parameter(
                    'event_data',
                    openapi.IN_FORM,
                    required=True,
                    type=openapi.TYPE_OBJECT
            ),                
            openapi.Parameter(
                    'image',
                    openapi.IN_FORM,
                    required=True,
                    type=openapi.TYPE_FILE
                    
            )

        ],
        operation_description="POST /events/predict/")
    def post(self, request, *args, **kwargs):
            serializer = PredictEventSerializer(data=request.data)
            if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


                    