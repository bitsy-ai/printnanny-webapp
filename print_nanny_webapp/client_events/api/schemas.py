
from drf_spectacular.extensions import OpenApiSerializerFieldExtension
from drf_spectacular.types import OpenApiTypes

# class JSONFieldFix(OpenApiSerializerFieldExtension):
#     target_class = 'rest_framework.serializers'

#     def map_serializer_field(self, auto_schema, direction):
#         print(direction)
#         # equivalent to return {'type': 'string'}
#         return build_basic_type(OpenApiTypes.BINARY)