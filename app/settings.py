from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    TOKEN: str
    DB_PROTOCOL: str = "sqlite"  # sqlite / postgresql / mysql

    ADMIN_ID: int

    USE_REDIS: bool = False
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379
    REDIS_PASSWORD: str = ""

    DB_USERNAME: str = "root"  # если используется sqlite, то не нужно
    DB_PASSWORD: str = "root"
    DB_HOST: str = "localhost"
    DB_PORT: int = 3306

    DB_SQLITE_DIR: str = "app/db/bot.db"


@lru_cache()
def settings():
    return Settings(
        _env_file=".env",
        _env_file_encoding="utf-8",
    )
