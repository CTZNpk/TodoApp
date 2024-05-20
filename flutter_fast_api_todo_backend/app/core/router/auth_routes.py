from app.core.cruds import user_cruds
from app.core.dependencies import (
    email_format_dependency,
    password_format_dependency,
    oauth2_form_dependency,
    db_dependency,
)
from app.core.schemas import user_schema
from datetime import datetime, timedelta, timezone
from app.core.config import settings
from jose import jwt
from fastapi import APIRouter
from fastapi import HTTPException, status
import bcrypt

router = APIRouter(tags=["auth"], )


def generate_jwt_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
        to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode,
                             settings.JWT_SECRET_KEY,
                             algorithm=settings.JWT_ALGORITHM)
    return encoded_jwt


def get_token_and_user(email, id):
    user = user_schema.User(email=email, id=id)

    access_token = generate_jwt_token(data={"sub": email})
    return {"access-token": access_token, "token-type": "bearer", "user": user}


@router.post(
    "/signup",
    dependencies=[password_format_dependency, email_format_dependency])
async def signup_user(db: db_dependency, form_data: oauth2_form_dependency):
    db_user = user_cruds.get_user_by_email(db, form_data.username)
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with email already exists",
        )
    db_user = user_cruds.create_user(
        db,
        user_schema.UserCreate(email=form_data.username,
                               password=form_data.password),
    )
    return get_token_and_user(form_data.username, db_user.id)


def __verify_password(password, hashed_password):
    password_bytes = password.encode("utf-8")
    hash_pass_bytes = hashed_password.encode("utf-8")

    if not bcrypt.checkpw(password_bytes, hash_pass_bytes):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Incorrect Password")


@router.post(
    "/login",
    dependencies=[password_format_dependency, email_format_dependency])
async def login_user(db: db_dependency, form_data: oauth2_form_dependency):
    db_user = user_cruds.get_user_by_email(db, form_data.username)
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The User with the email does not exist",
        )
    __verify_password(form_data.password, db_user.hashed_password)

    user = user_schema.User(email=db_user.email, id=db_user.id)

    access_token = generate_jwt_token(data={"sub": form_data.username})
    return {"access-token": access_token, "token-type": "bearer", "user": user}
