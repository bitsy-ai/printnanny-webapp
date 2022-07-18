from collections import OrderedDict

from rest_framework import serializers, exceptions
from rest_framework.metadata import BaseMetadata
from rest_framework.utils.field_mapping import ClassLookupDict
from rest_framework.request import clone_request

from django.core.exceptions import PermissionDenied
from django.http import Http404
from django.utils.encoding import force_str


class FormMetadata(BaseMetadata):
    """
    This is the default metadata implementation.
    It returns an ad-hoc set of information about the view.
    There are not any formalized standards for `OPTIONS` responses
    for us to base this on.
    """

    label_lookup = ClassLookupDict(
        {
            serializers.Field: "field",
            serializers.BooleanField: "boolean",
            serializers.NullBooleanField: "boolean",
            serializers.CharField: "string",
            serializers.UUIDField: "string",
            serializers.URLField: "url",
            serializers.EmailField: "email",
            serializers.RegexField: "regex",
            serializers.SlugField: "slug",
            serializers.IntegerField: "integer",
            serializers.FloatField: "float",
            serializers.DecimalField: "decimal",
            serializers.DateField: "date",
            serializers.DateTimeField: "datetime",
            serializers.TimeField: "time",
            serializers.ChoiceField: "choice",
            serializers.MultipleChoiceField: "multiple choice",
            serializers.FileField: "file upload",
            serializers.ImageField: "image upload",
            serializers.ListField: "list",
            serializers.DictField: "nested object",
            serializers.Serializer: "nested object",
        }
    )

    def determine_metadata(self, request, view):
        metadata = OrderedDict()
        metadata["name"] = view.get_view_name()
        metadata["description"] = view.get_view_description()
        metadata["renders"] = [
            renderer.media_type for renderer in view.renderer_classes
        ]
        metadata["parses"] = [parser.media_type for parser in view.parser_classes]
        metadata["fieldset"] = self.determine_fieldset(request, view)
        return metadata

    def determine_fieldset(self, request, view):
        fieldset = {}
        if "POST" in view.allowed_methods:
            view.request = clone_request(request, "POST")
            try:
                # Test global permissions
                if hasattr(view, "check_permissions"):
                    view.check_permissions(view.request)
            except (exceptions.APIException, PermissionDenied, Http404):
                pass
            else:
                # If user has appropriate permissions for the view, include
                # appropriate metadata about the fields that should be supplied.
                serializer = view.get_serializer()
                fieldset = self.get_serializer_info(serializer)
            finally:
                view.request = request
        return fieldset

    def get_serializer_info(self, serializer):
        """
        Given an instance of a serializer, return a dictionary of metadata
        about its fields.
        """
        if hasattr(serializer, "child"):
            # If this is a `ListSerializer` then we want to examine the
            # underlying child serializer instance instead.
            serializer = serializer.child
        return OrderedDict(
            [
                (field_name, self.get_field_info(field))
                for field_name, field in serializer.fields.items()
                if not isinstance(field, serializers.HiddenField)
            ]
        )

    def get_field_info(self, field):
        """
        Given an instance of a serializer field, return a dictionary
        of metadata about it.
        """
        field_info = OrderedDict()
        field_info["type"] = self.label_lookup[field]
        field_info["required"] = getattr(field, "required", False)

        attrs = [
            "read_only",
            "label",
            "help_text",
            "min_length",
            "max_length",
            "min_value",
            "max_value",
        ]

        for attr in attrs:
            value = getattr(field, attr, None)
            if value is not None and value != "":
                field_info[attr] = force_str(value, strings_only=True)

        if getattr(field, "child", None):
            field_info["child"] = self.get_field_info(field.child)
        elif getattr(field, "fields", None):
            field_info["children"] = self.get_serializer_info(field)

        if (
            not field_info.get("read_only")
            and not isinstance(
                field, (serializers.RelatedField, serializers.ManyRelatedField)
            )
            and hasattr(field, "choices")
        ):
            field_info["choices"] = [
                {
                    "value": choice_value,
                    "display_name": force_str(choice_name, strings_only=True),
                }
                for choice_value, choice_name in field.choices.items()
            ]

        return field_info
