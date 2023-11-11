from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication


class Authentication(BaseAuthentication):
    """
    自定义认证
    """

    def authenticate(self, request):
        pass
        # username = request.META.get('X_USERNAME')
        # if not username:
        #     return None
        #
        # try:
        #     user = User.objects.get(username=username)
        # except User.DoesNotExist:
        #     raise exceptions.AuthenticationFailed('No such user')
        #
        # return (user, None)