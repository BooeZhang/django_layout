from django.utils.translation import gettext_lazy as _
from rest_framework import status
from rest_framework.exceptions import APIException


class CommonException(APIException):
    status_code = status.HTTP_200_OK


class NotUserException(CommonException):
    default_detail = _("用户不存在")
    default_code = 10000


class UserOrPwdException(CommonException):
    default_detail = _("用户名或密码错误")
    default_code = 10001


class AuthenticationFailed(CommonException):
    default_detail = _("身份认证失败")
    default_code = 10002
