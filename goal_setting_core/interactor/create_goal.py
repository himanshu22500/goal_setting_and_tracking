from django.http import HttpResponse

from goal_setting_core.interactor.presenter_interfaces.presenter_interface import (
    PresenterInterface,
)
from goal_setting_core.interactor.storage_interfaces.goal_storage_interface import (
    GoalStorageInterface,
)


class CreateGoalInteractor:
    def __init__(self, goal_storage: GoalStorageInterface):
        self.goal_storage = goal_storage

    def create_goal_wrapper(
        self, create_goal_parameter_dto, presenter: PresenterInterface
    ) -> HttpResponse:
        pass

    def create_goal(self, create_goal_parameter_dto):
        pass
