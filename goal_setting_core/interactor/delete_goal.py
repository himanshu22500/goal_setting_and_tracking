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


class DeleteGoalInteractor:
    def __init__(self, goal_storage: GoalStorageInterface):
        self.goal_storage = goal_storage

    @property
    def account_service(self):
        return ServiceAdapter().sales_crm_service

    def delete_goal_wrapper(
        self, session_token: str, goal_id: str, presenter: PresenterInterface
    ):
        try:
            self.delete_goal(session_token=session_token, goal_id=goal_id)
            return presenter.get_goal_deleted_http_response(goal_id=goal_id)
        except InvalidAccessToken:
            return presenter.get_invalid_access_token_http_error()
        except InvalidGoalId:
            return presenter.get_goal_not_found_http_error(goal_id=goal_id)
        except GoalDoseNotBelongToUser:
            return presenter.get_goal_not_found_http_error(goal_id=goal_id)

    def delete_goal(self, session_token: str, goal_id: str):
        user_id = self.account_service.get_user_id(session_token=session_token)
        # todo : add cross account_goal validation
        return self.goal_storage.delete_goal(goal_id=goal_id)
