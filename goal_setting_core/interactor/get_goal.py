from goal_setting_core.adapters.service_adapter import ServiceAdapter
from goal_setting_core.exceptions.exceptions import (
    GoalDoseNotBelongToUser,
    InvalidAccessToken,
    InvalidGoalId,
)
from goal_setting_core.interactor.presenter_interfaces.presenter_interface import (
    PresenterInterface,
)
from goal_setting_core.interactor.storage_interfaces.goal_storage_interface import (
    GoalStorageInterface,
)
from goal_setting_core.interactor.validation_mixin import ValidationMixin


class GetGoalInteractor(ValidationMixin):
    def __init__(self, goal_storage: GoalStorageInterface):
        self.goal_storage = goal_storage

    @property
    def account_service(self):
        return ServiceAdapter().sales_crm_service

    def get_goal_wrapper(
        self, session_token: str, goal_id: str, presenter: PresenterInterface
    ):
        try:
            goal_dto = self.get_goal(
                session_token=session_token, goal_id=goal_id
            )
            return presenter.get_goal_http_response(goal_dto=goal_dto)
        except InvalidAccessToken:
            pass
        except InvalidGoalId:
            return presenter.get_goal_not_found_http_error(goal_id=goal_id)
        except GoalDoseNotBelongToUser:
            return presenter.get_goal_not_found_http_error(goal_id=goal_id)

    def get_goal(self, session_token: str, goal_id: str):
        user_id = self.account_service.get_user_id(session_token=session_token)
        self.validate_goal_belongs_to_user(
            user_id=user_id, goal_id=goal_id, goal_storage=self.goal_storage
        )
        return self.goal_storage.get_goal(goal_id=goal_id)
