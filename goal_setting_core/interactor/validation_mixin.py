from goal_setting_core.adapters.service_adapter import ServiceAdapter
from goal_setting_core.exceptions.exceptions import GoalDoseNotBelongToUser
from goal_setting_core.interactor.storage_interfaces.goal_storage_interface import (
    GoalStorageInterface,
)


class ValidationMixin:
    @staticmethod
    def validate_goal_belongs_to_user(
        goal_id: str, user_id: str, goal_storage: GoalStorageInterface
    ):
        goal_user_id = goal_storage.get_user_id_for_goal_id(goal_id=goal_id)

        if goal_user_id != user_id:
            raise GoalDoseNotBelongToUser(user_id=user_id, goal_id=goal_id)
