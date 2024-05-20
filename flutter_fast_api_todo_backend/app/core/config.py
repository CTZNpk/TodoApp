from typing import List, Union

from pydantic import AnyHttpUrl, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    PROJECT_NAME: str
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []
    POSTGRESS_DB_URL: str
    TEST_DB_URL: str
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str
    SALT_KEY: str

    @field_validator("BACKEND_CORS_ORIGINS")
    def assemble_cors_origins(
            cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    model_config = SettingsConfigDict(env_file="app/.env", case_sensitive=True)


settings = Settings()
