from functools import lru_cache
from urllib.parse import quote_plus
from pydantic_settings import BaseSettings
from decouple import config


class Settings(BaseSettings):

    # App
    APP_NAME:  str = config("APP_NAME", "App FastAPI")
    DEBUG: bool = bool(config("DEBUG", False))
    
    # FrontEnd Application
    FRONTEND_HOST: str = config("FRONTEND_HOST", "http://localhost:5173")

    # Mongo Database Config
    MONGO_HOST: str = config("MONGO_HOST", 'localhost')
    MONGO_USER: str = config("MONGO_USER", 'root')
    MONGO_PASS: str = config("MONGO_PASSWORD", '')
    MONGO_PORT: int = int(config("MONGO_PORT", 27017))
    MONGO_DB: str = config("MONGO_DB", 'taskdb')
    DATABASE_URI: str = f"mongodb://{MONGO_USER}:%s@{MONGO_HOST}:{MONGO_PORT}/{MONGO_DB}" % quote_plus(MONGO_PASS)

    # JWT Secret Key
    JWT_SECRET: str = config("JWT_SECRET", "")
    JWT_ALGORITHM: str = config("ACCESS_TOKEN_ALGORITHM", "HS256")
    # ACCESS_TOKEN_EXPIRE_MINUTES: int = int(config("ACCESS_TOKEN_EXPIRE_MINUTES", 3))
    # REFRESH_TOKEN_EXPIRE_MINUTES: int = int(config("REFRESH_TOKEN_EXPIRE_MINUTES", 1440))

    # App Secret Key
    SECRET_KEY: str = config("SECRET_KEY", "")


@lru_cache()
def get_settings() -> Settings:
    return Settings()