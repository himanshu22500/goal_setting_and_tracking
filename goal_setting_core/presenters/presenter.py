import json
from datetime import datetime

from django.http import HttpResponse

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
            "category": target_datetime,
        }
        response_json = json.dumps(response_dict)
        return HttpResponse(
            response_json, content_type="application/json", status=400
        )

    def get_invalid_due_datetime_http_error(self, due_datetime: datetime):
        response_dict = {
            "error": "Due datetime must be in the future.",
            "category": due_datetime,
        }
        response_json = json.dumps(response_dict)
        return HttpResponse(
            response_json, content_type="application/json", status=400
        )

    def get_goal_created_http_response(self, goal_dto: GoalDTO):
        goal_dict = {
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

        response_dict = {
            "message": "goal created successfully",
            "data": goal_dict,
        }
        response_json = json.dumps(response_dict)
        return HttpResponse(
            response_json, content_type="application/json", status=400
        )
