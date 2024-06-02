from typing import List

from goal_setting_core.adapters.service_adapter import ServiceAdapter
from goal_setting_core.exceptions.exceptions import InvalidSessionToken
from goal_setting_core.interactor.presenter_interfaces.presenter_interface import (
    PresenterInterface,
)
from goal_setting_core.interactor.storage_interfaces.dtos import GoalDTO
from goal_setting_core.interactor.storage_interfaces.goal_storage_interface import (
    GoalStorageInterface,
)


class GetUserPublicGoals:
    def __init__(self, goal_storage: GoalStorageInterface):
        self.goal_storage = goal_storage

    @property
    def account_service(self):
        return ServiceAdapter().sales_crm_service

    def get_user_public_goals_wrapper(
        self, session_token: str, user_id: int, presenter: PresenterInterface
    ):
        try:
            goal_dtos = self.get_user_public_goals(
                session_token=session_token, user_id=user_id
            )
            return presenter.get_user_goals_http_response(goal_dtos=goal_dtos)
        except InvalidSessionToken:
            return presenter.get_invalid_access_token_http_error()

    def get_user_public_goals(
        self, session_token: str, user_id: int
    ) -> List[GoalDTO]:
        self.validate_session_token(session_token=session_token)
        return self.goal_storage.get_user_public_goals(user_id=user_id)

    def validate_session_token(self, session_token: str):
        is_valid = self.account_service.is_session_token_valid(
            session_token=session_token
        )

        if not is_valid:
            raise InvalidSessionToken(session_token=session_token)
