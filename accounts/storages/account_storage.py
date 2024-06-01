from django.contrib.auth.models import User

from accounts.dtos import CreateUserParamsDTO
from accounts.interactor.storage_interfaces.account_storage_interface import (
    AccountStorageInterface,
)
from accounts.models.user_profile import UserProfile


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
