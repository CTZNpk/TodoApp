from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.core.database import Base


class Todo(Base):
    __tablename__ = "todos"

    todo_id = Column(Integer, primary_key=True, autoincrement=True)
    user_email = Column(String, ForeignKey("users.email"))
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    is_done = Column(Boolean, default=False)
    is_daily = Column(Boolean, default=False)
    created_time = Column(DateTime(timezone=True), server_default=func.now())

    user = relationship("User", back_populates="todos")
