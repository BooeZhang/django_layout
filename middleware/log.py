import datetime
from typing import Callable

from django.http import HttpRequest
from loguru import logger

# 日志配置
# logger.add('log_file.log',
#            level="INFO",
#            rotation='500 MB',  # 文件大小
#            encoding='utf-8',
#            retention="7 days",  # 定时清理
#            compression="zip",  # 压缩
#            enqueue=True,  # 多线程安全
#            )


class RequestLogMiddleware(object):
    """
    请求日志中间件
    """
    def __init__(self, get_response: Callable):
        self.get_response = get_response

    def __call__(self, request: HttpRequest):
        start_time = datetime.datetime.now()
        response = self.get_response(request)
        t = datetime.datetime.now() - start_time
        t = f'{t.microseconds/1000000}S'
        code = response.status_code
        host = request.META.get('HTTP_HOST')
        method = request.method
        path = request.path
        agreement = request.META.get('SERVER_PROTOCOL', 'HTTP/1.1')
        msg = "{:<5}|{:<10}|{:<20}|{:<6} {:<20} {:<6}".format(code, t, host, method, path, agreement)
        if code == 200:
            logger.info(msg)
        else:
            logger.warning(msg)
        return response
