from datetime import datetime
from pydantic import BaseModel, ConfigDict


class TodoBase(BaseModel):
    description: str
    title: str
    is_daily: bool


class TodoCreate(TodoBase):
    pass


class TodoUpdate(TodoBase):
    is_done: bool


class Todo(TodoBase):
    user_email: str
    todo_id: int
    created_time: datetime
    is_done: bool

    model_config = ConfigDict(from_attributes=True)
