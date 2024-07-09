from django.conf import settings
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.views import exception_handler, Response
from loguru import logger as log

from apps.common.exception import CommonExceptionMixin


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if isinstance(exc, ValidationError):
        code = exc.status_code
        http_status = status.HTTP_200_OK
        _request = context.get("request")
        url = _request.path
        log.error(f"{url} 请求参数错误：{exc.detail}")
        return Response(
            {"msg": "参数错误", "code": code}, status=http_status, exception=True
        )

    elif isinstance(exc, CommonExceptionMixin):
        code = exc.get_codes()
        msg = exc.detail
        http_status = status.HTTP_200_OK
        return Response({"msg": msg, "code": code}, status=http_status, exception=True)
    elif response is None:
        msg = str(exc)
        if not settings.DEBUG:
            msg = "服务器错误"
        return Response(
            {
                "msg": msg,
                "code": status.HTTP_500_INTERNAL_SERVER_ERROR,
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            exception=True,
        )
    else:
        return response
