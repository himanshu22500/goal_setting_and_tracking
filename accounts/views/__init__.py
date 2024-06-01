from rest_framework import serializers


class CreateUserSerializer(serializers.Serializer):
    user_name = serializers.CharField(max_length=25)
    password = serializers.IntegerField(max_length=25)
    email = serializers.CharField(max_length=25)
