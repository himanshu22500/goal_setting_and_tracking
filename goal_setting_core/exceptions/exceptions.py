from datetime import datetime


class CategoryDoesNotExist(Exception):
    pass


class TitleMustNotBeEmpty(Exception):
    pass


class TargetDateMustBeInFuture(Exception):
    def __init__(self, target_datetime: datetime):
        self.target_date = target_datetime


class DueDateMustBeInFuture(Exception):
    def __init__(self, due_datetime: datetime):
        self.due_datetime = due_datetime


class InvalidAccessToken(Exception):
    def __init__(self, access_token: str):
        self.access_token = access_token


class InvalidGoalId(Exception):
    def __init__(self, goal_id: str):
        self.goal_id = goal_id
