from datetime import datetime


class CategoryDoesNotExist(Exception):
    def __init__(self, category: str):
        self.category = category


class TitleMustNotBeEmpty(Exception):
    pass


class TargetDateMustBeInFuture(Exception):
    def __init__(self, target_datetime: datetime):
        self.target_date = target_datetime


class DueDateMustBeInFuture(Exception):
    def __init__(self, due_datetime: datetime):
        self.due_datetime = due_datetime


class InvalidSessionToken(Exception):
    def __init__(self, session_token: str):
        self.access_token = session_token


class InvalidGoalId(Exception):
    def __init__(self, goal_id: str):
        self.goal_id = goal_id


class GoalDoseNotBelongToUser(Exception):
    def __init__(self, goal_id: str, user_id: str):
        self.goal_id = goal_id
        self.user_id = user_id
