from app.core.cruds import todo_cruds, user_cruds
from app.core.dependencies import (
    db_dependency,
    protected_path_dependency,
    get_email_dependency,
)
from app.core.schemas import todo_schema
from fastapi import APIRouter
from fastapi import HTTPException, status

router = APIRouter(tags=["todo"],
                   prefix="/todo",
                   dependencies=[protected_path_dependency])


@router.post("/")
def create_todo(db: db_dependency, todo: todo_schema.TodoCreate):
    db_item = todo_cruds.createTodo(db, todo)
    todoResponse = todo_schema.Todo.from_orm(db_item)
    return {"detail": "Todo Created Successfully", "todo": todoResponse}


@router.get("/")
def get_user_todos(db: db_dependency, email: get_email_dependency):
    current_user = user_cruds.get_user_by_email(email)
    if not current_user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="The User is inactive",
        )
    return current_user.todos


@router.get("/{todo_id}")
def get_todo_from_id(db: db_dependency, email: get_email_dependency, todo_id):
    todo = todo_cruds.check_todo_exist_and_is_owner(db=db,
                                                    email=email,
                                                    todo_id=todo_id)
    return todo


@router.patch("/{todo_id}")
def set_todo_done(db: db_dependency, email: get_email_dependency, todo_id):
    todo_cruds.check_todo_exist_and_is_owner(db=db,
                                             email=email,
                                             todo_id=todo_id)
    todo_item = todo_cruds.todo_done(db=db, todo_id=todo_id)
    todo = todo_schema.Todo.from_orm(todo_item)
    return {"detail": "Todo updated successfully", "todo": todo}


@router.patch("/{todo_id}")
def update_todo(db: db_dependency, email: get_email_dependency, todo_id):
    todo = todo_cruds.check_todo_exist_and_is_owner(db=db,
                                                    email=email,
                                                    todo_id=todo_id)
    todo_item = todo_cruds.update_todo(db=db, todo=todo)
    todo = todo_schema.Todo.from_orm(todo_item)
    return {"detail": "Todo updated successfully", "todo": todo}


@router.delete("/{todo_id}")
def delete_todo(db: db_dependency, email: get_email_dependency, todo_id):
    todo_cruds.check_todo_exist_and_is_owner(db=db,
                                             email=email,
                                             todo_id=todo_id)
    todo_cruds.delete_todo(db=db, todo_id=todo_id)
    return {"detail": "Todo deleted successfully"}
