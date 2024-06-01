from goal_setting_core.adapters.service_adapter import ServiceAdapter
from goal_setting_core.exceptions.exceptions import (
    GoalDoseNotBelongToUser,
    InvalidGoalId,
    InvalidSessionToken,
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
        except InvalidSessionToken:
            return presenter.get_invalid_access_token_http_error()
        except InvalidGoalId:
            return presenter.get_goal_not_found_http_error(goal_id=goal_id)
        except GoalDoseNotBelongToUser:
            return presenter.get_goal_not_found_http_error(goal_id=goal_id)

    def get_goal(self, session_token: str, goal_id: str):
        self.validate_session_token(session_token=session_token)
        user_id = self.account_service.get_user_id(session_token=session_token)
        self.validate_goal_belongs_to_user(
            user_id=user_id, goal_id=goal_id, goal_storage=self.goal_storage
        )
        return self.goal_storage.get_goal(goal_id=goal_id)

    def validate_session_token(self, session_token: str):
        is_valid = self.account_service.is_session_token_valid(
            session_token=session_token
        )

        if not is_valid:
            raise InvalidSessionToken(session_token=session_token)
