from pathlib import Path

from src.common.config.env import StrEnv, IntEnv, BoolEnv

__all__ = [
    "DEBUG",
    "API_TOKEN",
    "FOLDER_ID",
    "API_YANDEX",
    "LOGGING_PATH",
    "REDIS_HOST",
    "REDIS_PORT",
]


DEBUG: bool = BoolEnv("DEBUG")

API_TOKEN: str = StrEnv("API_TOKEN")

FOLDER_ID: str = StrEnv("FOLDER_ID")
API_YANDEX: str = StrEnv("API_YANDEX")

LOGGING_PATH: Path = Path(StrEnv("LOGGING_PATH"))

REDIS_HOST: str = StrEnv("REDIS_HOST")
REDIS_PORT: int = IntEnv("REDIS_PORT")


