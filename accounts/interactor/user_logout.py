from django.http import HttpResponse

from accounts.exceptions.exceptions import InvalidAccessToken
from accounts.interactor.presenter_interfaces.presenter_interface import (
    PresenterInterface,
)
from accounts.interactor.storage_interfaces.account_storage_interface import (
    AccountStorageInterface,
)


class LogoutUserInteractor:
    def __init__(self, account_storage: AccountStorageInterface):
        self.account_storage = account_storage

    def logout_user_wrapper(
        self, access_token: str, presenter: PresenterInterface
    ) -> HttpResponse:
        try:
            self.logout_user(access_token=access_token)
            return presenter.logout_user_http_response()
        except InvalidAccessToken:
            return presenter.get_invalid_access_token_http_error()

    def logout_user(self, access_token: str):
        self.validate_access_token(access_token=access_token)

    def validate_access_token(self, access_token: str):
        is_valid_access_token = self.account_storage.is_session_token_valid(
            session_token=access_token
        )

        if not is_valid_access_token:
            raise InvalidAccessToken(access_token=access_token)

        self.account_storage.delete_session_token(session_token=access_token)
