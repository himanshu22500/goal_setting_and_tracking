from django.urls import path

from goal_setting_core.views.create_goal import create_goal

urlpatterns = [path("create_goal", create_goal)]
