from django.contrib import admin

from goal_setting_core.models.models import Category, Goal, GoalUpdate

admin.site.register(Goal)
admin.site.register(GoalUpdate)
admin.site.register(Category)
