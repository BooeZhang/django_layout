from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    """ 登陆字段序列化 """
    user_name = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=50)
