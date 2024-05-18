from fastapi import Depends
from app.core.database import get_db
from typing import Annotated
from sqlalchemy.orm import Session

db_dependency = Annotated[Session, Depends(get_db)]
