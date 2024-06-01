from datetime import datetime

from django.http import HttpResponse

from accounts.dtos import CreateGoalParamsDTO
from goal_setting_core.adapters.service_adapter import ServiceAdapter
from goal_setting_core.exceptions.exceptions import (
    CategoryDoesNotExist,
    DueDateMustBeInFuture,
    InvalidSessionToken,
    TargetDateMustBeInFuture,
    TitleMustNotBeEmpty,
)
from goal_setting_core.interactor.presenter_interfaces.presenter_interface import (
    PresenterInterface,
)
from goal_setting_core.interactor.storage_interfaces.goal_storage_interface import (
    GoalStorageInterface,
)


class CreateGoalInteractor:
    def __init__(self, goal_storage: GoalStorageInterface):
        self.goal_storage = goal_storage

    @property
    def account_service(self):
        return ServiceAdapter().sales_crm_service

    def create_goal_wrapper(
        self,
        create_goal_parameter_dto: CreateGoalParamsDTO,
        presenter: PresenterInterface,
    ) -> HttpResponse:
        try:
            goal_dto = self.create_goal(
                create_goal_parameter_dto=create_goal_parameter_dto
            )
            return presenter.get_goal_created_http_response(goal_dto=goal_dto)
        except TitleMustNotBeEmpty:
            return presenter.get_empty_title_http_error()
        except CategoryDoesNotExist:
            return presenter.get_invalid_category_http_error(
                category=create_goal_parameter_dto.category
            )
        except TargetDateMustBeInFuture:
            return presenter.get_invalid_target_datetime_http_error(
                target_datetime=create_goal_parameter_dto.target_datetime
            )
        except DueDateMustBeInFuture:
            return presenter.get_invalid_due_datetime_http_error(
                due_datetime=create_goal_parameter_dto.target_datetime
            )
        except InvalidSessionToken:
            return presenter.get_invalid_access_token_http_error()

    def create_goal(self, create_goal_parameter_dto: CreateGoalParamsDTO):
        self.validate_session_token(
            session_token=create_goal_parameter_dto.session_token
        )
        self.validate_creation_parameter(
            create_goal_parameter_dto=create_goal_parameter_dto
        )
        user_id = self.account_service.get_user_id(
            session_token=create_goal_parameter_dto.session_token
        )
        return self.goal_storage.create_user_goal(
            user_id=user_id,
            create_goal_parameter_dto=create_goal_parameter_dto,
        )

    def validate_creation_parameter(
        self, create_goal_parameter_dto: CreateGoalParamsDTO
    ):
        self.validate_title(create_goal_parameter_dto.title)
        self.validate_category(create_goal_parameter_dto.category)
        self.validate_target_date(create_goal_parameter_dto.target_datetime)

        if create_goal_parameter_dto.due_datetime:
            self.validate_due_date(create_goal_parameter_dto.due_datetime)

    def validate_title(self, title):
        if title == "":
            raise TitleMustNotBeEmpty()

    def validate_category(self, category: str):
        is_valid_category = self.goal_storage.is_category_exists(
            category=category
        )
        if not is_valid_category:
            raise CategoryDoesNotExist()

    def validate_target_date(self, target_datetime):
        if target_datetime <= datetime.now():
            raise TargetDateMustBeInFuture(target_datetime=target_datetime)

    def validate_due_date(self, due_datetime):
        if due_datetime <= datetime.now():
            raise DueDateMustBeInFuture(due_datetime=due_datetime)

    def validate_session_token(self, session_token: str):
        is_valid = self.account_service.is_session_token_valid(
            session_token=session_token
        )

        if not is_valid:
            raise InvalidSessionToken(session_token=session_token)
