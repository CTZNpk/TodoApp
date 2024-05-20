from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from app.core.config import settings
from sqlalchemy.orm import sessionmaker
from app.core.database import Base
from app.main import app
from app.core.database import get_db

engine = create_engine(settings.TEST_DB_URL)
TestingSessionLocal = sessionmaker(autocommit=False,
                                   autoflush=False,
                                   bind=engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

Base.metadata.create_all(bind=engine)

client = TestClient(app)


def test_api():
    response = client.get("/")
    assert response.status_code == 200
