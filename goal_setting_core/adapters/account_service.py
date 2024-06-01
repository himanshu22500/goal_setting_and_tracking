class AccountService:
    @property
    def interface(self):
        from accounts.app_interfaces.service_interface import ServiceInterface

        return ServiceInterface()

    def get_user_id(self, session_token: str) -> int:
        return self.interface.get_user_id(session_token=session_token)
