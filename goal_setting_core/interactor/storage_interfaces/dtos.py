from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class GoalDTO:
    id: str
    user_id: int
    title: str
    description: Optional[str]
    category: str
    target_datetime: datetime
    due_datetime: Optional[datetime]
    is_completed: bool
    priority: Optional[int]
    is_public: Optional[bool]
