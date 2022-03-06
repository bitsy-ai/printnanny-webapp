from distutils.log import error
import logging
from uuid import uuid4
from django.http import JsonResponse
from rest_framework.views import exception_handler
from rest_framework.exceptions import APIException
from rest_framework.status import HTTP_409_CONFLICT

logger = logging.getLogger(__name__)


class AlreadyExists(APIException):
    status_code = HTTP_409_CONFLICT
    default_detail = "Resource already exists"
    default_code = "already_exists"


def custom_exception_handler(exc, context):
    # call default exception handler
    response = exception_handler(exc, context)
    error_uuid = uuid4().hex
    logger.error(
        "FATAL API EXCEPTION uuid=%s exc=%s context=%s", error_uuid, exc, context
    )
    # returns response as handled normally by the framework, plus uuid
    if response is not None:
        response.data["error_uuid"] = error_uuid
        return response

    # otherwise, build an error handler
    payload = dict(error_uuid=error_uuid, exc=exc)
    return JsonResponse(payload, safe=False, status=500)
