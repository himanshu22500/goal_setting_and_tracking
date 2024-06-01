from dataclasses import dataclass
from datetime import datetime
from typing import Optional


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


@dataclass
class CreateGoalParamsDTO:
    title: str
    description: Optional[str]
    category: str
    target_datetime: datetime
    due_datetime: Optional[datetime]
    priority: Optional[int]
    is_public: Optional[bool]
    session_token: str


@dataclass
class UpdateGoalParamsDTO:
    title: Optional[str]
    description: Optional[str]
    category: Optional[str]
    target_datetime: Optional[datetime]
    due_datetime: Optional[datetime]
    completed: Optional[bool]
    priority: Optional[int]
    is_public: Optional[bool]
    session_token: str
    update_text: Optional[str]
