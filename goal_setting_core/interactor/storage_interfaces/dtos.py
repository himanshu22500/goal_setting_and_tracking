from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class GoalDTO:
    id: str
    title: str
    description: Optional[str]
    target_datetime: datetime
    due_datetime: Optional[datetime]
    priority: Optional[int]
    is_public: Optional[bool]
