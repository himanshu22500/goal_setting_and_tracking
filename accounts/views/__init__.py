from rest_framework import serializers


class CreateUserSerializer(serializers.Serializer):
    user_name = serializers.CharField(max_length=25)
    password = serializers.CharField(max_length=25)
    email = serializers.CharField(max_length=25)


class UserLoginSerializer(serializers.Serializer):
    user_name = serializers.CharField(max_length=25)
    password = serializers.CharField(max_length=25)


class UserLogoutSerializer(serializers.Serializer):
    access_token = serializers.CharField(max_length=255)
