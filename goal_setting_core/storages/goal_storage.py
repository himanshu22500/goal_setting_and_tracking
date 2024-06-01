from typing import List

from django.core.exceptions import ObjectDoesNotExist

from accounts.dtos import CreateGoalParamsDTO
from goal_setting_core.exceptions.exceptions import InvalidGoalId
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

    def get_user_goals(self, user_id: int) -> List[GoalDTO]:
        goal_objs = Goal.objects.filter(user__id=user_id)

        return self._get_goal_dtos(goal_objs=goal_objs)

    def _get_goal_dtos(self, goal_objs):
        return [self._get_goal_dto(goal=obj) for obj in goal_objs]

    def get_goal(self, goal_id: str):
        try:
            goal = Goal.objects.get(id=goal_id)
            return self._get_goal_dto(goal=goal)
        except ObjectDoesNotExist:
            raise InvalidGoalId(goal_id=goal_id)

    def delete_goal(self, goal_id: str):
        try:
            goal = Goal.objects.get(id=goal_id)
            goal.delete()
        except ObjectDoesNotExist:
            raise InvalidGoalId(goal_id=goal_id)
