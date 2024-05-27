from fastapi import APIRouter
from app.core.cruds import user_cruds
from app.core.schemas import user_schema
from app.core.dependencies import (
    db_dependency,
    get_current_active_user_dependency,
)

router = APIRouter(
    tags=["user"],
    prefix="/user",
)


@router.get("/")
def get_current_user(
    db: db_dependency,
    user: get_current_active_user_dependency,
):
    db_user = user_cruds.get_user_by_email(db=db, email=user.email)
    user = user_schema.User.model_validate(db_user)
    return user


@router.patch("/disable")
def disable_current_user(
    db: db_dependency,
    user_model: get_current_active_user_dependency,
):
    user = user_schema.User.model_validate(user_model)
    user.is_active = False
    db_user = user_cruds.update_user(db=db, user=user)
    return db_user
