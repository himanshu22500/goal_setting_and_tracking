from rest_framework.decorators import api_view

from accounts.dtos import CreateGoalParamsDTO
from accounts.views import CreateGoalSerializer
from goal_setting_core.interactor.get_user_goals import GetUserGoalsInteractor
from goal_setting_core.presenters.presenter import Presenter
from goal_setting_core.storages.goal_storage import GoalStorage


@api_view(["GET"])
def get_user_goals(request):
    session_token = request.META.get("HTTP_AUTHORIZATION")
    if session_token:
        session_token = session_token.split()[1]

    goal_storage = GoalStorage()
    presenter = Presenter()
    interactor = GetUserGoalsInteractor(goal_storage=goal_storage)
    return interactor.get_user_goals_wrapper(
        session_token=session_token,
        presenter=presenter,
    )
