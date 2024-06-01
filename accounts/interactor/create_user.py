import re

from django.contrib.auth.hashers import make_password
from django.http import HttpResponse

from accounts.constants.constants import (
    EMAIL_REGEX,
    PASSWORD_REGEX,
    USERNAME_REGEX,
)
from accounts.dtos import CreateUserParamsDTO
from accounts.exceptions.exceptions import (
    EmailAlreadyExists,
    InvalidEmail,
    InvalidPassword,
    InvalidUserName,
    UserNameAlreadyExists,
)
from accounts.interactor.presenter_interfaces.presenter_interface import (
    PresenterInterface,
)
from accounts.interactor.storage_interfaces.account_storage_interface import (
    AccountStorageInterface,
)


class CreateUserInteractor:
    def __init__(self, account_storage: AccountStorageInterface):
        self.account_storage = account_storage

    def create_account_user_wrapper(
        self,
        create_user_params_dto: CreateUserParamsDTO,
        presenter: PresenterInterface,
    ) -> HttpResponse:
        try:
            self.create_account_user(
                create_user_params_dto=create_user_params_dto
            )
        except InvalidUserName:
            return presenter.get_invalid_username_http_error(
                user_name=create_user_params_dto.user_name
            )
        except InvalidEmail:
            return presenter.get_invalid_email_http_error(
                email=create_user_params_dto.email
            )
        except InvalidPassword:
            return presenter.get_invalid_password_http_error(
                password=create_user_params_dto.password
            )
        except UserNameAlreadyExists:
            return presenter.get_username_already_exists_http_error(
                user_name=create_user_params_dto.user_name
            )
        except EmailAlreadyExists:
            return presenter.get_email_already_exists_http_error(
                email=create_user_params_dto.email
            )
        else:
            return presenter.get_success_http_response_for_create_user()

    def create_account_user(self, create_user_params_dto: CreateUserParamsDTO):
        self._validate_creation_params(
            create_user_params_dto=create_user_params_dto
        )
        create_user_params_dto.password = make_password(
            create_user_params_dto.password
        )
        self.account_storage.create_account_user(
            create_user_params_dto=create_user_params_dto
        )

    def validate_username(self, user_name: str):
        is_username_taken = self.account_storage.is_username_exists(
            user_name=user_name
        )
        if is_username_taken:
            raise UserNameAlreadyExists(user_name=user_name)
        is_valid = bool(re.match(USERNAME_REGEX, user_name))
        if not is_valid:
            raise InvalidUserName(user_name=user_name)

    @staticmethod
    def validate_password(password: str):
        is_valid = bool(re.match(PASSWORD_REGEX, password))
        if not is_valid:
            raise InvalidPassword(password=password)

    def validate_email(self, email: str):
        user_exists_with_email = self.account_storage.is_email_exists(
            email=email
        )

        if user_exists_with_email:
            raise EmailAlreadyExists(email=email)

        is_valid = bool(re.match(EMAIL_REGEX, email))
        if not is_valid:
            raise InvalidEmail(email=email)

    def _validate_creation_params(
        self, create_user_params_dto: CreateUserParamsDTO
    ):
        self.validate_username(user_name=create_user_params_dto.user_name)
        self.validate_email(email=create_user_params_dto.email)
        self.validate_password(password=create_user_params_dto.password)
