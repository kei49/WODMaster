import secrets
import os
from typing import Any, Dict, List, Optional, Union

from pydantic import AnyHttpUrl, BaseSettings, EmailStr, HttpUrl, PostgresDsn, validator


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    SERVER_NAME: str = "test"
    SERVER_HOST: AnyHttpUrl = "http://localhost:8000"
    # BACKEND_CORS_ORIGINS is a JSON-formatted list of origins
    # e.g: '["http://localhost", "http://localhost:4200", "http://localhost:3000", \
    # "http://localhost:8080", "http://local.dockertoolbox.tiangolo.com"]'
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)


    fastapi_env = os.getenv('FASTAPI_ENV', 'dev')

    MYSQL_SERVER: str = os.getenv('MYSQL_SERVER', 'default')
    MYSQL_USER: str = os.getenv('MYSQL_USER', 'default')
    MYSQL_PASSWORD: str = os.getenv('MYSQL_PASSWORD', 'default')

    MYSQL_DB: str = "dev_v2"
    PROJECT_NAME: str = "WODMaster(local)"

    if fastapi_env == "staging":
        PROJECT_NAME: str = "WODMaster(Staging)"
        MYSQL_DB: str = "staging_v1"
    elif fastapi_env == "production":
        PROJECT_NAME: str = "WODMaster"
        MYSQL_DB: str = "production_v1"

    #SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn] = "test"
    MYSQL_URI = "mysql+pymysql://{}:{}@{}/{}".format(MYSQL_USER, MYSQL_PASSWORD, MYSQL_SERVER, MYSQL_DB)


settings = Settings()
