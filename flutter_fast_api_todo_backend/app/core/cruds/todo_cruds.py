from sqlalchemy.orm import Session
from app.core.models import todo_model
from app.core.schemas import todo_schema


def createTodo(db: Session, todo: todo_schema.TodoCreate):
    db_todo = todo_model.Todo(
        user_id=todo.user_id,
        title=todo.title,
        description=todo.description,
        is_daily=todo.is_daily,
        deadline_time=todo.deadline_time,
    )
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo


def get_todos_by_user_id(db: Session, user_id: str):
    return db.query(todo_model.Todo).filter(todo_model.Todo.user_id == user_id)


def get_todo_by_id(db: Session, todo_id: str):
    return db.query(
        todo_model.Todo).filter(todo_model.Todo.todo_id == todo_id).first()


def update_todo(
    db: Session,
    todo: todo_schema.TodoUpdate,
):
    db_item = (db.query(todo_model.Todo).filter(
        todo_model.Todo.todo_id == todo.todo_id).first())
    if db_item:
        for key, value in todo.dict().items():
            if hasattr(db_item, key):
                setattr(db_item, key, value)
    db.commit()
    db.refresh(db_item)
    return db_item


def todo_done(db: Session, todo_id: str):
    db_item = (db.query(
        todo_model.Todo).filter(todo_model.Todo.todo_id == todo_id).first())
    db["is_done"] = True
    db.commit()
    db.refresh(db_item)
    return db_item


def delete_todo(db: Session, todo_id: str):
    db_item = (db.query(
        todo_model.Todo).filter(todo_model.Todo.todo_id == todo_id).first())
    if db_item:
        db.delete(db_item)
        db.commit()
        return True
    return False
