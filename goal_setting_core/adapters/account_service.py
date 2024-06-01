class AccountService:
    @property
    def interface(self):
        from accounts.app_interfaces.service_interface import ServiceInterface

        return ServiceInterface()

    def get_user_id(self, session_token: str) -> int:
        return self.interface.get_user_id(session_token=session_token)

    def is_session_token_valid(self, session_token: str) -> bool:
        return self.interface.is_session_token_valid(
            session_token=session_token
        )
