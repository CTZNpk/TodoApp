from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from app.core.database import Base


class User(Base):
    __tablename__ = "users"

    id: Column(Integer, primary_key=True)
    email: Column(String, unique=True, index=True)
    hashed_password: Column(String)
    is_active: Column(Boolean, default=True)

    # todos = relationship("Item", back_populates="owner")
