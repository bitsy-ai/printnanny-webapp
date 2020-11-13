from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.decorators import action

from drf_spectacular.utils import extend_schema_field
from drf_spectacular.types import OpenApiTypes

from ..models import OctoPrintEvent, PredictEvent, GcodeFile, PrintJob, PrinterProfile

@extend_schema_field(OpenApiTypes.STR)  # also takes basic python types
class JSONField(serializers.JSONField):
    pass

class OctoPrintEventSerializer(serializers.ModelSerializer):

    class Meta:
        model = OctoPrintEvent
        fields = '__all__'
        read_only_fields = ('user',)


class GcodeFileSerializer(serializers.ModelSerializer):

    class Meta:
        model = GcodeFile
        fields = '__all__'
        read_only_fields = ('user',)

class PrintJobSerializer(serializers.ModelSerializer):

    class Meta:
        model = PrintJob
        fields = '__all__'
        read_only_fields = ('user',)

class PrinterProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = PrinterProfile
        fields = '__all__'
        read_only_fields = ('user',)

    def update_or_create(self, validated_data, user):
        return PrinterProfile.objects.update_or_create(**validated_data, user=user)


class PredictEventSerializer(serializers.ModelSerializer):

    event_data = JSONField()

    class Meta:
        model = PredictEvent
        fields = (
            'dt', 'original_image', 'annotated_image', 'event_data', 'plugin_version', 'octoprint_version',
            'user', 'print_job'
        )

        read_only_fields = ('user',)
        
        # extra_kwargs = {
        #     "url": {"view_name": "api:user-detail", "lookup_field": "id"}
        # }

    # Default `create` and `update` behavior...

    # def create(self, validated_data):
    #     """
    #     We have a bit of extra checking around this in order to provide
    #     descriptive messages when something goes wrong, but this method is
    #     essentially just:
    #         return ExampleModel.objects.create(**validated_data)
    #     If there are many to many fields present on the instance then they
    #     cannot be set until the model is instantiated, in which case the
    #     implementation is like so:
    #         example_relationship = validated_data.pop('example_relationship')
    #         instance = ExampleModel.objects.create(**validated_data)
    #         instance.example_relationship = example_relationship
    #         return instance
    #     The default implementation also does not handle nested relationships.
    #     If you want to support writable nested relationships you'll need
    #     to write an explicit `.create()` method.
    #     """
    #     raise_errors_on_nested_writes('create', self, validated_data)

    #     ModelClass = self.Meta.model

    #     # Remove many-to-many relationships from validated_data.
    #     # They are not valid arguments to the default `.create()` method,
    #     # as they require that the instance has already been saved.
    #     info = model_meta.get_field_info(ModelClass)
    #     many_to_many = {}
    #     for field_name, relation_info in info.relations.items():
    #         if relation_info.to_many and (field_name in validated_data):
    #             many_to_many[field_name] = validated_data.pop(field_name)

    #     # get or create fields that are read-only to api clients
    #     read_only_fields = self._get_or_create_read_only_fields(validated_data)

    #     try:
    #         instance = ModelClass._default_manager.create(**validated_data)
    #     except TypeError:
    #         tb = traceback.format_exc()
    #         msg = (
    #             'Got a `TypeError` when calling `%s.%s.create()`. '
    #             'This may be because you have a writable field on the '
    #             'serializer class that is not a valid argument to '
    #             '`%s.%s.create()`. You may need to make the field '
    #             'read-only, or override the %s.create() method to handle '
    #             'this correctly.\nOriginal exception was:\n %s' %
    #             (
    #                 ModelClass.__name__,
    #                 ModelClass._default_manager.name,
    #                 ModelClass.__name__,
    #                 ModelClass._default_manager.name,
    #                 self.__class__.__name__,
    #                 tb
    #             )
    #         )
    #         raise TypeError(msg)

    #     # Save many-to-many relationships after the instance is created.
    #     if many_to_many:
    #         for field_name, value in many_to_many.items():
    #             field = getattr(instance, field_name)
    #             field.set(value)

    #     return instance
