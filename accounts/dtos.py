from dataclasses import dataclass


@dataclass
class CreateUserParamsDTO:
    user_name: str
    password: str
    email: str
