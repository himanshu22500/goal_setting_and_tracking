from accounts.interactor.storage_interfaces.account_storage_interface import (
    AccountStorageInterface,
)


class ValidateSessionTokenInteractor:
    def __init__(self, account_storage: AccountStorageInterface):
        self.account_storage = account_storage

    def is_session_token_valid(self, session_token: str) -> bool:
        return self.account_storage.is_session_token_valid(
            session_token=session_token
        )
