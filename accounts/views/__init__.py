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


class CreateGoalSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=255, required=False)
    category = serializers.CharField(max_length=255)
    target_datetime = serializers.DateTimeField()
    due_datetime = serializers.DateTimeField(required=False)
    priority = serializers.IntegerField()
    is_public = serializers.BooleanField()


class UpdateGoalSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=255, required=False)
    category = serializers.CharField(max_length=255, required=False)
    target_datetime = serializers.DateTimeField(required=False)
    due_datetime = serializers.DateTimeField(required=False)
    priority = serializers.IntegerField(required=False)
    is_public = serializers.BooleanField(required=False)
