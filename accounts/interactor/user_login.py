import secrets
from datetime import datetime, timedelta

from django.http import HttpResponse

from accounts.dtos import UserLoginParamsDTO
from accounts.exceptions.exceptions import InvalidLoginUsernameOrPassword
from accounts.interactor.presenter_interfaces.presenter_interface import (
    PresenterInterface,
)
from accounts.interactor.storage_interfaces.account_storage_interface import (
    AccountStorageInterface,
)


class LoginUserInteractor:
    def __init__(self, account_storage: AccountStorageInterface):
        self.account_storage = account_storage

    def login_user_wrapper(
        self,
        user_login_params_dto: UserLoginParamsDTO,
        presenter: PresenterInterface,
    ) -> HttpResponse:
        try:
            session_token = self.login_user(
                user_login_params_dto=user_login_params_dto
            )
        except InvalidLoginUsernameOrPassword:
            return presenter.get_unsuccessful_login_attempt_http_error(
                user_name=user_login_params_dto.user_name,
                password=user_login_params_dto.password,
            )
        else:
            return presenter.get_successful_login_attempt_http_error(
                session_token=session_token
            )

    def login_user(self, user_login_params_dto: UserLoginParamsDTO) -> str:
        user = self.account_storage.validate_username_and_password(
            user_login_params_dto.user_name, user_login_params_dto.password
        )

        if not user:
            raise InvalidLoginUsernameOrPassword(
                user_name=user_login_params_dto.user_name,
                password=user_login_params_dto.password,
            )

        session_token = secrets.token_hex(16)
        expiry_datetime = datetime.now() + timedelta(hours=1)
        self.account_storage.store_session_token(
            user_id=user.id,
            session_token=session_token,
            expiry_datetime=expiry_datetime,
        )

        return session_token
