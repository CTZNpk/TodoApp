import re
from app.core.cruds import user_cruds
from app.core.config import settings
from fastapi import Depends
from jose import jwt, JWTError
from app.core.database import get_db
from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from app.core.models.user_model import User

db_dependency = Annotated[Session, Depends(get_db)]

oauth2_scheme_dependency = Annotated[
    str,
    Depends(OAuth2PasswordBearer(tokenUrl="login")),
]


async def __get_current_user(
        token: oauth2_scheme_dependency,
        db: Session = Depends(get_db),
):
    user = __verify_token_and_get_user(db=db, token=token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user


async def __get_current_active_user(
    current_user: Annotated[User, Depends(__get_current_user)], ):
    if not current_user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


get_current_active_user_dependency = Annotated[
    User, Depends(__get_current_active_user)]

oauth2_form_dependency = Annotated[OAuth2PasswordRequestForm, Depends()]


def check_password_format(form: oauth2_form_dependency):
    regex = r"^(?=.*[A-Z])(?=.*\d).{6,}$"
    if not re.match(regex, form.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Incorrect Password Format")


password_format_dependency = Depends(check_password_format)


def check_email_format(form: oauth2_form_dependency):
    regex = r"^[\w\.-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$"
    if not re.match(regex, form.username):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Incorrect Email Format")


email_format_dependency = Depends(check_email_format)


def __verify_token_and_get_user(token: str, db: Session):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token,
                             settings.JWT_SECRET_KEY,
                             algorithms=[settings.JWT_ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception

    except JWTError:
        raise credentials_exception

    user = user_cruds.get_user_by_email(db=db, email=username)
    if user is None:
        credentials_exception
    return user
