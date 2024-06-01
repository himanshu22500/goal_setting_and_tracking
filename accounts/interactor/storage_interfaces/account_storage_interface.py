from abc import abstractmethod
from datetime import datetime

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

    @abstractmethod
    def is_username_exists(self, user_name: str):
        pass

    @abstractmethod
    def is_email_exists(self, email: str):
        pass

    @abstractmethod
    def validate_username_and_password(self, user_name: str, password: str):
        pass

    @abstractmethod
    def store_session_token(
        self, user_id: int, session_token: str, expiry_datetime: datetime
    ):
        pass

    @abstractmethod
    def is_session_token_valid(self, session_token: str):
        pass

    @abstractmethod
    def delete_session_token(self, session_token: str):
        pass

    @abstractmethod
    def get_user_id_from_session_token(self, session_token: str):
        pass
