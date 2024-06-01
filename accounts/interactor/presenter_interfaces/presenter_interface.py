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
