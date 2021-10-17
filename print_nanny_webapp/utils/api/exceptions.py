from rest_framework.exceptions import APIException
from rest_framework.status import HTTP_409_CONFLICT


class AlreadyExists(APIException):
    status_code = HTTP_409_CONFLICT
    default_detail = "Resource already exists"
    default_code = "already_exists"
