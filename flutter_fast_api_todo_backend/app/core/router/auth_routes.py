from datetime import datetime, timedelta, timezone
from app.core.config import settings
from jose import jwt
from fastapi import APIRouter
from fastapi import HTTPException, status
from pydantic import BaseModel
from app.core.dependencies import (
    email_format_dependency,
    password_format_dependency,
    oauth2_form_dependency,
    db_dependency,
)
from app.core.cruds import user_cruds

router = APIRouter(tags=["auth"], )


class Token(BaseModel):
    access_token: str
    token_type: str


def generate_jwt_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
        to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode,
                             settings.JWT_SECRET_KEY,
                             algorithm=settings.JWT_ALGORITHM)
    return encoded_jwt


@router.post(
    "/signup",
    dependencies=[password_format_dependency, email_format_dependency])
async def signup_user(db: db_dependency, form_data: oauth2_form_dependency):
    db_user = user_cruds.get_user_by_email(db, form_data.username)
    if db_user:
        HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with email already exists",
        )
    access_token = generate_jwt_token(data={"sub": form_data.username})
    return Token(access_token=access_token, token_type="Bearer")
