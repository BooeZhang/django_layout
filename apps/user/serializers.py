from rest_framework import serializers

from apps.user.models import UserModel


class LoginSerializer(serializers.Serializer):
    user_name = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=50)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['user_name']
