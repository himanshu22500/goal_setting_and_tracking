from accounts.dtos import CreateGoalParamsDTO
from goal_setting_core.interactor.storage_interfaces.dtos import GoalDTO
from goal_setting_core.interactor.storage_interfaces.goal_storage_interface import (
    GoalStorageInterface,
)
from goal_setting_core.models.models import Category, Goal


class GoalStorage(GoalStorageInterface):
    def create_user_goal(
        self, user_id: int, create_goal_parameter_dto: CreateGoalParamsDTO
    ):
        category_obj = Category.objects.get(
            name=create_goal_parameter_dto.category
        )

        goal = Goal.objects.create(
            user_id=user_id,
            title=create_goal_parameter_dto.title,
            description=create_goal_parameter_dto.description,
            category=category_obj,
            target_datetime=create_goal_parameter_dto.target_datetime,
            due_datetime=create_goal_parameter_dto.due_datetime,
            priority=create_goal_parameter_dto.priority,
            is_public=create_goal_parameter_dto.is_public,
        )
        return self._get_goal_dto(goal=goal)

    def is_category_exists(self, category: str):
        return Category.objects.filter(name=category).exists()

    @staticmethod
    def _get_goal_dto(goal):
        return GoalDTO(
            id=str(goal.id),
            title=goal.title,
            description=goal.description,
            target_datetime=goal.target_datetime,
            due_datetime=goal.due_datetime,
            priority=goal.priority,
            is_public=goal.is_public,
        )
