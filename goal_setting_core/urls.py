from django.urls import path

from goal_setting_core.views.create_goal import create_goal
from goal_setting_core.views.delete_goal import delete_goal
from goal_setting_core.views.get_goal import get_goal
from goal_setting_core.views.get_user_goals import get_user_goals

urlpatterns = [
    path("goals/create", create_goal),
    path("goals", get_user_goals),
    path("goals/<str:goal_id>", get_goal),
    path("goals/<str:goal_id>/delete", delete_goal),
    path("goals/goals/<str:goal_id>/status", update_goal_staus),
]
