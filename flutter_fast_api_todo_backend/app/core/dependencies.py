import re
from fastapi import Depends
from app.core.database import get_db
from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

db_dependency = Annotated[Session, Depends(get_db)]

oauth2_scheme_dependency = Annotated[
    str,
    Depends(OAuth2PasswordBearer(tokenUrl="token"), ),
]

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
