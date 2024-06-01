import json

from django.http import HttpResponse
from rest_framework import status

from accounts.constants.constants import (
    CREATE_USER_SUCCESS_MESSAGE,
    INVALID_EMAIL_FORMAT_MESSAGE,
    INVALID_PASSWORD_FORMAT_MESSAGE,
    INVALID_USERNAME_FORMAT_MESSAGE,
)
from accounts.interactor.presenter_interfaces.presenter_interface import (
    PresenterInterface,
)


class Presenter(PresenterInterface):
    def get_invalid_username_http_error(self, user_name: str) -> HttpResponse:
        response_dict = {
            "message": INVALID_USERNAME_FORMAT_MESSAGE,
            "user_name": user_name,
        }
        response_json = json.dumps(response_dict)
        return HttpResponse(
            response_json, content_type="application/json", status=400
        )

    def get_invalid_password_http_error(self, password: str) -> HttpResponse:
        response_dict = {
            "message": INVALID_PASSWORD_FORMAT_MESSAGE,
            "password": password,
        }
        response_json = json.dumps(response_dict)
        return HttpResponse(
            response_json, content_type="application/json", status=400
        )

    def get_invalid_email_http_error(self, email: str) -> HttpResponse:
        response_dict = {
            "message": INVALID_EMAIL_FORMAT_MESSAGE,
            "email": email,
        }
        response_json = json.dumps(response_dict)
        return HttpResponse(
            response_json, content_type="application/json", status=400
        )

    def get_success_http_response_for_create_user(self) -> HttpResponse:
        response_dict = {
            "message": CREATE_USER_SUCCESS_MESSAGE,
        }
        response_json = json.dumps(response_dict)
        return HttpResponse(
            response_json, content_type="application/json", status=400
        )

    def get_username_already_exists_http_error(
        self, user_name: str
    ) -> HttpResponse:
        response_dict = {
            "message": "username already exists",
            "user_name": user_name,
        }
        response_json = json.dumps(response_dict)
        return HttpResponse(
            response_json, content_type="application/json", status=400
        )

    def get_email_already_exists_http_error(self, email: str) -> HttpResponse:
        response_dict = {"message": "email already exists", "email": email}
        response_json = json.dumps(response_dict)
        return HttpResponse(
            response_json,
            content_type="application/json",
            status=status.HTTP_400_BAD_REQUEST,
        )

    def get_unsuccessful_login_attempt_http_error(
        self, user_name: str, password: str
    ):
        response_dict = {
            "message": "invalid user_name or password",
            "user_name": user_name,
            "password": password,
        }

        response_json = json.dumps(response_dict)
        return HttpResponse(
            response_json,
            content_type="application/json",
            status=status.HTTP_400_BAD_REQUEST,
        )

    def get_successful_login_attempt_http_error(self, session_token: str):
        response_dict = {"session_token": session_token}

        response_json = json.dumps(response_dict)
        return HttpResponse(
            response_json,
            content_type="application/json",
            status=status.HTTP_200_OK,
        )

    def logout_user_http_response(self):
        response_dict = {"message": "successfully logged out"}

        response_json = json.dumps(response_dict)
        return HttpResponse(
            response_json,
            content_type="application/json",
            status=status.HTTP_200_OK,
        )

    def get_invalid_access_token_http_error(self):
        response_dict = {"error": "invalid or expired access token"}

        response_json = json.dumps(response_dict)
        return HttpResponse(
            response_json,
            content_type="application/json",
            status=status.HTTP_401_UNAUTHORIZED,
        )
