from abc import abstractmethod
from datetime import datetime

from goal_setting_core.interactor.storage_interfaces.dtos import GoalDTO


class PresenterInterface:
    @abstractmethod
    def get_empty_title_http_error(self):
        pass

    @abstractmethod
    def get_invalid_category_http_error(self, category: str):
        pass

    @abstractmethod
    def get_invalid_target_datetime_http_error(
        self, target_datetime: datetime
    ):
        pass

    @abstractmethod
    def get_invalid_due_datetime_http_error(self, due_datetime: datetime):
        pass

    @abstractmethod
    def get_goal_created_http_response(self, goal_dto: GoalDTO):
        pass
