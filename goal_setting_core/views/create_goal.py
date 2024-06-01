from rest_framework.decorators import api_view

from accounts.dtos import UserLoginParamsDTO
from accounts.views import UserLoginSerializer
from goal_setting_core.interactor.create_goal import CreateGoalInteractor
from goal_setting_core.presenters.presenter import Presenter
from goal_setting_core.storages.goal_storage import GoalStorage


@api_view(["POST"])
def create_goal(request):
    post_body = request.data
    serializer = UserLoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    create_goal_parameter_dto = UserLoginParamsDTO(
        user_name=post_body["user_name"],
        password=post_body["password"],
    )

    goal_storage = GoalStorage()
    presenter = Presenter()
    interactor = CreateGoalInteractor(goal_storage=goal_storage)
    return interactor.create_goal_wrapper(
        create_goal_parameter_dto=create_goal_parameter_dto,
        presenter=presenter,
    )
