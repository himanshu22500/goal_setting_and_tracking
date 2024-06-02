from rest_framework.decorators import api_view

from goal_setting_core.interactor.get_user_public_goals import (
    GetUserPublicGoals,
)
from goal_setting_core.presenters.presenter import Presenter
from goal_setting_core.storages.goal_storage import GoalStorage


@api_view(["GET"])
def get_user_public_goals(request, user_id):
    session_token = request.META.get("HTTP_AUTHORIZATION")
    if session_token:
        session_token = session_token.split()[1]

    goal_storage = GoalStorage()
    presenter = Presenter()
    interactor = GetUserPublicGoals(goal_storage=goal_storage)
    return interactor.get_user_public_goals_wrapper(
        session_token=session_token,
        user_id=user_id,
        presenter=presenter,
    )
