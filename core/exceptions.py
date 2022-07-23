from rest_framework import status
from rest_framework.exceptions import APIException


class UniqueException(APIException):
    status_code = status.HTTP_409_CONFLICT
    default_detail = "This value must be unique."
