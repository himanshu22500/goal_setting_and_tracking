from datetime import datetime

from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from accounts.dtos import CreateUserParamsDTO
from accounts.exceptions.exceptions import InvalidAccessToken
from accounts.interactor.storage_interfaces.account_storage_interface import (
    AccountStorageInterface,
)
from accounts.models.user_profile import SessionToken, UserProfile


class AccountStorage(AccountStorageInterface):
    def create_account_user(self, create_user_params_dto: CreateUserParamsDTO):
        user_obj = User(
            username=create_user_params_dto.user_name,
            password=create_user_params_dto.password,
            email=create_user_params_dto.email,
        )
        user_obj.save()

        user_profile_obj = UserProfile(user=user_obj)
        user_profile_obj.save()

    def get_account_user_profile(self):
        pass

    def update_account_user_profile(self):
        pass

    def is_username_exists(self, user_name: str):
        return User.objects.filter(username=user_name).exists()

    def is_email_exists(self, email: str):
        return User.objects.filter(email=email).exists()

    def validate_username_and_password(self, user_name: str, password: str):
        user = authenticate(username=user_name, password=password)
        return user

    def store_session_token(
        self, user_id: int, session_token: str, expiry_datetime: datetime
    ):
        user_obj = User.objects.get(id=user_id)
        session_token_obj = SessionToken(
            user=user_obj, token=session_token, expiry_date=expiry_datetime
        )
        session_token_obj.save()

    def is_session_token_valid(self, session_token: str):
        current_time = datetime.now()
        return SessionToken.objects.filter(
            token=session_token, expiry_date__gt=current_time
        ).exists()

    def delete_session_token(self, session_token: str):
        session_token_obj = SessionToken.objects.filter(token=session_token)
        if session_token_obj.exists():
            session_token_obj.delete()

    def get_user_id_from_session_token(self, session_token: str):
        try:
            session_token_obj = SessionToken.objects.get(token=session_token)
            return session_token_obj.user.id
        except SessionToken.DoesNotExist:
            return InvalidAccessToken(access_token=session_token)
