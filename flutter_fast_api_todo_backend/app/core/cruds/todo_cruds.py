from sqlalchemy.orm import Session
from app.core.models import todo_model
from app.core.schemas import todo_schema
from fastapi import HTTPException, status


def createTodo(db: Session, todo: todo_schema.TodoCreate, email: str):
    db_todo = todo_model.Todo(
        user_email=email,
        title=todo.title,
        description=todo.description,
        is_daily=todo.is_daily,
    )
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo


def get_todos_by_user_id(db: Session, user_id: str):
    return db.query(todo_model.Todo).filter(todo_model.Todo.user_id == user_id)


def get_todo_by_id(db: Session, todo_id: int):
    return db.query(
        todo_model.Todo).filter(todo_model.Todo.todo_id == todo_id).first()


def update_todo(db: Session, todo: todo_schema.TodoUpdate, todo_id: int):
    db_item = (db.query(
        todo_model.Todo).filter(todo_model.Todo.todo_id == todo_id).first())
    if db_item:
        for key, value in todo.model_dump().items():
            if hasattr(db_item, key):
                setattr(db_item, key, value)
    db.commit()
    db.refresh(db_item)
    return db_item


def todo_done(db: Session, todo_id: str):
    db_item = (db.query(
        todo_model.Todo).filter(todo_model.Todo.todo_id == todo_id).first())
    db_item.is_done = True
    db.commit()
    db.refresh(db_item)
    return db_item


def check_todo_exist_and_is_owner(db: Session, todo_id: int, email: str):
    todo_item = get_todo_by_id(db=db, todo_id=todo_id)
    print(email)
    print(todo_id)
    print(todo_item)
    if not todo_item:
        print("WE ARE HERHEHRHEH")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The Todo does not exist",
        )
    todo = todo_schema.Todo.model_validate(todo_item)
    print(todo.user_email)
    print(email)
    if todo.user_email != email:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="This todo does not belong to you",
        )
    return todo


def delete_todo(db: Session, todo_id: str):
    db_item = (db.query(
        todo_model.Todo).filter(todo_model.Todo.todo_id == todo_id).first())
    if db_item:
        db.delete(db_item)
        db.commit()
        return True
    return False
