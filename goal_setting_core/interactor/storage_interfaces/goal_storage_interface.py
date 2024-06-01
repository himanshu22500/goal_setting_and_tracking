from abc import abstractmethod

from accounts.dtos import CreateGoalParamsDTO


class GoalStorageInterface:
    @abstractmethod
    def create_user_goal(
        self, user_id: int, create_goal_parameter_dto: CreateGoalParamsDTO
    ):
        pass

    def is_category_exists(self, category: str):
        pass
