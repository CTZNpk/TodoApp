from fastapi import APIRouter
from app.core.cruds import user_cruds
from app.core.schemas import user_schema
from app.core.dependencies import (
    protected_path_dependency,
    db_dependency,
    get_email_dependency,
)

router = APIRouter(tags=["user"],
                   prefix="/user",
                   dependencies=[protected_path_dependency])


@router.get("/")
def get_current_user(db: db_dependency, email: get_email_dependency):
    db_user = user_cruds.get_user_by_email(db=db, email=email)
    user = user_schema.User.model_validate(db_user)
    return user
