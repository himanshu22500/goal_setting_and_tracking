from accounts.interactor.storage_interfaces.account_storage_interface import (
    AccountStorageInterface,
)


class GetUserIdInteractor:
    def __init__(self, account_storage: AccountStorageInterface):
        self.account_storage = account_storage

    def get_user_id(self, session_token: str) -> int:
        return self.account_storage.get_user_id_from_session_token(
            session_token=session_token
        )
