import uuid
from sqlalchemy.orm import Session
from app.core.models import user_model
from app.core.schemas import user_schema
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], depricated="auto")


def get_hash_password(password: str):
    return pwd_context.hash(password)


def get_user_by_email(db: Session, email: str):
    return db.query(
        user_model.User).filter(user_model.User.email == email).first()


def get_user_by_id(db: Session, id: int):
    return db.query(user_model.User).filter(user_model.User.id == id).first()


def create_user(db: Session, user: user_schema.UserCreate):
    hashed_password = get_hash_password(user.password)
    db_user = user_model.User(id=uuid.uuid4(),
                              email=user.email,
                              hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh()
    return db_user
