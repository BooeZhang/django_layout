from typing import Tuple

from channels.db import database_sync_to_async
from channels_auth_token_middlewares.middleware import (
    DRFAuthTokenMiddleware,
    SimpleJWTAuthTokenMiddleware,
)
from channels_auth_token_middlewares.middleware.drf import (
    SimpleJWTAuthTokenMiddlewareMixin,
)
from django.contrib.auth.models import AnonymousUser
from rest_framework import status
from rest_framework.request import Request
from rest_framework_simplejwt.authentication import JWTAuthentication, AuthUser
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.settings import api_settings
from django.utils.translation import gettext_lazy as _
from rest_framework_simplejwt.tokens import Token
from rest_framework_simplejwt.utils import get_md5_hash_password

from apps.common.exception import AuthenticationFailed
from apps.user.models import UserModel


class Authentication(JWTAuthentication):
    """
    自定义认证
    """

    def authenticate(self, request: Request) -> Tuple[UserModel, Token] | None:
        header = self.get_header(request)
        if header is None:
            raise AuthenticationFailed(
                status_code=status.HTTP_401_UNAUTHORIZED, detail=_("header 头不存在")
            )

        raw_token = self.get_raw_token(header)
        if raw_token is None:
            raise AuthenticationFailed(
                status_code=status.HTTP_401_UNAUTHORIZED, detail=_("token 为空")
            )

        validated_token = self.get_validated_token(raw_token)

        return self.get_user(validated_token), validated_token

    def get_user(self, validated_token: Token) -> AuthUser:
        """
        Attempts to find and return a user using the given validated token.
        """
        try:
            user_id = validated_token[api_settings.USER_ID_CLAIM]
        except KeyError:
            raise AuthenticationFailed(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail=_("不包含可识别的用户标识"),
            )

        try:
            user = UserModel.objects.get(**{api_settings.USER_ID_FIELD: user_id})
        except UserModel.DoesNotExist:
            raise AuthenticationFailed(
                status_code=status.HTTP_401_UNAUTHORIZED, detail=_("用户不存在")
            )

        if not user.is_active:
            raise AuthenticationFailed(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail=_("不是活跃用户"),
            )

        if api_settings.CHECK_REVOKE_TOKEN:
            if validated_token.get(
                api_settings.REVOKE_TOKEN_CLAIM
            ) != get_md5_hash_password(user.password):
                raise AuthenticationFailed(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail=_("用户的密码已更改"),
                )

        return user

    def get_validated_token(self, raw_token: bytes) -> Token:
        """
        Validates an encoded JSON web token and returns a validated token
        wrapper object.
        """
        messages = []
        for AuthToken in api_settings.AUTH_TOKEN_CLASSES:
            try:
                return AuthToken(raw_token)
            except TokenError as e:
                messages.append(
                    {
                        "token_class": AuthToken.__name__,
                        "token_type": AuthToken.token_type,
                        "message": e.args[0],
                    }
                )

        raise AuthenticationFailed(
            status_code=status.HTTP_401_UNAUTHORIZED, detail=_("令牌无效或已过期")
        )


class WSAuthentication(SimpleJWTAuthTokenMiddleware, Authentication):
    """自定义 Websocket 认证"""

    def get_jwt_user(self, validated_token: Token) -> AuthUser:
        try:
            user_id = validated_token[api_settings.USER_ID_CLAIM]
        except KeyError:
            raise AuthenticationFailed(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail=_("不包含可识别的用户标识"),
            )

        try:
            user = UserModel.objects.get(**{api_settings.USER_ID_FIELD: user_id})
        except UserModel.DoesNotExist:
            raise AuthenticationFailed(
                status_code=status.HTTP_401_UNAUTHORIZED, detail=_("用户不存在")
            )

        if not user.is_active:
            raise AuthenticationFailed(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail=_("不是活跃用户"),
            )

        if api_settings.CHECK_REVOKE_TOKEN:
            if validated_token.get(
                api_settings.REVOKE_TOKEN_CLAIM
            ) != get_md5_hash_password(user.password):
                raise AuthenticationFailed(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail=_("用户的密码已更改"),
                )

        return user

    @database_sync_to_async
    def get_jwt_user_instance(self, token_key):
        if self._auth is None or self._exceptions is None:
            raise RuntimeError("_setup method has to be called before.")
        try:
            validated_token = self.get_validated_token(token_key)
            return self.get_jwt_user(validated_token)
        except self._exceptions:
            return None
