from datetime import datetime

from rest_framework.decorators import api_view

from accounts.dtos import UpdateGoalParamsDTO
from accounts.views import UpdateGoalSerializer
from goal_setting_core.interactor.update_goal import UpdateGoalInteractor
from goal_setting_core.presenters.presenter import Presenter
from goal_setting_core.storages.goal_storage import GoalStorage


@api_view(["PUT"])
def update_goal(request, goal_id):
    session_token = request.META.get("HTTP_AUTHORIZATION")
    if session_token:
        session_token = session_token.split()[1]

    post_body = request.data
    serializer = UpdateGoalSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    due_datetime = post_body.get("due_datetime")
    if due_datetime:
        due_datetime = datetime.strptime(due_datetime, "%Y-%m-%d %H:%M:%S.%f")

    target_datetime = post_body.get("target_datetime")
    if target_datetime:
        target_datetime = datetime.strptime(
            target_datetime, "%Y-%m-%d %H:%M:%S.%f"
        )

    update_goal_params_dto = UpdateGoalParamsDTO(
        title=post_body.get("title"),
        description=post_body.get("description"),
        category=post_body.get("category"),
        target_datetime=target_datetime,
        due_datetime=due_datetime,
        priority=post_body.get("priority"),
        is_public=post_body.get("is_public"),
        session_token=session_token,
        update_text=post_body.get("update_text"),
        completed=post_body.get("completed"),
    )

    goal_storage = GoalStorage()
    presenter = Presenter()
    interactor = UpdateGoalInteractor(goal_storage=goal_storage)
    return interactor.update_goal_wrapper(
        session_token=session_token,
        update_goal_params_dto=update_goal_params_dto,
        presenter=presenter,
        goal_id=goal_id,
    )
