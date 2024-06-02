from abc import abstractmethod
from typing import List

from accounts.dtos import CreateGoalParamsDTO, UpdateGoalParamsDTO
from goal_setting_core.interactor.storage_interfaces.dtos import GoalDTO


class GoalStorageInterface:
    @abstractmethod
    def create_user_goal(
        self, user_id: int, create_goal_parameter_dto: CreateGoalParamsDTO
    ):
        pass

    @abstractmethod
    def is_category_exists(self, category: str):
        pass

    @abstractmethod
    def get_user_goals(self, user_id: int) -> List[GoalDTO]:
        pass

    @abstractmethod
    def get_goal(self, goal_id: str):
        pass

    @abstractmethod
    def delete_goal(self, goal_id: str):
        pass

    @abstractmethod
    def update_goal(
        self, update_goal_params_dto: UpdateGoalParamsDTO, goal_id: str
    ):
        pass

    @abstractmethod
    def get_user_id_for_goal_id(self, goal_id: str) -> int:
        pass

    @abstractmethod
    def get_user_public_goals(self, user_id: int) -> List[GoalDTO]:
        pass
