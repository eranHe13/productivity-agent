from datetime import datetime, date
from pydantic import BaseModel
from typing import Optional


class CategoryBase(BaseModel):
    name: str
    color: Optional[str] = None


class CategoryCreate(CategoryBase):
    pass


class Category(CategoryBase):
    id: int
    class Config:
        from_attributes = True


class TaskBase(BaseModel):
    title: str
    completed: bool = False
    due_date: Optional[datetime] = None
    category_id: Optional[int] = None


class TaskCreate(TaskBase):
    pass


class Task(TaskBase):
    id: int
    created_at: datetime
    category: Optional[Category]
    class Config:
        from_attributes = True


class DailyGoalBase(BaseModel):
    date: date
    title: str
    completed: bool = False


class DailyGoal(DailyGoalBase):
    id: int
    class Config:
        from_attributes = True


class FocusSessionBase(BaseModel):
    start_ts: datetime
    end_ts: Optional[datetime] = None
    duration_sec: Optional[int] = None
    type: Optional[str] = None
    interrupted: bool = False


class FocusSession(FocusSessionBase):
    id: int
    class Config:
        from_attributes = True


class CoachPromptBase(BaseModel):
    question: str
    answer: Optional[str] = None
    ts: Optional[datetime] = None
    model: Optional[str] = None
    tokens_in: int = 0
    tokens_out: int = 0


class CoachPrompt(CoachPromptBase):
    id: int
    class Config:
        from_attributes = True
