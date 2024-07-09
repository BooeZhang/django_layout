from django.utils.translation import gettext_lazy as _
from rest_framework import status
from rest_framework.exceptions import APIException


class CommonExceptionMixin(APIException):
    default_detail: str
    default_code: int
    status_code: int = status.HTTP_200_OK

    def __init__(
        self,
        status_code: int,
        detail: str = _("失败"),
        code: int = 0,
    ) -> None:
        """为异常构建详细信息，以便向 API 用户提供更多信息"""
        if status_code != 0:
            self.status_code = status_code
        if code != 0:
            self.default_code = code

        self.default_detail = detail
        super().__init__(self.default_detail, self.default_code)


class NotUserException(CommonExceptionMixin):
    default_detail = _("用户不存在")
    default_code = 10000


class UserOrPwdException(CommonExceptionMixin):
    default_detail = _("用户名或密码错误")
    default_code = 10001


class AuthenticationFailed(CommonExceptionMixin):
    default_detail = _("身份认证失败")
    default_code = 10002
