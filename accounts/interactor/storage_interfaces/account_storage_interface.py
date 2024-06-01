from abc import abstractmethod

from accounts.dtos import CreateUserParamsDTO


class AccountStorageInterface:
    @abstractmethod
    def create_account_user(self, create_user_params_dto: CreateUserParamsDTO):
        pass

    @abstractmethod
    def get_account_user_profile(self):
        pass

    @abstractmethod
    def update_account_user_profile(self):
        pass
