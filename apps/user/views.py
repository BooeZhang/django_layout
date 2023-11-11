from drf_yasg.utils import swagger_auto_schema
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.user.models import UserModel
from apps.user.serializers import LoginSerializer


# Create your views here.


class Login(APIView):
    """
    登录
    """

    @swagger_auto_schema(
        operation_description="登录",
        request_body=LoginSerializer
    )
    def post(self, request: Request, format=None):
        ps = LoginSerializer(data=request.data)
        if ps.is_valid():
            print(ps.data.get('user_name'))
        return Response(data={})
