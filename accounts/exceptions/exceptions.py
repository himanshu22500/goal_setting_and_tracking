class InvalidEmail(Exception):
    def __init__(self, email: str):
        self.email = email


class InvalidUserName(Exception):
    def __init__(self, user_name: str):
        self.user_name = user_name


class InvalidPassword(Exception):
    def __init__(self, password: str):
        self.password = password
