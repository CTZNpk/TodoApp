from app.core.cruds import todo_cruds
from app.core.dependencies import (
    db_dependency,
    get_current_active_user_dependency,
)
from app.core.schemas import todo_schema
from fastapi import APIRouter

router = APIRouter(
    tags=["todo"],
    prefix="/todo",
)


@router.post("/")
def create_todo(
    db: db_dependency,
    todo: todo_schema.TodoCreate,
    user: get_current_active_user_dependency,
):
    db_item = todo_cruds.createTodo(db=db, todo=todo, email=user.email)
    todoResponse = todo_schema.Todo.model_validate(db_item)
    return {"detail": "Todo Created Successfully", "todo": todoResponse}


@router.get("/")
def get_user_todos(db: db_dependency,
                   user: get_current_active_user_dependency):
    return user.todos


@router.get("/{todo_id}")
def get_todo_from_id(db: db_dependency,
                     user: get_current_active_user_dependency, todo_id):
    todo = todo_cruds.check_todo_exist_and_is_owner(db=db,
                                                    email=user.email,
                                                    todo_id=todo_id)
    return todo


@router.patch("/{todo_id}/done")
def set_todo_done(db: db_dependency, user: get_current_active_user_dependency,
                  todo_id):
    todo_cruds.check_todo_exist_and_is_owner(db=db,
                                             email=user.email,
                                             todo_id=todo_id)
    todo_item = todo_cruds.todo_done(db=db, todo_id=todo_id)
    todo = todo_schema.Todo.from_orm(todo_item)
    return {"detail": "Todo updated successfully", "todo": todo}


@router.patch("/{todo_id}")
def update_todo(
    db: db_dependency,
    user: get_current_active_user_dependency,
    todo_id,
    todo: todo_schema.Todo,
):
    todo_cruds.check_todo_exist_and_is_owner(db=db,
                                             email=user.email,
                                             todo_id=todo_id)
    todo_item = todo_cruds.update_todo(db=db, todo=todo)
    todo = todo_schema.Todo.from_orm(todo_item)
    return {"detail": "Todo updated successfully", "todo": todo}


@router.delete("/{todo_id}")
def delete_todo(db: db_dependency, user: get_current_active_user_dependency,
                todo_id):
    todo_cruds.check_todo_exist_and_is_owner(db=db,
                                             email=user.email,
                                             todo_id=todo_id)
    todo_cruds.delete_todo(db=db, todo_id=todo_id)
    return {"detail": "Todo deleted successfully"}
