import json
from datetime import datetime
from typing import List

from django.http import HttpResponse
from rest_framework import status

from goal_setting_core.interactor.presenter_interfaces.presenter_interface import (
    PresenterInterface,
)
from goal_setting_core.interactor.storage_interfaces.dtos import GoalDTO


class Presenter(PresenterInterface):
    def get_empty_title_http_error(self):
        response_dict = {"error": "Title can't be an empty string."}
        response_json = json.dumps(response_dict)
        return HttpResponse(
            response_json, content_type="application/json", status=400
        )

    def get_invalid_category_http_error(self, category: str):
        response_dict = {
            "error": "category doesn't exists",
            "category": category,
        }
        response_json = json.dumps(response_dict)
        return HttpResponse(
            response_json, content_type="application/json", status=400
        )

    def get_invalid_target_datetime_http_error(
        self, target_datetime: datetime
    ):
        response_dict = {
            "error": "Target datetime must be in the future.",
            "target_datetime": str(target_datetime),
        }
        response_json = json.dumps(response_dict)
        return HttpResponse(
            response_json, content_type="application/json", status=400
        )

    def get_invalid_due_datetime_http_error(self, due_datetime: datetime):
        response_dict = {
            "error": "Due datetime must be in the future.",
            "due_datetime": str(due_datetime),
        }
        response_json = json.dumps(response_dict)
        return HttpResponse(
            response_json,
            content_type="application/json",
            status=status.HTTP_400_BAD_REQUEST,
        )

    def _get_goal_dict(self, goal_dto: GoalDTO):
        return {
            "id": goal_dto.id,
            "title": goal_dto.title,
            "description": goal_dto.description,
            "target_datetime": goal_dto.target_datetime.isoformat(),
            "due_datetime": goal_dto.due_datetime.isoformat()
            if goal_dto.due_datetime
            else None,
            "priority": goal_dto.priority,
            "is_public": goal_dto.is_public,
        }

    def _get_goal_dicts(self, goal_dtos: List[GoalDTO]):
        return [self._get_goal_dict(goal_dto=dto) for dto in goal_dtos]

    def get_goal_created_http_response(self, goal_dto: GoalDTO):
        goal_dict = self._get_goal_dict(goal_dto=goal_dto)

        response_dict = {
            "message": "goal created successfully",
            "data": goal_dict,
        }
        response_json = json.dumps(response_dict)
        return HttpResponse(
            response_json,
            content_type="application/json",
            status=status.HTTP_200_OK,
        )

    def get_user_goals_http_response(self, goal_dtos: List[GoalDTO]):
        goal_dicts = self._get_goal_dicts(goal_dtos=goal_dtos)
        response_dict = {
            "data": goal_dicts,
        }
        response_json = json.dumps(response_dict)
        return HttpResponse(
            response_json,
            content_type="application/json",
            status=status.HTTP_200_OK,
        )

    def get_goal_http_response(self, goal_dto: GoalDTO):
        goal_dict = self._get_goal_dict(goal_dto=goal_dto)

        response_dict = {
            "data": goal_dict,
        }
        response_json = json.dumps(response_dict)
        return HttpResponse(
            response_json,
            content_type="application/json",
            status=status.HTTP_200_OK,
        )

    def get_goal_not_found_http_error(self, goal_id: str):
        response_dict = {
            "error": "goal_id not found",
            "goal_id": goal_id,
        }
        response_json = json.dumps(response_dict)
        return HttpResponse(
            response_json,
            content_type="application/json",
            status=status.HTTP_400_BAD_REQUEST,
        )

    def get_goal_deleted_http_response(self, goal_id: str):
        response_dict = {
            "message": "goal deleted successfully",
            "goal_id": goal_id,
        }
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
