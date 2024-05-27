from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.database import engine
from app.core.database import Base
from app.core.router import auth_routes, todo_routes, user_routes

from app.core.config import settings


def get_application():
    _app = FastAPI(title=settings.PROJECT_NAME, lifespan=lifespan)

    _app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            str(origin) for origin in settings.BACKEND_CORS_ORIGINS
        ],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return _app


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


app = get_application()

app.include_router(auth_routes.router)
app.include_router(todo_routes.router)
app.include_router(user_routes.router)


@app.get("/")
def default():
    return "The Api is working"
