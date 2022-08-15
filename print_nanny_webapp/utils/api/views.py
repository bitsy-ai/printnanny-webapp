from print_nanny_webapp.utils.api.serializers import (
    ErrorDetailSerializer,
)


generic_list_errors = {
    400: ErrorDetailSerializer,
    401: ErrorDetailSerializer,
    403: ErrorDetailSerializer,
    500: ErrorDetailSerializer,
}

generic_get_errors = {404: ErrorDetailSerializer} | generic_list_errors


generic_create_errors = {409: ErrorDetailSerializer} | generic_list_errors

generic_update_errors = generic_create_errors
