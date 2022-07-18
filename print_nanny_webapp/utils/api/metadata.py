from drf_spectacular.generators import SchemaGenerator, EndpointEnumerator
from rest_framework import views, viewsets
from rest_framework.schemas.generators import (
)
from rest_framework.settings import api_settings
from rest_framework.schemas.generators import BaseSchemaGenerator

from drf_spectacular.extensions import OpenApiViewExtension
from drf_spectacular.plumbing import (
    error,
    get_class,
)
from drf_spectacular.settings import spectacular_settings

# drf_spectacular EndpointEnumerator excludes OPTIONS method, but we want to include OPTIONS in generated schema
class CustomEndpointEnumerator(EndpointEnumerator):
    def get_allowed_methods(self, callback):
        methods = super().get_allowed_methods(callback)
        return [
            method for method in methods if method not in ("HEAD", "TRACE", "CONNECT")
        ]


class CustomSchemaGenerator(SchemaGenerator):
    endpoint_inspector_cls = CustomEndpointEnumerator

    def create_view(self, callback, method, request=None):
        """
        customized create_view which is called when all routes are traversed. part of this
        is instantiating views with default params. in case of custom routes (@action) the
        custom AutoSchema is injected properly through 'initkwargs' on view. However, when
        decorating plain views like retrieve, this initialization logic is not running.
        Therefore forcefully set the schema if @extend_schema decorator was used.
        """
        override_view = OpenApiViewExtension.get_match(callback.cls)
        if override_view:
            original_cls = callback.cls
            callback.cls = override_view.view_replacement()

        # we refrain from passing request and deal with it ourselves in parse()
        view = BaseSchemaGenerator.create_view(self, callback, method, None)

        # drf-yasg compatibility feature. makes the view aware that we are running
        # schema generation and not a real request.
        view.swagger_fake_view = True

        # callback.cls is hosted in urlpatterns and is therefore not an ephemeral modification.
        # restore after view creation so potential revisits have a clean state as basis.
        if override_view:
            callback.cls = original_cls

        # metadata is a special action handled by drf's base view class, which serves extra metadata about fields. used for form building.
        if method == "OPTIONS":
            action = getattr(view, method.lower())
        elif isinstance(view, viewsets.ViewSetMixin):
            action = getattr(view, view.action)
        elif isinstance(view, views.APIView):
            action = getattr(view, method.lower())
        else:
            error(
                "Using not supported View class. Class must be derived from APIView "
                "or any of its subclasses like GenericApiView, GenericViewSet."
            )
            return view

        action_schema = getattr(action, "kwargs", {}).get("schema", None)
        if not action_schema:
            print("No action schema found, returning view", view)

            # there is no method/action customized schema so we are done here.
            return view

        # action_schema is either a class or instance. when @extend_schema is used, it
        # is always a class to prevent the weakref reverse "schema.view" bug for multi
        # annotations. The bug is prevented by delaying the instantiation of the schema
        # class until create_view (here) and not doing it immediately in @extend_schema.

        action_schema_class = get_class(action_schema)
        print("Got action_schema_class for view ", method, action_schema_class, view)

        view_schema_class = get_class(callback.cls.schema)
        if not issubclass(action_schema_class, view_schema_class):

            # this handles the case of having a manually set custom AutoSchema on the
            # view together with extend_schema. In most cases, the decorator mechanics
            # prevent extend_schema from having access to the view's schema class. So
            # extend_schema is forced to use DEFAULT_SCHEMA_CLASS as fallback base class
            # instead of the correct base class set in view. We remedy this chicken-egg
            # problem here by rearranging the class hierarchy.
            mro = (
                tuple(
                    cls
                    for cls in action_schema_class.__mro__
                    if cls not in api_settings.DEFAULT_SCHEMA_CLASS.__mro__
                )
                + view_schema_class.__mro__
            )
            action_schema_class = type("ExtendedRearrangedSchema", mro, {})

        view.schema = action_schema_class()
        return view
