from dataclasses import dataclass


@dataclass
class CreateUserParamsDTO:
    user_name: str
    password: str
    email: str


@dataclass
class UserLoginParamsDTO:
    user_name: str
    password: str


@dataclass
class UserLoginSessionDTO:
    user_id: int
    session_token: str
