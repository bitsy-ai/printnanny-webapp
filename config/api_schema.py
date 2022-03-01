from drf_yasg.generators import OpenAPISchemaGenerator
import logging


class CustomOpenAPISchemaGenerator(OpenAPISchemaGenerator):
    def determine_path_prefix(self, paths):
        return self._gen.determine_path_prefix(paths)
