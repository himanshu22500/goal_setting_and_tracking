from abc import abstractmethod

from django.http import HttpResponse


class PresenterInterface:
    @abstractmethod
    def get_invalid_username_http_error(self, user_name: str) -> HttpResponse:
        pass

    @abstractmethod
    def get_invalid_password_http_error(self, password: str) -> HttpResponse:
        pass

    @abstractmethod
    def get_invalid_email_http_error(self, email: str) -> HttpResponse:
        pass

    @abstractmethod
    def get_success_http_response_for_create_user(self) -> HttpResponse:
        pass

    @abstractmethod
    def get_username_already_exists_http_error(
        self, user_name: str
    ) -> HttpResponse:
        pass

    @abstractmethod
    def get_email_already_exists_http_error(self, email: str) -> HttpResponse:
        pass

    @abstractmethod
    def get_unsuccessful_login_attempt_http_error(
        self, user_name: str, password: str
    ):
        pass

    @abstractmethod
    def get_successful_login_attempt_http_error(self, session_token: str):
        pass

    @abstractmethod
    def logout_user_http_response(self):
        pass

    @abstractmethod
    def get_invalid_access_token_http_error(self):
        pass
