from rest_framework import serializers

from apps.user.models import UserModel


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        exclude = ["password"]
