from django.conf import settings
from django.utils.deprecation import MiddlewareMixin
from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.views import exception_handler, Response


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if response is None:
        msg = str(exc)
        if not settings.DEBUG:
            msg = '服务器错误'
        return Response({
            'msg': msg,
            'code': status.HTTP_500_INTERNAL_SERVER_ERROR,
        },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR, exception=True)
    elif isinstance(exc, APIException):
        code = exc.status_code
        msg = exc.detail
        if hasattr(exc, 'code'):
            code = exc.code
        http_status = 200

        if isinstance(exc.detail, dict):
            if exc.detail.get('messages'):
                msg = exc.detail.get('messages')[0].get('message')
        return Response({'msg': msg, 'code': code}, status=http_status, exception=True)
    else:
        return response
