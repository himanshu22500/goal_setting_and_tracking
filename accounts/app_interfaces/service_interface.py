from accounts.storages.account_storage import AccountStorage


class ServiceInterface:
    def get_user_id(self, session_token: str) -> int:
        from accounts.interactor.get_user_id import GetUserIdInteractor

        interactor = GetUserIdInteractor(account_storage=AccountStorage())

        return interactor.get_user_id(session_token=session_token)
