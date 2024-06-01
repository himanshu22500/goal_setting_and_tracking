from datetime import datetime

from rest_framework.decorators import api_view

from accounts.dtos import CreateGoalParamsDTO
from accounts.views import CreateGoalSerializer
from goal_setting_core.interactor.create_goal import CreateGoalInteractor
from goal_setting_core.presenters.presenter import Presenter
from goal_setting_core.storages.goal_storage import GoalStorage


@api_view(["POST"])
def create_goal(request):
    session_token = request.META.get("HTTP_AUTHORIZATION")
    if session_token:
        session_token = session_token.split()[1]

    post_body = request.data
    serializer = CreateGoalSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    due_datetime = post_body.get("due_datetime")
    if due_datetime:
        due_datetime = datetime.strptime(due_datetime, "%Y-%m-%d %H:%M:%S.%f")

    create_goal_parameter_dto = CreateGoalParamsDTO(
        title=post_body["title"],
        description=post_body.get("description"),
        category=post_body["category"],
        target_datetime=datetime.strptime(
            post_body["target_datetime"], "%Y-%m-%d %H:%M:%S.%f"
        ),
        due_datetime=due_datetime,
        priority=post_body.get("priority"),
        is_public=post_body.get("is_public"),
        session_token=session_token,
    )

    goal_storage = GoalStorage()
    presenter = Presenter()
    interactor = CreateGoalInteractor(goal_storage=goal_storage)
    return interactor.create_goal_wrapper(
        create_goal_parameter_dto=create_goal_parameter_dto,
        presenter=presenter,
    )
