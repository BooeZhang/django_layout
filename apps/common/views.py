from django.contrib.auth.hashers import check_password
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from apps.common.exception import NotUserException, UserOrPwdException
from apps.common.serializers import LoginSerializer
from apps.user.models import UserModel


# Create your views here.


class Login(APIView):
    """
    登录
    """

    @swagger_auto_schema(
        operation_description="登录",
        request_body=LoginSerializer,
        responses={status.HTTP_200_OK: LoginSerializer},
    )
    def post(self, request: Request):
        ps = LoginSerializer(data=request.data)
        if ps.is_valid():
            try:
                _user = UserModel.objects.get(user_name=ps.data.get("user_name"))
            except UserModel.DoesNotExist:
                raise NotUserException()

            if check_password(ps.data.get("password"), _user.password):
                token = RefreshToken.for_user(_user)
                return Response(
                    {"refresh_toke": str(token), "access": str(token.access_token)},
                    status=status.HTTP_200_OK,
                )
            else:
                raise UserOrPwdException()

        raise ValidationError(ps.errors)
