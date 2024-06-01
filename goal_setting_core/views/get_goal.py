from rest_framework.decorators import api_view

from goal_setting_core.interactor.get_goal import GetGoalInteractor
from goal_setting_core.presenters.presenter import Presenter
from goal_setting_core.storages.goal_storage import GoalStorage


@api_view(["GET"])
def get_goal(request, goal_id):
    session_token = request.META.get("HTTP_AUTHORIZATION")
    if session_token:
        session_token = session_token.split()[1]

    goal_storage = GoalStorage()
    presenter = Presenter()
    interactor = GetGoalInteractor(goal_storage=goal_storage)
    return interactor.get_goal_wrapper(
        session_token=session_token,
        goal_id=goal_id,
        presenter=presenter,
    )
