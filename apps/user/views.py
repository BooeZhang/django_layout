from django.http import Http404
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from apps.user.models import UserModel
from apps.user.serializers import UserSerializer
from middleware.authentication.authentication import Authentication


# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
    authentication_classes = (Authentication,)
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        queryset = UserModel.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    # def retrieve(self, request, pk=None):
    #     queryset = UserModel.objects.filter(id=pk)
    #     user = get_object_or_404(queryset, pk=pk)
    #     serializer = UserSerializer(user)
    #     return Response(serializer.data)
    #
    # def create(self, request):
    #     pass
    #
    # def update(self, request, pk=None): ...
    #
    # def destroy(self, request, pk=None): ...
