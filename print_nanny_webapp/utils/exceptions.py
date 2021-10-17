from rest_framework.exceptions import APIException


class AlreadyExistsException(APIException):
    status_code = 409
    default_detail = "Resource already exists"
    default_code = "already_exists"
