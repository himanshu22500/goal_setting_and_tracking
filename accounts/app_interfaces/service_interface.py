from accounts.storages.account_storage import AccountStorage


class ServiceInterface:
    def get_user_id(self, session_token: str) -> int:
        from accounts.interactor.get_user_id import GetUserIdInteractor

        interactor = GetUserIdInteractor(account_storage=AccountStorage())

        return interactor.get_user_id(session_token=session_token)

    def is_access_token_valid(self, session_token: str) -> bool:
        from accounts.interactor.validate_session_token import (
            ValidateSessionTokenInteractor,
        )

        interactor = ValidateSessionTokenInteractor(
            account_storage=AccountStorage()
        )

        return interactor.is_session_token_valid(session_token=session_token)
