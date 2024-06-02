from typing import List

from django.core.exceptions import ObjectDoesNotExist

from accounts.dtos import CreateGoalParamsDTO, UpdateGoalParamsDTO
from goal_setting_core.exceptions.exceptions import (
    CategoryDoesNotExist,
    InvalidGoalId,
)
from goal_setting_core.interactor.storage_interfaces.dtos import GoalDTO
from goal_setting_core.interactor.storage_interfaces.goal_storage_interface import (
    GoalStorageInterface,
)
from goal_setting_core.models.models import Category, Goal, GoalUpdate


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
            user_id=goal.user.id,
            title=goal.title,
            description=goal.description,
            category=goal.category.name,
            target_datetime=goal.target_datetime,
            due_datetime=goal.due_datetime,
            is_completed=goal.completed,
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

    def update_goal(
        self, update_goal_params_dto: UpdateGoalParamsDTO, goal_id: str
    ):
        try:
            goal = Goal.objects.get(id=goal_id)
        except ObjectDoesNotExist:
            raise InvalidGoalId(goal_id=goal_id)

        if update_goal_params_dto.title:
            goal.title = update_goal_params_dto.title

        if update_goal_params_dto.target_datetime:
            goal.target_datetime = update_goal_params_dto.target_datetime

        if update_goal_params_dto.due_datetime:
            goal.due_datetime = update_goal_params_dto.due_datetime

        if update_goal_params_dto.category:
            try:
                category = Category.objects.get(
                    name=update_goal_params_dto.category
                )
            except ObjectDoesNotExist:
                raise CategoryDoesNotExist(
                    category=update_goal_params_dto.category
                )
            goal.category = category

        if update_goal_params_dto.completed:
            goal.completed = update_goal_params_dto.completed

        if update_goal_params_dto.description:
            goal.description = update_goal_params_dto.description

        if update_goal_params_dto.is_public is not None:
            goal.is_public = update_goal_params_dto.is_public

        if update_goal_params_dto.priority:
            goal.priority = update_goal_params_dto.priority

        if update_goal_params_dto.update_text:
            self.create_or_update_goal_update_text(
                goal_id=goal_id, update_text=update_goal_params_dto.update_text
            )

        goal.save()
        return self._get_goal_dto(goal=goal)

    def create_or_update_goal_update_text(
        self, goal_id: str, update_text: str
    ):
        try:
            goal_update_obj = GoalUpdate.objects.get(goal__id=goal_id)
            goal_update_obj.update_text = update_text
            goal_update_obj.save()
        except ObjectDoesNotExist:
            GoalUpdate.objects.create(update_text=update_text)

    def get_user_id_for_goal_id(self, goal_id: str) -> int:
        try:
            goal = Goal.objects.get(id=goal_id)
        except ObjectDoesNotExist:
            raise InvalidGoalId(goal_id=goal_id)

        return goal.user.id

    def get_user_public_goals(self, user_id: int) -> List[GoalDTO]:
        goal_objs = Goal.objects.filter(user__id=user_id, is_public=True)

        return self._get_goal_dtos(goal_objs=goal_objs)
