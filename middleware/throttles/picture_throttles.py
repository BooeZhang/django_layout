from django.contrib.auth.models import AnonymousUser
from rest_framework.throttling import BaseThrottle


class PictureThrottles(BaseThrottle):
    """
    图片功能，根据不同用户进行访问次数限制
    """
    def allow_request(self, request, view) -> bool:
        print(request.user)
        if isinstance(request.user, AnonymousUser):
            print('===========')
        return True
