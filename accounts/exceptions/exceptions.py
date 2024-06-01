class InvalidEmail(Exception):
    def __init__(self, email: str):
        self.email = email


class InvalidUserName(Exception):
    def __init__(self, user_name: str):
        self.user_name = user_name


class InvalidPassword(Exception):
    def __init__(self, password: str):
        self.password = password


class UserNameAlreadyExists(Exception):
    def __init__(self, user_name: str):
        self.user_name = user_name


class EmailAlreadyExists(Exception):
    def __init__(self, email: str):
        self.email = email


class InvalidLoginUsernameOrPassword(Exception):
    def __init__(self, password: str, user_name: str):
        self.password = password
        self.user_name = user_name


class InvalidAccessToken(Exception):
    def __init__(self, access_token: str):
        self.access_token = access_token
