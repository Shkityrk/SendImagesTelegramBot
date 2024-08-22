from enum import StrEnum, unique

__all__ = [
    "KeyBases"
]


@unique
class KeyBases(StrEnum):
    """Base for keys in Redis. Key in redis consists of this base + user_id """
    pass