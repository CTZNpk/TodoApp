import datetime
from pydantic import BaseModel, ConfigDict


class TodoBase(BaseModel):
    user_email: int
    description: str
    title: str
    is_daily: bool
    deadline_time: datetime | None


class TodoCreate(TodoBase):
    pass


class Todo(TodoBase):
    todo_id: int
    created_time: datetime
    is_done: bool

    model_config = ConfigDict(from_attributes=True)
