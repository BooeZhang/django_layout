from typing import Callable

from django.http import HttpRequest
from loguru import logger


class RequestDumpMiddleware(object):
    """
    请求数据打印中间件
    """

    def __init__(self, get_response: Callable):
        self.get_response = get_response

    def __call__(self, request: HttpRequest):
        if request.method == "POST":
            logger.info(
                f"{request.path} post body dumps: {request.body.decode('utf-8')}"
            )
        response = self.get_response(request)
        return response
