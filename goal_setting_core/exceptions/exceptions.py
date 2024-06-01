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
